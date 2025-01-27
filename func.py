from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, Updater, CommandHandler, CallbackQueryHandler
import random

def clean_result (result):
    return result.replace('{"result":{"alternatives":[{"message":{"role":"assistant","text":"',' ').split('"status"')[0].strip().    replace('$','').replace('\\Delta','Δ').replace('frac', '').replace('\\n','').replace('\\','').replace('}{','/').replace('}','').replace('{','').replace('int', '∫') [:-2]

def codif(update: Update, context: CallbackContext):
    file_path = "fi-9_oge_2025_kodif.pdf"
    update.message.reply_document(document=open(file_path, 'rb'), caption = 'Кодификатор ОГЭ')
    
    file_path = "code-2024.pdf"
    update.message.reply_document(document=open(file_path, 'rb'), caption = 'Кодификатор ЕГЭ')


def start(update: Update, context):
    update.message.reply_text("Привет, я помогу тебе с изучением физики!")

def help(update: Update, context):
    update.message.reply_text("1. /codif - отправляет кодификатор для ЕГЭ/ОГЭ по физике;"
                              "\n2. /recommend - отправляет список рекомендованных материалов для изучения физики")

def recommend(update: Update, context):
    update.message.reply_text("1. Г.С.Ландсберг - элементарный учебник физики в трёх томах;"
                              "\n2. Задачник А.П Рымкевича 10-11 кл;"
                              "\n3. Павел ВИКТОР (YOUTUBE канал);"
                              "\n4. Каталог хадач ШКОЛКОВО (ссылка: "
                              "https://3.shkolkovo.online/catalog);"
                              "\n5. Купер Л. Физика для всех. Классическая физика;"
                              "\n6. Чешев Ю.В ., Можаев В.В и др. Методическое пособие для поступающих в ВУЗ.")
