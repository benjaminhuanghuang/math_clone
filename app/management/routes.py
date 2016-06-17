from flask import render_template, request, redirect, url_for , current_app
from flask_login import login_required

from . import management
from app.models.user import User

@management.route('/usermanagement', )
@login_required
def usermanagement():
    users = User.get_all_users()
    return render_template('management/userlist.html', users = users)


@management.route('/userdetail')
@login_required
def user_detail():
    return render_template('management/user_detail.html')

