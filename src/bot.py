import datetime as dt
import telebot
import config
bot = telebot.TeleBot(config.BOT_TOKEN)


text_user = ['ghbdtn', 'привет']
days_week = {
    'понедельник': 5,

    'вторник': 4,
    'среда': 3,
    'четверг': 2,
    'пятница': 1,
    'суббота': 0,
    'воскресенье': 1
}

current_list = {
    'Понедельник': '20.06.2022 в 19:00 английский - неделя, 27.06.2022 в 9-00 - Еврокапа',
    'Вторник': '9-30 Английский с Олегом 21.06. в 20-30 психолог',
    'Среда': '22.06 в вебинар ЯП',
    'Четверг': '',
    'Пятница': '9-30 Английский с Олегом',
    'Суббота': '17-00 испанскйи с Олегом',
    'Воскресенье': ''
}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    #bot.reply_to(message, f'Привет, {message.from_user.first_name} \U0001F64C')

    if message.text == '/time':
        time_utc = dt.datetime.utcnow()
        bot.reply_to(message, f'Время UTC: {time_utc}')

    elif message.text.lower() in text_user:
        print(message.text)
        bot.reply_to(
            message, f'Привет, {message.from_user.first_name} \U0001F64C')

    elif message.text == '/timetable':
        days = []
        for day, activity in current_list.items():
            days.append(f'{day}: {activity}')
        text = '\n'.join(days)
        bot.reply_to(message, text)

# Этим кодом хочу сократить запись следующего за ним кода!
    # for days in days_week():
    # elif message.text == days_week.keys():
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=days_week.values())
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

# Этот код работает!
    # elif message.text == 'понедельник':
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=5)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

    # elif message.text == 'вторник':
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=4)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

    # elif message.text == 'среда':
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=3)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

    # elif message.text == 'четверг':
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=2)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

    # elif message.text == 'пятница':
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=1)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

    # elif message.text == 'суббота':
    #     current_day = dt.datetime.utcnow() - dt.timedelta(days=0)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")

    # elif message.text == 'воскресенье':
    #     current_day = dt.datetime.utcnow() + dt.timedelta(days=1)
    #     bot.reply_to(
    #         message, f"{message.text} на этой неделе {current_day.strftime('%d %B %Y')}")


print('start polling')
bot.infinity_polling()
print('finish polling')
