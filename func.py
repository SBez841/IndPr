from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, Updater, CommandHandler, CallbackQueryHandler

def clean_result (result):
    result = result.replace('{"result":{"alternatives":[{"message":{"role":"assistant","text":"',' ')
    result = result.split('"status"')[0].strip()
    result = result.replace('$','').replace('\\Delta','Δ').replace('frac', '')
    result = result.replace('\\n','').replace('\\','').replace('}{','/').replace('}','')
    result = result.replace('{','').replace('int', '∫') [:-2]

def codif(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("ОГЭ", callback_data="OGE"), InlineKeyboardButton("ЕГЭ", callback_data="EGE")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Для какого экзамена вам нужен кодификатор?", reply_markup=reply_markup)

def send_codif(update: Update, context: CallbackContext):
    query = update.callback_query
    exam_type = query.data  # Получаем, какую кнопку нажал пользователь
    chat_id = query.message.chat_id

    if exam_type == "OGE":
        file_path = "fi-9_oge_2025_kodif.pdf"  # Путь к кодификатору ОГЭ
        message = "Отправляю кодификатор для ОГЭ."
    elif exam_type == "EGE":
        file_path = "code-2024.pdf"  # Путь к кодификатору ЕГЭ
        message = "Отправляю кодификатор для ЕГЭ."

    context.bot.send_document(chat_id=chat_id, document=open(file_path, 'rb'))
    query.edit_message_text(message)
    
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
