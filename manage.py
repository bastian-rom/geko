import os
import sys
from extensions import db
from models import User
from landing import app

def create_admin(email=None, password=None):
    email = email or os.environ.get('ADMIN_EMAIL')
    password = password or os.environ.get('ADMIN_PASSWORD')
    if not email or not password:
        print('Provide ADMIN_EMAIL and ADMIN_PASSWORD as env vars or pass them as args.')
        return
    with app.app_context():
        existing = User.query.filter_by(email=email).first()
        if existing:
            print('User already exists:', email)
            if existing.role != 'admin':
                existing.role = 'admin'
                db.session.commit()
                print('Promoted existing user to admin.')
            return
        user = User(email=email, role='admin')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print('Admin created:', email)

if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'create-admin':
        create_admin(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif len(sys.argv) == 2 and sys.argv[1] == 'create-admin':
        create_admin()
    else:
        print('Usage:')
        print('  python manage.py create-admin [email] [password]')