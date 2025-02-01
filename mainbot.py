#Импорт функций библиотеки python-telegram-bot
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler

#Импорт функции ЯндексГПТ
from YAGPT import get_response

#Импорт команд бота
from func import recommend, start, help
from func import codif, send_codif, exam_demo, send_exam_demo

from consts import TG_Token

import json

HISTORY_FILE = "user_history.json"
history = {}

#Функция загрузки (открытия) файла истории
def load_history():
    global history
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = {}

#Функция сохранения истории
def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

#Команда очистки истории сообщений
def reset_history(update: Update, context):
    update.message.reply_text("История сообщений очищена.")
    user_id = str(update.message.from_user.id)
    history[user_id] = []
    save_history()

#Обработчик сообщений и добавление их в историю
def handle_message(update: Update, context):
    user_id = str(update.message.from_user.id)
    user_message = update.message.text

#Добавление/Очистка истории сообщений пользователя
    if user_id not in history or len(history[user_id]) > 37:
        history[user_id] = []
        
    history[user_id].append({"role": "user", "text": user_message})
    response = get_response(history[user_id])
    history[user_id].append({"role": "assistant", "text": response})
    save_history()
    update.message.reply_text(response)

def main():
    load_history()
    updater = Updater(TG_Token, use_context=True)
    dp = updater.dispatcher

#Команды /start, /help, /recommend, /reset
    dp.add_handler(CommandHandler("recommend", recommend))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reset", reset_history))

#Команда /ExamDemo
    dp.add_handler(CommandHandler("ExamDemo", exam_demo))
    dp.add_handler(CallbackQueryHandler(send_exam_demo, pattern="ОГЭ"))
    dp.add_handler(CallbackQueryHandler(send_exam_demo, pattern="ЕГЭ"))

#Команда /codif
    dp.add_handler(CommandHandler("codif", codif))
    dp.add_handler(CallbackQueryHandler(send_codif, pattern="OGE"))
    dp.add_handler(CallbackQueryHandler(send_codif, pattern="EGE"))
    
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,
                                  handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
