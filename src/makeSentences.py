import logging
import json
import MeCab
from filters import filter_words, filter_links
import numpy as np
import os
from misskey import Misskey

with open('../assets/config.json', 'r') as json_file:
    config = json.load(json_file)

print(config)

misskey = Misskey(config['token']['server'], i= config['token']['i'])

# MeCab
mecab = MeCab.Tagger(f"-Ochasen")

with open('../assets/templates.json', 'r') as json_file:
    templates = json.load(json_file)

text_list = []
def make_sentences():
    note = misskey.notes_timeline(limit=10)

    for number in note:
        note_data = number["text"]
        print(number["text"])
        text_list.append(note_data)
        
    # フィルター
    data = filter_links(text_list)
    for t in data:
        t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("?", "？").replace("!", "！").replace("，", "、").replace("．", "。") + ","

    # ツイートリストを出力
    logging.debug(data)

    # 名詞を格納するリスト
    nouns = []

    # 全ての文章から固有名詞だけを取り出す
    for tweet in data:
        t = tweet.replace(",", "")
        # 形態素出力
        logging.debug(mecab.parse(t))
        # 名詞を格納
        for n in [line for line in mecab.parse(t).splitlines() if "固有名詞" in line.split()[-1]]:
            noun = n.split("\t")[0]
            # 重複チェック
            if not noun in nouns:
                nouns.append(noun)

    # 名詞リストを出力
    logging.debug(nouns)

    # ランダムな名詞を選び、語幹 + 名詞 + 語尾 の形で文章を2つ生成する
    s_1 = np.random.choice(templates)
    s_2 = np.random.choice(templates)
    n_1 = filter_words(np.random.choice(nouns))
    n_2 = filter_words(np.random.choice(nouns))
    sentence_1 = s_1["gokan"] + n_1 + s_1["gobi"]
    sentence_2 = s_2["gokan"] + n_2 + s_2["gobi"]

    # 文章を出力
    logging.debug(sentence_1)
    logging.debug(sentence_2)

    # 文章を返す
    return sentence_1, sentence_2
