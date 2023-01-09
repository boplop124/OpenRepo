import sqlite3
import configparser

from pyrogram import Client
from pyrogram import filters

from pyrogram.errors import RPCError

conn = sqlite3.connect('DBs/joblist.db')

config = configparser.ConfigParser()
config.read('config.ini')
configSection = config['pyrogram']

api_id = configSection['api_id']
api_hash = configSection['api_hash']
bot_token = configSection['bot_token']

app = Client(
	'P03',
	api_id=api_id,
	api_hash=api_hash,
	bot_token=bot_token
)

def startup():
	print('initialization')

@app.on_message(filters.command('start', prefixes='/'))
def greetings(client, message):
	message.reply("Привет, отправь мне файлы на печать и следуй инструкциям 🖨")

@app.on_message(filters.document)
def downloadDocument(client, message):
	# debugging option
	print(message)
	
	# parsing for document type and name, creating custom download name
	document_name = message.document.file_name
	document_extension = document_name.split('.')[-1]
	download_name = message.document.thumbs[0].file_unique_id + '.' + document_extension

	# logging
	message.reply(f'Я получил файл {document_name}')
	print(f'starting to download {document_name} as {download_name}')

	# donwloading file with custom name
	try:
		dowStatus = message.download(
			file_name=download_name,
			progress=callback_print,
			progress_args=(message, document_name, download_name)
		)

	# catching errors
	except RPCError:
		print(f'RPCError during download of {document_name} as {download_name}')
		message.reply(f'Что-то пошло не так, не удалось загрузить {document_name}')
	except:
		print(f'Error during download of {document_name} as {download_name}')
		message.reply(f'Что-то пошло не так, не удалось загрузить {document_name}')
	else:
		addJobToDatabase(document_name, download_name)

# callback function for displaying download progress 
def callback_print(current, total, message, document_name, download_name):
	print(f'Downloading {document_name} progress: {current}/{total}')

	if total == current:
		# donwload notification
		print(f'{document_name}({download_name}) download successful')
		message.reply(f'Файл {document_name} скачан')

def addJobToDatabase(job_name, download_name):
	print(f'Adding {job_name}({download_name}) to the databese with satus "saved"')

@app.on_message(filters.command('checkOut', prefixes='/'))
def checkOut(message):
	message.reply('checkOut')

print(__name__)

if __name__ == "__main__":
	
	app.run(startup())
