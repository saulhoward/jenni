#!/usr/bin/env python
# coding=utf-8
"""
cruft.py - Phenny Cruft Module
http://inamidst.com/phenny/
"""
#import os
import subprocess, random 

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
sorryOksana.rule = r'.*(?i)(fuck|shit|balls|bollocks|bastard|bitch|bloody|cunt|ballbag|crap).*'
sorryOksana.priority = 'medium'

def cruftDetected(phenny, input):
    randmsg = random.choice(["You called?", "Cruft, you say?"])
    phenny.say(randmsg)
cruftDetected.rule = r'.*(?i)(cruft).*'
cruftDetected.priority = 'medium'
