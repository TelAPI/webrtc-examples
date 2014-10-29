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
def dialer():
    """ Dialer view
    """
    nickname = str(uuid4())
    js_creds = account.applications[app_sid].client_token.create(nickname=nickname)
    return render_template("dialer.html", token=js_creds.sid, password=js_creds.client_password)


@app.route("/xml", methods=['GET', 'POST'])
def xml():
    """ InboundXML for dialing a dynamic number
    """
    number = request.form.get('WebClientParam_number')
    xml = inboundxml.Response(inboundxml.Dial(
        inboundxml.Number(
            str(number), 
        )
    ))
    return Response(str(xml), mimetype='text/xml')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
