from flask import abort
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from extensions import db
from models import User

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and getattr(current_user, 'role', '') == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return abort(403)

def init_admin(app, admin):
    # Add your models here for management in Flask-Admin
    admin.add_view(AdminModelView(User, db.session))