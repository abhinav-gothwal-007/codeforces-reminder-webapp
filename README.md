# Codeforces Contest Reminder Web App

A simple Flask app that lets users subscribe with their email and an offset (minutes before start),  
then automatically sends reminder emails ahead of every upcoming Codeforces contest.

## Features

- User signup with email + offset (minutes before contest)
- Polls Codeforces API (`contest.list`) every hour
- Schedules per-contest emails via APScheduler
- Uses Flask-Mail (SMTP) for notifications
- SQLite backend (via SQLAlchemy + Flask-Migrate)

