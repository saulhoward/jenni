#!/usr/bin/env python
# coding=utf-8
"""
cruft.py - Phenny Cruft Module
http://inamidst.com/phenny/
"""
#import os
import subprocess, random
from datetime import datetime

def chins(phenny, input):
    process = subprocess.Popen(
            #'/opt/vdna/trunk/scripts/cassandra/status',
            '/home/saul/bin/cassandraStatus.sh',
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
            )
    output = process.communicate()
    phenny.say(str(output).replace('\\n', '|'))
    phenny.say("Done.")
chins.commands = ['chins']
chins.priority = 'medium'

# def hello(phenny, input):
    # phenny.say('Hello ' + input.nick + '.')
# hello.rule = r'(?i)(hello|good morning|yo|wassup|hi) cruftBot'
# hello.priority = 'medium'

def sorryOksana(phenny, input):
    phenny.say("Sorry Oksana.")
sorryOksana.rule = r'\b(?i)(fuck|shit|balls|bollocks|bastard|bitch|bloody|cunt|ballbag|crap)\b'
sorryOksana.priority = 'medium'

def cruftDetected(phenny, input):
    if (random.random() > 0.5) :
        randmsg = random.choice(["You called?", "Warning: cruft detected in this channel."])
        phenny.say(randmsg)
cruftDetected.rule = r'\b(?i)(cruft)(?!Bot)\b'
cruftDetected.priority = 'medium'

def beerOClock(phenny, input):
    hour   = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    if (hour == '17' and (minute >= '30' or minute <= '35')) :
        phenny.say("Beer O'Clock!")
beerOClock.rule = r'.*'
beerOClock.priority = 'low'
