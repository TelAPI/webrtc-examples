#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telapi import rest, inboundxml
from flask import Flask, render_template, request, Response
from uuid import uuid4



app = Flask(__name__)


# Config data
account_sid = '[account_sid]'
auth_token  = '[auth_token]'
app_sid = '[app_sid]'


client      = rest.Client(account_sid=account_sid, auth_token=auth_token)
account     = client.accounts[client.account_sid]


@app.route('/')
def home():
    """ Just home view for creating new conference
    """
    conference_name = str(uuid4())
    return render_template("home.html", conference_name=conference_name)


@app.route("/<conference_name>")
def conference(conference_name):
    """ View for joining a conference
    """
    nickname = str(uuid4())
    js_creds = account.applications[app_sid].client_token.create(nickname=nickname)
    return render_template("conference.html", token=js_creds.sid, password=js_creds.client_password, conference_name=conference_name)


@app.route("/xml", methods=['GET', 'POST'])
def xml():
    """ InboundXML for dialing a conference with dynamic conferece name
    """
    conference_name = request.form.get('WebClientParam_conference_name')
    xml = inboundxml.Response(inboundxml.Dial(
        inboundxml.Conference(
            str(conference_name), 
        )
    ))
    return Response(str(xml), mimetype='text/xml')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
