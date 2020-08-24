#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Версия движка: Alpha 1

#Engine Bot Vk - Это бесплатный движок для создания простых Vk ботов, с минимальным использованием
#знаний в программирование. Сам движок сделан на Python 3.8

#Создатель движка: Гарик Сукиасян: vk.com/id575200203

#Группа vk: vk.com/bot_engin_e

#Беседа vk: vk.cc/axO9hD

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from config import *
from tqdm import tqdm

import vk_api
import random
import json
import requests

import time

mylist = [1,2,3,4,5,6,7,8,9,10]

for i in tqdm(mylist):
    time.sleep(0.3)
    vk = vk_api.VkApi(token=connect[0]["Token"])

    vk._auth_token()

    vk.get_api()

    longpoll = VkBotLongPoll(vk, connect[0]["grop_id"])

def write_msg(peer_id, message):
   vk.method("messages.send", {"peer_id": peer_id, "message": message, "random_id": 0})

print("Бот запущен")
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id != event.object.from_id and connect[0]["Bot_chat"] == "True":
                    cmd = event.object.text.lower()

                    if cmd in mybot[0]["vopros1"]:
                        sim1 = len(mybot[0]["otvet-1"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach1"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-1"][x1], "attachment": mybot[0]["attach1"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros2"]:
                        sim1 = len(mybot[0]["otvet-2"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach2"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-2"][x1], "attachment": mybot[0]["attach2"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros3"]:
                        sim1 = len(mybot[0]["otvet-3"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach3"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-3"][x1], "attachment": mybot[0]["attach3"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros4"]:
                        sim1 = len(mybot[0]["otvet-4"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach4"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-4"][x1], "attachment": mybot[0]["attach4"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros5"]:
                        sim1 = len(mybot[0]["otvet-5"])
                        x = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach5"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-5"][x1], "attachment": mybot[0]["attach5"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros6"]:
                        sim1 = len(mybot[0]["otvet-6"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach6"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-6"][x1], "attachment": mybot[0]["attach6"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros7"]:
                        sim1 = len(mybot[0]["otvet-7"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach7"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-7"][x1], "attachment": mybot[0]["attach7"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros8"]:
                        sim1 = len(mybot[0]["otvet-8"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach8"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-8"][x1], "attachment": mybot[0]["attach8"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros9"]:
                        sim1 = len(mybot[0]["otvet-9"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach9"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-9"][x1], "attachment": mybot[0]["attach9"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros10"]:
                        sim1 = len(mybot[0]["otvet-10"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach10"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-10"][x1], "attachment": mybot[0]["attach10"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros11"]:
                        sim1 = len(mybot[0]["otvet-11"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach11"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-11"][x1], "attachment": mybot[0]["attach11"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros12"]:
                        sim1 = len(mybot[0]["otvet-12"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach12"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-12"][x1], "attachment": mybot[0]["attach12"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros13"]:
                        sim1 = len(mybot[0]["otvet-13"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach13"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-13"][x1], "attachment": mybot[0]["attach13"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros14"]:
                        sim1 = len(mybot[0]["otvet-14"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach14"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-14"][x1], "attachment": mybot[0]["attach14"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros15"]:
                        sim1 = len(mybot[0]["otvet-15"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach15"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-15"][x1], "attachment": mybot[0]["attach15"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros16"]:
                        sim1 = len(mybot[0]["otvet-16"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach16"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-16"][x1], "attachment": mybot[0]["attach16"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros17"]:
                        sim1 = len(mybot[0]["otvet-17"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach17"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-17"][x1], "attachment": mybot[0]["attach17"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros18"]:
                        sim1 = len(mybot[0]["otvet-18"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach18"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-18"][x1], "attachment": mybot[0]["attach18"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros19"]:
                        sim1 = len(mybot[0]["otvet-19"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach19"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-19"][x1], "attachment": mybot[0]["attach19"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros20"]:
                        sim1 = len(mybot[0]["otvet-20"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach20"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-20"][x1], "attachment": mybot[0]["attach20"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros21"]:
                        sim1 = len(mybot[0]["otvet-21"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach21"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-21"][x1], "attachment": mybot[0]["attach21"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros22"]:
                        sim1 = len(mybot[0]["otvet-22"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach22"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-22"][x1], "attachment": mybot[0]["attach22"][x2], "random_id": 0})

                    elif cmd == "dev":
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "vk.com/id575200203", "random_id": 0})

                    elif cmd in mybot[0]["vopros23"]:
                        sim1 = len(mybot[0]["otvet-23"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach23"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-23"][x1], "attachment": mybot[0]["attach23"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros24"]:
                        sim1 = len(mybot[0]["otvet-24"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach24"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-24"][x1], "attachment": mybot[0]["attach24"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros25"]:
                        sim1 = len(mybot[0]["otvet-25"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach25"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-25"][x1], "attachment": mybot[0]["attach25"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros26"]:
                        sim1 = len(mybot[0]["otvet-26"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach26"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-26"][x1], "attachment": mybot[0]["attach26"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros27"]:
                        sim1 = len(mybot[0]["otvet-27"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach27"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-27"][x1], "attachment": mybot[0]["attach27"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros28"]:
                        sim1 = len(mybot[0]["otvet-28"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach28"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-28"][x1], "attachment": mybot[0]["attach28"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros29"]:
                        sim1 = len(mybot[0]["otvet-29"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach29"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-29"][x1], "attachment": mybot[0]["attach29"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros30"]:
                        sim1 = len(mybot[0]["otvet-30"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach30"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": mybot[0]["otvet-30"][x1], "attachment": mybot[0]["attach30"][x2], "random_id": 0})

                elif event.object.peer_id == event.object.from_id and connect[0]["Bot_chat"] == "False":
                    cmd = event.object.text.lower()

                    if cmd in mybot[0]["vopros1"]:
                        sim1 = len(mybot[0]["otvet-1"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-1"][x1], "attachment": mybot[0]["attach1"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros2"]:
                        sim1 = len(mybot[0]["otvet-2"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach2"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-2"][x1], "attachment": mybot[0]["attach2"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros3"]:
                        sim1 = len(mybot[0]["otvet-3"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach3"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-3"][x1], "attachment": mybot[0]["attach3"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros4"]:
                        sim1 = len(mybot[0]["otvet-4"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach4"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-4"][x1], "attachment": mybot[0]["attach4"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros5"]:
                        sim1 = len(mybot[0]["otvet-5"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach5"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-5"][x1], "attachment": mybot[0]["attach5"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros6"]:
                        sim1 = len(mybot[0]["otvet-6"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach6"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-6"][x1], "attachment": mybot[0]["attach6"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros7"]:
                        sim1 = len(mybot[0]["otvet-7"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach7"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-7"][x1], "attachment": mybot[0]["attach7"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros8"]:
                        sim1 = len(mybot[0]["otvet-8"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach8"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-8"][x1], "attachment": mybot[0]["attach8"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros9"]:
                        sim1 = len(mybot[0]["otvet-9"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach9"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-9"][x1], "attachment": mybot[0]["attach9"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros10"]:
                        sim1 = len(mybot[0]["otvet-10"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach10"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-10"][x1], "attachment": mybot[0]["attach10"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros11"]:
                        sim1 = len(mybot[0]["otvet-11"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach11"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-11"][x1], "attachment": mybot[0]["attach11"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros12"]:
                        sim1 = len(mybot[0]["otvet-12"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach12"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-12"][x1], "attachment": mybot[0]["attach12"][x2], "random_id": 0})

                    elif cmd == "dev":
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": "vk.com/id575200203", "random_id": 0})

                    elif cmd in mybot[0]["vopros13"]:
                        sim1 = len(mybot[0]["otvet-13"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach13"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-13"][x1], "attachment": mybot[0]["attach13"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros14"]:
                        sim1 = len(mybot[0]["otvet-14"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach14"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-14"][x1], "attachment": mybot[0]["attach14"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros15"]:
                        sim1 = len(mybot[0]["otvet-15"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach15"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-15"][x1], "attachment": mybot[0]["attach15"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros16"]:
                        sim1 = len(mybot[0]["otvet-16"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach16"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-16"][x1], "attachment": mybot[0]["attach16"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros17"]:
                        sim1 = len(mybot[0]["otvet-17"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach17"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-17"][x1], "attachment": mybot[0]["attach17"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros18"]:
                        sim1 = len(mybot[0]["otvet-18"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach18"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-18"][x1], "attachment": mybot[0]["attach18"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros19"]:
                        sim1 = len(mybot[0]["otvet-19"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach19"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-19"][x1], "attachment": mybot[0]["attach19"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros20"]:
                        sim1 = len(mybot[0]["otvet-20"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach20"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-20"][x1], "attachment": mybot[0]["attach20"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros21"]:
                        sim1 = len(mybot[0]["otvet-21"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach21"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-21"][x1], "attachment": mybot[0]["attach21"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros22"]:
                        sim1 = len(mybot[0]["otvet-22"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach22"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-22"][x1], "attachment": mybot[0]["attach22"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros23"]:
                        sim1 = len(mybot[0]["otvet-23"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach23"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-23"][x1], "attachment": mybot[0]["attach23"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros24"]:
                        sim1 = len(mybot[0]["otvet-24"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach24"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-24"][x1], "attachment": mybot[0]["attach24"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros25"]:
                        sim1 = len(mybot[0]["otvet-25"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach25"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-25"][x1], "attachment": mybot[0]["attach25"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros26"]:
                        sim1 = len(mybot[0]["otvet-26"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach26"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-26"][x1], "attachment": mybot[0]["attach26"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros27"]:
                        sim1 = len(mybot[0]["otvet-27"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach27"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-27"][x1], "attachment": mybot[0]["attach27"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros28"]:
                        sim1 = len(mybot[0]["otvet-28"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach28"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-28"][x1], "attachment": mybot[0]["attach28"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros29"]:
                        sim1 = len(mybot[0]["otvet-29"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach29"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-29"][x1], "attachment": mybot[0]["attach29"][x2], "random_id": 0})

                    elif cmd in mybot[0]["vopros30"]:
                        sim1 = len(mybot[0]["otvet-30"])
                        x1 = random.randint(0, sim1 - 1)
                        sim2 = len(mybot[0]["attach30"])
                        x2 = random.randint(0, sim2 - 1)
                        vk.method("messages.send", {"peer_id": event.object.from_id, "message": mybot[0]["otvet-30"][x1], "attachment": mybot[0]["attach30"][x2], "random_id": 0})
    except:
        pass
