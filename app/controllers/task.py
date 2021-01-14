# -*- coding: utf-8 -*-
import functools, json, requests

from flask import flash, redirect, render_template, request
from flask import Blueprint, session, url_for, g

from app.models.task import Task
from app.settings import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET
from app.services.github import GitHub

blueprint = Blueprint('task', __name__)

@blueprint.before_app_request
def get_current_task():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = Task.query.filter_by(id=task).first()
