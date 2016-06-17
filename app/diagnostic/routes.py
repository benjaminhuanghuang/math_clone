from flask import render_template, request, redirect, url_for , current_app

from . import diagnostic

@diagnostic.route('/makecrash')
def makecrash():
    return render_template('diagnostic/index.html')




