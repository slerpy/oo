#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# texter.py
# --------------------
# program to send text messages
#
# @author Slerpy, 0x899319D4251502BA
# @date 25 June 2015
# @version 0.0.1
##############################################################################

from twilio.rest import TwilioRestClient

account_sid = "twilio.assigned sid"
auth_token = "twilio.assigned auth token"
client = TwilioRestClient (account_sid, auth_token)

message = client.sms.messages.create (
    body="HI! Did you get this???",
    to="phone number to text",
    from_="phone number assigned by twilio")

#print message.sid

    

