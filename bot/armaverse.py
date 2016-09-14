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

@respond_to(r'(?:\W|^)(SITREP|Report in|Respond)(?:\W|$)', re.IGNORECASE)
def arma_sitrep_reply(*message):
    sleep(1)
    answers = ('Grid {0:06d}'.format(randrange(0, 999999)),)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Scott Miller|Falcon|Keystone)(?:\W|$)', re.IGNORECASE)
def arma_callsign_reply(*message):
    sleep(1)
    answers = ('Go ahead, over.', 'Ready to copy, over.', 'Come in, over.', 'Send, over.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Medevac)(?:\W|$)', re.IGNORECASE)
def arma_medevac_reply(*message):
    sleep(1)
    answers = ('Medevac? With respect, soldier, it\'s not like we\'ve got a helo on standby here.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Reinforcements|Renforts)(?:\W|$)', re.IGNORECASE)
def arma_reinforcements_reply(*message):
    sleep(1)
    answers = ('Reinforcements are inbound.', 'Charlie\'s inbound with support for your wounded. Entrench your positions. Falcon out.', 'All right, the best we can do is divert an element from Delta.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Contact[s]{0,1}|Enem[yies]{1,3}|Under fire)(?:\W|$)', re.IGNORECASE)
def arma_contact_reply(*message):
    sleep(1)
    answers = ('Open fire!', 'Engage at will!', 'Fire at will!', 'Weapons free!',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Syndikat[s]{0,1}|Putain[s]{0,1} de fant[ôo]{1}me[s]{0,1}|Solomon Maru)(?:\W|$)', re.IGNORECASE)
def arma_syndikat_reply(*message):
    sleep(1)
    answers = ('Please don\'t talk about those fucking Syndikats...', 'I spent enough time with those guys to tell you I do not like them.', 'You remember me bad moments.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(CSAT|Griffin|Canton Protocol|Iran|Iranian[s]{0,1}|China|Chinese|Iranien[s]{0,1}|Chine|Chinois)(?:\W|$)', re.IGNORECASE)
def arma_syndikat_reply(*message):
    sleep(1)
    answers = ('Don\'t joke about CSAT. Those guys are not kinding.', 'Actually, CSAT forces are better equiped than ours.', 'CSAT soldiers are extremly well trained.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(CSAT|Griffin|Canton Protocol|Iran|Iranian[s]{0,1}|China|Chinese|Iranien[s]{0,1}|Chine|Chinois)(?:\W|$)', re.IGNORECASE)
def arma_syndikat_reply(*message):
    sleep(1)
    answers = ('Don\'t joke about CSAT. Those guys are not kinding.', 'Did you know CSAT forces are better equiped than ours?', 'I can tell you that CSAT soldiers are extremly well trained.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(CTRG|Viper[s]{0,1}|Vent d\'Est|East[\s]{0,1}Wind|Apex Protocol)(?:\W|$)', re.IGNORECASE)
def arma_confidential_reply(*message):
    sleep(1)
    answers = ('That\'s classified.', 'You\'re not supposed to talk about it.', 'This information is classified!')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)
