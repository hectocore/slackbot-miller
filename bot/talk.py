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
def default_hanlder(message):
    sleep(1)
    answers = ('Repeat last.', 'Say again.', 'Repeat last, over.', 'Say again, over.', 'Repeat, soldier.', 'Say again, soldier.', 'Poor transmission, say again.', 'What on earth are you talking about, soldier?', 'Question time\'s over.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='default_reply', message=message, answer=answer)
    message.reply(answer)

@respond_to(r'(?:\W|^)(hey|hi|hello|good morning|good afternoon|good evening|salut|salutation[s]{0,1}|coucou|bonjour|bonsoir)(?:\W|$)', re.IGNORECASE)
def talk_hello_reply(*message):
    sleep(1)
    answers = ('Good to see you.', 'Glad to see you\'re still alive.', 'I thought you were dead.', 'It\'s good to hear from you.', 'Ah, soldier. You certainly do have the tendency to show up unexpectedly', 'There you are, soldier!')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(goodbye|good night|byebye|bye|see you|cheers|have a nice day|au revoir|[aà]{1} plus|[aà]{1}\+|\+\+|[aà]{1} bientôt|[aà]{1} la prochaine|[aà]{1} la revoyure|allez[,]{0,1} salut|bon[,]{0,1} salut|bonne nuit|adieu|ciao|tchao|me tire|m\'en vais|s\'en va)(?:\W|$)', re.IGNORECASE)
def talk_goodbye_reply(*message):
    sleep(1)
    answers = ('See you soon.', 'Roger, out.', 'Goodbye.', 'Try to still alive.', 'Copy. See you soon.', 'Understood. Good luck. out.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(thank you|thanks|thk[s]{0,1}|thx[s]{0,1}|ty|merci|remercie)(?:\W|$)', re.IGNORECASE)
def talk_thanks_reply(*message):
    sleep(1)
    answers = ('Glad to help you.', 'You\'re welcome.', 'The pleasure is mine.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Are you ok|How are you|How\'re you|Comment vas[\s-]{1}tu|Comment allez[\s-]{1}vous|[ÇC]a va|Tu vas bien|Vous allez bien)[\s]{0,1}\?(?:\W|$)', re.IGNORECASE)
def talk_howreyou_reply(*message):
    sleep(1)
    answers = ('I\'m still alive.', 'Everything good.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(I love you|je t\'aime(?!\spas))(?:\W|$)', re.IGNORECASE)
def talk_loveyou_reply(*message):
    sleep(1)
    answers = ('Good to hear, soldier.', 'I like you, soldier.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Permission to speak|Permission to talk|Autorisation de parler|Autorisation à parler)(?:\W|$)', re.IGNORECASE)
def talk_permission_reply(*message):
    sleep(1)
    answers = ('Granted.', 'Yes soldier, go ahead.', 'Yes, go ahead.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Respectfully|Respectueusement|Sauf votre respect)(?:\W|$)', re.IGNORECASE)
def talk_disrespect_reply(*message):
    sleep(1)
    answers = ('Saying \'respectfully\', soldier, and proceeding to be disrespectful somewhat defeats the purpose, don\'t you think?', )
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(I hate you|I didn\'t like you|je t\'aime pas|je te déteste|je te hais)(?:\W|$)', re.IGNORECASE)
def talk_hateyou_reply(*message):
    sleep(1)
    answers = ('Keep your thoughts to yourself, soldier.', 'I don\'t care about your feelings, soldier.', 'Things are about to get ugly.', )
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(bastard[s]{0,1}|puss[yies]{1,3}|dick[s]{0,1}|ass[es]{0,2}|shut up|fuck[a-z]{0,3}|bi[a]{0,1}tch[a-z]{0,2}|shit|cul[s]{0,1}|bite[s]{0,1}|anus|con[s]{0,1}|conne[s]{0,1}|connard[s]{0,1}|connasse[s]{0,1}|bolosse[s]{0,1}|salaud[s]{0,1}|salope[s]{0,1}|encul[a-zé]{1,3}|niqu[éerzs]{1,3}|bais[a-zé]{1,3}|chi[eérs]{1,3}|chiant[s]{0,1}|pute[s]{0,1}|batard[a-z]{0,2}|gueule[s]{0,1}|pd|tg|ftg|fdp|ptn|ntm|putain[s]{0,1}|couille[s]{0,1}|merd[a-zé]{1,2})(?:\W|$)', re.IGNORECASE)
def talk_dirty_reply(*message):
    sleep(1)
    answers = ('Don\'t talk that way, soldier. That\'s an order!', 'Watch your language, soldier!', 'Soldier, I swear, once more and I\'ll drop you where you stand.', 'You\'d do well to refrain from threatening me.', 'You\'re doing it again, soldier.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(what time|quelle heure)(?:\W|$)', re.IGNORECASE)
def talk_whattime_reply(*message):
    sleep(1)
    answers = ('It\'s actually {0:02d}:{1:02d}, out.'.format(datetime.now().hour, datetime.now().minute), '{0:02d}:{1:02d}, out.'.format(datetime.now().hour, datetime.now().minute),)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(Who are you|Who\'re you|T\'es qui|Tu es qui|Vous êtes qui|Qui es[\s-]{1}tu|Qui êtes[\s-]{1}vous)[\s]{0,1}\?(?:\W|$)', re.IGNORECASE)
def talk_whoreyou_reply(*message):
    sleep(1)
    answers = ('I\'m Captain Scott Miller.','I\'m Captain Scott Miller, leader of the CTRG Group 14.', 'I\'m Captain Scott F. Miller, Born in UK in 1992 and member of NATO SF.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(problem[s]{0,1}|disturb[seding]{0,3}|bother[seding]{0,3}|énerv[a-zé]{1,3}|emp[eê]{1}ch[a-zé]{1,3}|emb[eê]{1}t[a-zé]{1,3}|dérang[a-zé]{1,3}|aga[cç]{1}[a-zé]{1,3}|problème[s]{0,1})(?:\W|$)', re.IGNORECASE)
def talk_problem_reply(*message):
    sleep(1)
    answers = ('It\'s not my business.', 'It\'s your problem.', 'That\'s your business, not mine.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)([a\'is]{1,2} bad|nasty|méchant[s]{0,1}|mauvais|pas sympa[s]{0,1}|pas gentil[sle]{0,3})(?:\W|$)', re.IGNORECASE)
def talk_complaint_reply(*message):
    sleep(1)
    answers = ('That\'s your opinion.', 'Perfection doesn\'t exist in this world.', 'I disagree.', 'Sorry, but I do not agree with you.', 'I agree.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:\W|^)(feel[ing]{0,3} bad|sad|melancholic|[\'a]{1}m crying|I cry|suis [trop]{0,4}[\s]{0,1}triste|je pleure|de pleurer|me sens [trop]{0,4}[\s]{0,1}mal)(?:\W|$)', re.IGNORECASE)
def talk_feelbad_reply(*message):
    sleep(1)
    answers = ('Don\'t give up!', 'It will be fine.', 'Things will get better.', 'You did what you could.', 'I know things don\'t look good for us right now. We took a hit. We lost a number of good men.',)
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)

@respond_to(r'(?:^)([\s]{0,1}\?|Scott[\s]{0,1}\?|Miller[\s]{0,1}\?|Scott Miller[\s]{0,1}\?|Captain[\s]{0,1}\?)(?:$)', re.IGNORECASE)
def talk_question_reply(*message):
    sleep(1)
    answers = ('Go ahead.', 'Yes soldier, go ahead.', 'Yes, go ahead.', 'Yes soldier?', 'Any questions?', 'Come in.', 'Receiving you, soldier. Go ahead. Over.')
    answer = answers[randrange(0, len(answers))]
    debug_bot(functype='respond_to', message=message[0], answer=answer)
    message[0].reply(answer)
