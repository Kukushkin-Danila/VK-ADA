
# -*- coding: utf-8 -*-
import random, time, vk, datetime

from Lessons.Chapter_1 import C1L1
from Lessons.Contents import Content, ContentP2, ContentP3, ContentP4
from Lessons.Chapter_2 import C2L1, C2L1_2
from Lessons.Help import HELP
from Lessons.Ym import Ym
from Lessons.Yr import Top, Mid, Mda


done = True
history = open('history.txt', 'w')
session = vk.Session(
    access_token="3e39f64310d6265db34707e865e2f1de96e90830611ad9a4c0169b239c72af62ed01250a0012a1b9d3c28")
api = vk.API(session)
sleep = 1.5

while done:
    sm = api.messages.get(count=10)
    time.sleep(sleep)
    a = []
    maxi = 0
    nui = {}

    for i in sm[1:]:
        try:
            if i['read_state'] == 0:
                a.append(i)
        except UnicodeEncodeError:
            api.messages.markAsRead(message_ids=i['mid'])
            time.sleep(sleep)
    for i in a:
        if i['date'] > maxi:
            maxi = i['date']
            nui = i

    print(nui)

    if str(datetime.datetime.now()).__contains__('15:00:00'):
        api.messages.send(user_id=244728879, message="Го заниматься!")
        time.sleep(sleep)
#Привет
    if nui != {}:
        if str(nui['body']).upper().__contains__('ПРИВЕТ'):
            try:
                api.messages.send(user_id=nui['uid'],
                                  message=random.choice(['Привет','ку','приветствую']))
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='Hello')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
#как дела
        elif str(nui['body']).upper().__contains__('КАК ДЕЛА'):
            try:
                api.messages.send(user_id=nui['uid'],
                                  message=random.choice(['Норм', 'Прекрасно', 'Отлично', 'Все пучком', 'Лучше всех',
                                                         'По тихой грусти', 'Всё ОК', 'Все хорошо', 'Ничего',
                                                         'Как в "Брат 2"', 'Отлично, не дождёшься',
                                                         'Вчера сломал 2 ребра']))
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='Good')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
#справочник Сломан
        elif str(nui['body']).upper().__contains__('Справочник'):
            try:
                api.messages.send(user_id=nui['uid'], message='Какую главу будем зубрить? \n' + Content.__doc__)
                api.messages.send(user_id=nui['uid'], message=ContentP2.__doc__)
                api.messages.send(user_id=nui['uid'], message=ContentP3.__doc__)
                api.messages.send(user_id=nui['uid'], message=ContentP4.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
#глава 1
        elif str(nui['body']).upper().__contains__('1.1'):
            try:
                api.messages.send(user_id=nui['uid'], message=C1L1.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
# глава 2
        elif str(nui['body']).upper().__contains__('2.1'):
            try:
                api.messages.send(user_id=nui['uid'], message=C2L1.__doc__)
                api.messages.send(user_id=nui['uid'], message=C2L1_2.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
# Помощь
        elif str(nui['body']).upper().__contains__('/HELP'):
            try:
                api.messages.send(user_id=nui['uid'], message=HELP.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
 #Обучение
        elif str(nui['body']).upper().__contains__('НАЧАТЬ ОБУЧЕНИЕ'):
            try:
                api.messages.send(user_id=nui['uid'], message='Укажите свой уровень знаний в Python \n '+ Ym.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
 #ур.нов.
        elif str(nui['body']).upper().__contains__('НОВИЧОК'):
            try:
                api.messages.send(user_id=nui['uid'], message='Ммм, так вы новичок,тогда я могу предложить вам \n' +   Mda.__doc__)
                api.messages.send(user_id=nui['uid'], message='P.s. курсы "Молодого бойца" ХОРОШИ')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
  #ур.Бывалый
        elif str(nui['body']).upper().__contains__('Бывалый'):
            try:
                api.messages.send(user_id=nui['uid'],
                                  message='Хороший выбор... \n' + Mid.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
#Профи
        elif str(nui['body']).upper().__contains__('Профи'):
            try:
                api.messages.send(user_id=nui['uid'],
                                  message='Если ты на столько крут, то тогда пройди пару задачь которые мы тебе предложем \n' + Top.__doc__)
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
        else:
            try:
                api.messages.send(user_id=nui['uid'], message='Не понял')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)
            except Exception:
                api.messages.send(user_id=nui['uid'], message='И что это?')
                time.sleep(sleep)
                api.messages.markAsRead(message_ids=nui['mid'])
                time.sleep(sleep)

