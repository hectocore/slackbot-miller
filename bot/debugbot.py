#coding: UTF-8
from datetime import datetime

def debug_bot(functype, message, answer):
    COLORS_CODE = {
        'gray':'\033[90m',
        'red':'\033[91m',
        'green':'\033[92m',
        'yellow':'\033[93m',
        'blue':'\033[94m',
        'magenta':'\033[95m',
        'cyan':'\033[96m',
        'white':'\033[97m',
        'reset':'\033[0m'
    }


    print('{defcolor}\nFunction {function} triggered at {hour:02d}:{minutes:02d}\'{seconds:02d}:{errcolor}'.format(
        function=functype,
        hour=datetime.now().hour,
        minutes=datetime.now().minute,
        seconds=datetime.now().second,
        defcolor=COLORS_CODE['reset'],
        errcolor=COLORS_CODE['red']))


    if functype == 'default_reply':
        print('  {warcolor}Received Unknow Message:{txtcolor} {text}{errcolor}'.format(
            text=message._body['text'],
            warcolor=COLORS_CODE['yellow'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
        print('  {dircolor}Direct Message:{txtcolor} {text}{errcolor}'.format(
            text=answer,
            dircolor=COLORS_CODE['green'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
    elif functype == 'default_reply react':
        print('  {warcolor}Received Unknow Message:{txtcolor} {text}{errcolor}'.format(
            text=message._body['text'],
            warcolor=COLORS_CODE['yellow'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
        print('  {dircolor}Direct React:{emocolor} {emoji}{errcolor}'.format(
            emoji=answer,
            dircolor=COLORS_CODE['green'],
            errcolor=COLORS_CODE['red'],
            emocolor=COLORS_CODE['blue']))

    elif functype == 'respond_to':
        print('  {rcvcolor}Received Message:{txtcolor} {text}{errcolor}'.format(
            text=message._body['text'],
            rcvcolor=COLORS_CODE['magenta'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
        print('  {dircolor}Direct Message:{txtcolor} {text}{errcolor}'.format(
            text=answer,
            dircolor=COLORS_CODE['green'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
    elif functype == 'respond_to react':
        print('  {rcvcolor}Received Message:{txtcolor} {text}{errcolor}'.format(
            text=message._body['text'],
            rcvcolor=COLORS_CODE['magenta'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
        print('  {dircolor}Direct React:{emocolor} {emoji}{errcolor}'.format(
            emoji=answer,
            dircolor=COLORS_CODE['green'],
            errcolor=COLORS_CODE['red'],
            emocolor=COLORS_CODE['blue']))

    elif functype == 'listen_to':
        print('  {rcvcolor}Channel Message:{txtcolor} {text}{errcolor}'.format(
            text=message._body['text'],
            rcvcolor=COLORS_CODE['magenta'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
        print('  {sndcolor}Send Message:{txtcolor} {text}{errcolor}'.format(
            text=answer,
            sndcolor=COLORS_CODE['cyan'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
    elif functype == 'listen_to react':
        print('  {rcvcolor}Channel Message:{txtcolor} {text}{errcolor}'.format(
            text=message._body['text'],
            rcvcolor=COLORS_CODE['magenta'],
            errcolor=COLORS_CODE['red'],
            txtcolor=COLORS_CODE['white']))
        print('  {sndcolor}Send React:{emocolor} {emoji}{errcolor}'.format(
            emoji=answer,
            sndcolor=COLORS_CODE['cyan'],
            errcolor=COLORS_CODE['red'],
            emocolor=COLORS_CODE['blue']))

    else:
        print('  {errcolor}Unknow function type.'.format(
            errcolor=COLORS_CODE['red']))
