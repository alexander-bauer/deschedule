from app import app, db, models, api

import flask
from flask import request, render_template
from flask.ext.api.decorators import set_renderers
from flask.ext.api.renderers import HTMLRenderer
import sqlalchemy

from app.renderers import ICalendarRenderer

@app.route('/')
@app.route('/index')
@set_renderers(HTMLRenderer)
def index():
    return render_template('index.html',
            semesters = models.Semester.query.order_by(
                sqlalchemy.desc('end')).all(),
            section_kinds = models.Section.kinds
    )

@app.route('/schedule/ical/')
@set_renderers(ICalendarRenderer)
def schedule_ical():
    return {'data': api.schedule_events(request.args.get('semester'))}

@app.route('/schedule/')
@set_renderers(HTMLRenderer, ICalendarRenderer)
def schedule():
    # Check the media type. If it is a calendar type, then return the iCalendar
    # file.
    print('here')
    print(request.headers)
    if ICalendarRenderer.media_type in request.headers['Accept'].split(','):
        return {'data': api.schedule_events(request.args.get('semester'))}
    else:
        return render_template('schedule.html')
