from makeSentences import make_sentences
import numpy as np
from misskey import Misskey
import json
#from discordWebhook import send


with open('../assets/config.json', 'r') as json_file:
    config = json.load(json_file)
misskey = Misskey(config['token']['server'], i= config['token']['i'])



def note():
    # 10%の確率で「にゃんぱすー」を呟く
    if np.random.randint(1,91) == 1:
        nyanpass_status = misskey.notes_create("にゃんぱすー")
#        send(nyanpass_status)
    sentence_1,sentence_2 = make_sentences()
    tweet_result_1 = misskey.notes_create(sentence_1)
    tweet_result_2 = misskey.notes_create(sentence_2)
#    send(tweet_result_1)
#    send(tweet_result_2)

