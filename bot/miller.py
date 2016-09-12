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

@default_reply
def my_default_hanlder(message):
    sleep(1)
    answers = ('Repeat last, over.', 'Say again, over.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='default_reply', message=message, answer=answer)
    message.reply(answer)

@respond_to(r'(?:\W|^)(hey|hi|hello|good morning|good afternoon|good evening|salut|salutation[s]{0,1}|coucou|bonjour|bonsoir)(?:\W|$)', re.IGNORECASE)
def hello_reply(*message):
    sleep(1)
    answers = ('Good to see you.', 'Glad to see you\'re still alive.', 'I thought you were dead.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(goodbye|good night|byebye|bye|see you|cheers|have a nice day|au revoir|[aà]{1} plus|[aà]{1}\+|\+\+|[aà]{1} bientôt|[aà]{1} la prochaine|[aà]{1} la revoyure|allez[,]{0,1} salut|bon[,]{0,1} salut|bonne nuit|adieu|ciao|tchao|me tire)(?:\W|$)', re.IGNORECASE)
def goodbye_reply(*message):
    sleep(1)
    answers = ('See you soon.', 'Roger, out.', 'Goodbye.', 'Try to still alive.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(thank you|thanks|thk[s]{0,1}|thx[s]{0,1}|ty|merci|remercie)(?:\W|$)', re.IGNORECASE)
def thanks_reply(*message):
    sleep(1)
    answers = ('Glad to help you.', 'You\'re welcome.', 'The pleasure is mine.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Are you ok|How are you|How\'re you|Comment vas[\s-]{1}tu|Comment allez[\s-]{1}vous|[ÇC]a va|Tu vas bien|Vous allez bien)[\s]{0,1}\?(?:\W|$)', re.IGNORECASE)
def howreyou_reply(*message):
    sleep(1)
    answers = ('I\'m still alive.', 'Everything good.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Who are you|Who\'re you|T\'es qui|Tu es qui|Vous êtes qui|Qui es[\s-]{1}tu|Qui êtes[\s-]{1}vous)[\s]{0,1}\?(?:\W|$)', re.IGNORECASE)
def whoreyou_reply(*message):
    sleep(1)
    answers = ('I\'m Captain Scott Miller.','I\'m Captain Scott Miller, leader of the CTRG Group 14.', 'I\'m Captain Scott F. Miller, Born in UK in 1992 and member of NATO SF.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(problem[s]{0,1}|disturb[seding]{0,3}|bother[seding]{0,3}|énerv[a-zé]{1,3}|emp[eê]{1}ch[a-zé]{1,3}|emb[eê]{1}t[a-zé]{1,3}|dérang[a-zé]{1,3}|aga[cç]{1}[a-zé]{1,3}|problème[s]{0,1})(?:\W|$)', re.IGNORECASE)
def problem_reply(*message):
    sleep(1)
    answers = ('It\'s not my business.', 'It\'s your problem.', 'That\'s your business, not mine.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)([a\'is]{1,2} bad|nasty|méchant[s]{0,1}|mauvais|pas sympa[s]{0,1}|pas gentil[sle]{0,3})(?:\W|$)', re.IGNORECASE)
def complaint_reply(*message):
    sleep(1)
    answers = ('That\'s your opinion.', 'Perfection doesn\'t exist in this world.', 'I disagree.', 'Sorry, but I do not agree with you.', 'I agree.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(feel[ing]{0,3} bad|sad|melancholic|[\'a]{1}m crying|I cry|suis [trop]{0,4}[\s]{0,1}triste|je pleure|de pleurer|me sens [trop]{0,4}[\s]{0,1}mal)(?:\W|$)', re.IGNORECASE)
def feelbad_reply(*message):
    sleep(1)
    answers = ('Don\'t give up!', 'It will be fine.', 'Things will get better.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(SITREP)(?:\W|$)', re.IGNORECASE)
def sitrep_reply(*message):
    sleep(1)
    answers = ('Grid {0:06d}'.format(randrange(0, 999999)),)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(quelle heure|what time)(?:\W|$)', re.IGNORECASE)
def time_reply(*message):
    sleep(1)
    answers = ('It\'s actually {0:02d}:{1:02d}, out.'.format(datetime.now().hour, datetime.now().minute), '{0:02d}:{1:02d}, out.'.format(datetime.now().hour, datetime.now().minute),)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

# @respond_to(r'(?:\W|^)(why|what|when|where|who|whose|how|quoi|qui|où|quand|comment|combien|quel[les]{0,3})(?:\W|$)', re.IGNORECASE)
# def question_reply(*message):
#     sleep(1)
#     answers = ('Question time\'s over!', 'No time for questions.')
#     answer = answers[randrange(0, len(answers))]
#     debug_bot(functype='respond_to', message=message[0], answer=answer)
#     message[0].reply(answer)

@respond_to(r'(?:\W|^)(Scott Miller|Falcon|Keystone)(?:\W|$)', re.IGNORECASE)
def callsign_reply(*message):
    sleep(1)
    answers = ('Go ahead, over.', 'Ready to copy, over.', 'Come in, over.', 'Send, over.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:^)([\s]{0,1}\?|Scott[\s]{0,1}\?|Miller[\s]{0,1}\?)(?:$)', re.IGNORECASE)
def question_reply(*message):
    sleep(1)
    answers = ('Go ahead.', 'Yes soldier, go ahead.', 'Yes, go ahead.', 'Yes soldier?')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@listen_to(r'(?:\W|^)(Syndikat[s]{0,1}|Putain[s]{0,1} de fantôme[s]{0,1}|Solomon Maru)(?:\W|$)', re.IGNORECASE)
def syndikat_send(*message):
    sleep(1)
    answers = ('Please don\'t talk about those fucking Syndikats...', 'I spent enough time with those guys to tell you I do not like them.', 'You remember me bad moments.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='listen_to', message=message[0], answer=answer)
    message[0].send(answer)

@listen_to(r'(?:\W|^)(bastard[s]{0,1}|dick[s]{0,1}|ass[es]{0,2}|shut up|fuck[a-z]{0,3}|bi[a]{0,1}tch[a-z]{0,2}|shit|cul[s]{0,1}|bite[s]{0,1}|anus|con[s]{0,1}|conne[s]{0,1}|connard[s]{0,1}|connasse[s]{0,1}|bolosse[s]{0,1}|salaud[s]{0,1}|salope[s]{0,1}|encul[a-zé]{1,3}|niqu[a-zé]{1,3}|bais[a-zé]{1,3}|chi[eérs]{1,3}|chiant[s]{0,1}|pute[s]{0,1}|batard[a-z]{0,2}|gueule[s]{0,1}|pd|tg|ftg|fdp|ptn|ntm|putain[s]{0,1}|couille[s]{0,1}|merd[a-zé]{1,2})(?:\W|$)', re.IGNORECASE)
def disrepect_send(*message):
    reactions = ('rage',)
    reaction = reactions[randrange(0, len(reactions))]
    debug_bot(functype='listen_to react', message=message[0], answer=reaction)
    message[0].react(reaction)
    # sleep(1)
    # answers = ('Don\'t talk that way, soldier!', 'Watch your language, soldier!', 'Watch your mouth!', 'Watch your tongue!')
    # answer = answers[randrange(0, len(answers))]
    # debug_bot(functype='listen_to', message=message[0], answer=answer)
    # message[0].send(answer)

@listen_to(r'(?:\W|^)(CTRG|Viper[s]{0,1}|Vent d\'Est|East[\s]{0,1}Wind|Apex Protocol)(?:\W|$)', re.IGNORECASE)
def confidential_send(*message):
    sleep(1)
    answers = ('You\'re not supposed to talk about it.', 'This information is classified!')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='listen_to', message=message[0], answer=answer)
    message[0].send(answer)

@listen_to(r'(?:\W|^)(man down|is hit|is down|dead|die|crev[a-z]{1,2}|mort|décédé|décès)(?:\W|$)', re.IGNORECASE)
def dead_send(*message):
    reactions = ('skull_and_crossbones',)
    reaction = reactions[randrange(0, len(reactions))]
    debug_bot(functype='listen_to react', message=message[0], answer=reaction)
    message[0].react(reaction)
    sleep(1)
    answers = ('Man down!', 'We lost one!', 'He\'s hit!', 'Fuck, man down!')
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
