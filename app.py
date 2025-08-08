from flask import Flask, render_template, request, redirect, flash, url_for
from flask_migrate import Migrate

from config   import Config
from models   import db, User
from scheduler import init_scheduler

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    @app.route('/', methods=['GET','POST'])
    def index():
        if request.method == 'POST':
            email = request.form['email'].strip()
            if not email:
                flash('Please enter a valid email.', 'warning')
            elif User.query.filter_by(email=email).first():
                flash('Email already subscribed', 'warning')
            else:
                u = User(email=email)
                db.session.add(u)
                db.session.commit()
                flash('Subscribed successfully!', 'success')
            return redirect(url_for('index'))

        users = User.query.all()
        return render_template('index.html', users=users)

    return app

app = create_app()
init_scheduler(app)

if __name__ == '__main__':
    app.run()