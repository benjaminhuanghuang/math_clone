from flask import render_template, flash, redirect, url_for, abort,\
    request, current_app
from flask_login import login_required, current_user

from . import practice

@practice.route('/courses/')
@login_required
def courses():
    return render_template('practice/courses.html')


@practice.route('/assignment/')
@login_required
def assignment():
    return render_template('practice/assignment.html')