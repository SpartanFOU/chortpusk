import telebot  # pip install pyTelegramBotAPI
import random
import sys
import datetime
from datetime import datetime, date, time, timezone,timedelta
import workdays    #pip install workdays
API_TOKEN = '7029461470:AAFoyZSIZEoPe7ArIf-TpCHcJOHuM4J88gk' #bot token

bot = telebot.TeleBot(API_TOKEN)
user_dict = {}
class User:
    def __init__(self, name):
        self.name = name
        self.point = None

  
@bot.message_handler(commands=['kogda', 'when'])   #when function prints how many days lasts for vac when commands are /kogda /when
def send_welcome(message):                              #reaction to command
    today = datetime.now()
    print(today)
    vac=datetime(2024,3,28,5,00,00,00)
    wrk=workdays.networkdays(today,vac)
    vac_c=(vac-today)
    days=vac_c.days
    hrs=vac_c.seconds//3600
    mns=(vac_c.seconds//60)%60
    rand=4
    rand=random.randint(0,2)
    q_of_days=4
    degr_of_grust_mtx=[['Вам пизда!','Arbeiten!', 'ПОЧЕМУ ОН А НЕ Я ЕДЕТ В ЕГИПЕТ????'],
                   ['Не переживай - переживешь','Сейчас немного поработаешь, потом немного отдохнешь', 'AAAAAAAAAAAAA'],    #degree of sadness
                   ['ТУСЕЕЕЕЕЕМ', 'Собирайте чемоданы, вы едете в Новосиб', 'Назар, гони сотку']]
    if days>15:
        q_of_days=0
    elif days>10:
        q_of_days=1
    elif days>5:
        q_of_days=2
    deg_of_grust=degr_of_grust_mtx[q_of_days][rand]
    bot.send_message(message.chat.id,'До отпуска осталось '+str(days)+' дней, ' +str(hrs)+' часов, '+str(mns)+" минут \nИз них "+str(wrk)+" рабочие. \n"+str(deg_of_grust))

@bot.message_handler(commands=['help']) #please suck
def hlp(message):
    bot.send_message(message.chat.id, 'Никто тебе не поможет, несчастный. Отъебись от робота!')
@bot.massage_handler(commands=['Honda Game'])   #better than ubisoft games 
def registration(message):
    try:
        msg=bot.reply_to(message.chat.id, 'Пиши кликуху, звать тебя так буду')
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user 
        bot.register_next_step_handler(msg, game)
        
    except Exception as e: 
      bot.reply_to(message, 'oooops')  
def game(message):         
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        money=10000
        points=user.point=0
        bot.send_message(message.chat.id,"У тимура осталось "+money+" у.е.")
        while points<3000:
          bot.send_message(message.chat.id,"Что отхлебнет у Хонды? \n 1) Мотор \n 2) Коробка \n 3) Электрика \n 4) Акум \n 5) Арки \n 6) Шины")  
    except Exception as e: 
        bot.reply_to(message, 'oooops') 
@bot.message_handler(commands=['shutdown'])  #shutdown
def shdwn(sht):
    print('goodby')
    bot.stop_bot()

bot.infinity_polling() #works until shut down/killed terminal