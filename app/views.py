from app import app
from app import EventTypes
import flask
import json
from app import events
from flask import Flask, request, Response, render_template

@app.route('/')
@app.route('/index')
def index():
	machines = ["MSALPRASHANTH"]

	return render_template("index.html",
        servers = machines)


@app.route('/eventtypes/<server>')
def eventtypes(server):
    # show the user profile for that user
    return json.dumps(EventTypes.getEventTypes(server))


@app.route('/logs/<server>/<eventtype>/<search>')
def logs(server, eventtype, search):
	#return server + eventtype + search
	return Response(events.getEvents(server, eventtype, search),mimetype='text/event-stream')


    