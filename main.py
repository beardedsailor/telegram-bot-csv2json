import os
import sys
import logging
import csv
import json
import pandas as pd

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text("Hi! i'm the bot which convert csv to json")


def help(update, context):
    update.message.reply_text('Help! you can contact me through Description')


def doc_handler(update, context):
    file_id = update.message.document.file_id
    newFile = context.bot.get_file(file_id)
    chat_id = update.message.from_user.id
    newFile.download('file1.csv')
    update.message.reply_text("I'm working on your request")

    csvFilePath = "file1.csv"
    jsonFilePath = "data.json"
    # read the csv and add the data to a dictionary
    data = {}
    list2 = []
    with open("file1.csv") as f:
        for row in f:
            value = list2.append(row)
            # value=list2.split(",")
            ans = list2[0].split(",")
            val = ans[0]
            break
    with open(csvFilePath) as csvFile:
        csvFile = csv.DictReader(csvFile)
        for csvRow in csvFile:
            id = csvRow[val]
            data[id] = csvRow
    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))
    context.bot.send_document(chat_id=chat_id, document=open('data.json', 'rb'))


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    try:
        TOKEN = sys.argv[1]
    except IndexError:
        TOKEN = os.environ.get("TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.document, doc_handler))
    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Ready to rock..!")
    updater.idle()


if __name__ == '__main__':
    main()
