# scheduler.py

import datetime
import requests
from flask_apscheduler import APScheduler
from flask_mail import Message, Mail
from models import User

mail = Mail()
sched = APScheduler()

CODEFORCES_API = "https://codeforces.com/api/contest.list"

def fetch_upcoming_contests():
    """Return all contests that haven’t finished yet."""
    resp = requests.get(CODEFORCES_API).json()
    return [c for c in resp['result'] if c['phase'] == 'BEFORE']

def send_daily_report():
    """Email each user a list of contests starting within the next 48 hours."""
    with sched.app.app_context():
        now = datetime.datetime.utcnow()
        cutoff = now + datetime.timedelta(days=2)

        upcoming = []
        for c in fetch_upcoming_contests():
            start = datetime.datetime.utcfromtimestamp(c['startTimeSeconds'])
            if now < start <= cutoff:
                upcoming.append((c['name'], start))

        if not upcoming:
            return  # nothing to report

        # build the email body
        lines = ["Here are the Codeforces contests coming up in the next 2 days:\n"]
        for name, start in sorted(upcoming, key=lambda x: x[1]):
            lines.append(f"- {name} at {start.strftime('%Y-%m-%d %H:%M UTC')}")
        body = "\n".join(lines)

        # send to all subscribers
        for user in User.query.all():
            msg = Message(
                subject="[Codeforces] Upcoming contests in next 48 hours",
                recipients=[user.email],
                body=body
            )
            mail.send(msg)

def init_scheduler(app):
    mail.init_app(app)
    sched.init_app(app)
    sched.start()
    # schedule report at 00:00 UTC every day
    sched.add_job(
        id='daily_cf_report',
        func=send_daily_report,
        trigger='cron',
        hour=0,
        minute=0,
        timezone='UTC'
    )
