import os
import telebot
import config
bot = telebot.TeleBot(config.BOT_MANAGER_TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if not message.from_user.username in config.ALLOWED_USERS:
        bot.reply_to(message, 'access denied')
        return

    if message.text == '/start_jarvis':
        result = os.system('pm2 start jarvis_bot')
        bot.reply_to(message, 'started' if result == 0 else 'error')

    elif message.text == '/stop_jarvis':
        result = os.system('pm2 stop jarvis_bot')
        bot.reply_to(message, 'stopped' if result == 0 else 'error')

    elif message.text == '/refresh_jarvis':
        result = os.popen('git pull').read()
        bot.reply_to(message, result)

        result = os.system('pm2 restart jarvis_bot')
        bot.reply_to(message, 'restarted' if result == 0 else 'error')

    else:
        bot.reply_to(message, 'unknown command')



bot.infinity_polling()