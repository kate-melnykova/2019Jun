from celery import Celery
from flask import Flask
from flask import url_for
from flask import redirect
from flask import request
from flask import render_template
import flask_login
import json
from redis import Redis


def factory_app():
    app = Flask(__name__, instance_relative_config=True, template_folder='templates')
    app.secret_key = '1e9424b4-737b-4f49-91fa-cdb6290984e7'
    app.config.from_object('config')

    celery = Celery(app.name)
    celery.set_default()
    celery.conf.update(app.config)
    celery.config_from_object('celeryconf')
    return app, celery