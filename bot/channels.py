# -*-coding:utf-8 -*
import re
from time import sleep
from random import randrange
from datetime import datetime
import pickle
from slackbot.bot import default_reply
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from debugbot import debug_bot

@listen_to(r'(?:\W|^)(bastard[s]{0,1}|puss[yies]{1,3}|dick[s]{0,1}|ass[es]{0,2}|shut up|fuck[a-z]{0,3}|bi[a]{0,1}tch[a-z]{0,2}|shit|cul[s]{0,1}|bite[s]{0,1}|anus|con[s]{0,1}|conne[s]{0,1}|connard[s]{0,1}|connasse[s]{0,1}|bolosse[s]{0,1}|salaud[s]{0,1}|salope[s]{0,1}|encul[a-zé]{1,3}|niqu[éerzs]{1,3}|bais[a-zé]{1,3}|chi[eérs]{1,3}|chiant[s]{0,1}|pute[s]{0,1}|batard[a-z]{0,2}|gueule[s]{0,1}|pd|tg|ftg|fdp|ptn|ntm|putain[s]{0,1}|couille[s]{0,1}|merd[a-zé]{1,2}|ta m[eè]{1}re|vos m[eè]{1}res)(?:\W|$)', re.IGNORECASE)
def disrepect_send(*message):
    reactions = ('rage',)
    reaction = reactions[randrange(0, len(reactions))]
    debug_bot(functype='listen_to react', message=message[0], answer=reaction)
    message[0].react(reaction)

@listen_to(r'(?:\W|^)(man down|he\'s hit|he\'s down|he\'s dead|is hit|is down|is dead|est mort|est décédé|homme à terre|est à terre)(?:\W|$)', re.IGNORECASE)
def dead_send(*message):
    reactions = ('skull_and_crossbones',)
    reaction = reactions[randrange(0, len(reactions))]
    debug_bot(functype='listen_to react', message=message[0], answer=reaction)
    message[0].react(reaction)
    sleep(1)
    answers = ('Man down!', 'We lost one!', 'He\'s hit!','Fuck, man down!')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='listen_to', message=message[0], answer=answer)
    message[0].send(answer)

@listen_to(r'(?:\W|^)(Scott Miller)(?:\W|$)', re.IGNORECASE)
def scottmiller_send(*message):
    sleep(1)
    answers = ('This is Captain Scott Miller, Royal Navy. Next time, avoid broadcasting over the whole net, soldier.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='listen_to', message=message[0], answer=answer)
    message[0].send(answer)

@listen_to(r'(?:\W|^)(John Miller|Scott Kerry|Millah)(?:\W|$)', re.IGNORECASE)
def johnmiller_send(*message):
    reactions = ('unamused',)
    reaction = reactions[randrange(0, len(reactions))]
    debug_bot(functype='listen_to react', message=message[0], answer=reaction)
    message[0].react(reaction)
