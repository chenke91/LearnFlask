from datetime import datetime

from flask import render_template,session,redirect,url_for
from flask.ext.login import login_required

from . import main
from .. import db
from ..models import Permission
from ..decorators import admin_required,permission_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return 'For administrators!'

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENT)
def for_moderators_only():
    return 'For comment moderators!'