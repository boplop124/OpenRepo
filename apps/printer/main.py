import configparser

import requests
import datetime 
# import win32print

import subprocess

config = configparser.ConfigParser()
config.read('config.ini')
configSection = config['monobank']

TOKEN = configSection['TOKEN']
END_POINT = configSection['END_POINT']
TRANSACTIONAL_ENDPOINT = configSection['TRANSACTIONAL_ENDPOINT']

def getTransactions(timedelta=30):
	"""Returns transactional list"""
	dateNow = datetime.datetime.now()
	timedelta = datetime.timedelta(days=timedelta)
	dateFrom = dateNow - timedelta
	timestampFrom = int(dateFrom.timestamp())

	transactions = requests.get(TRANSACTIONAL_ENDPOINT.format(timestampFrom), headers={'X-Token': TOKEN})
	print(transactions.text)
	# values: id, time, description, amount, ballance
	return transactions


def printsomehting():
	printer='Xerox Phaser 3020'
	pdffile=r'C:\Programming\Random projects\Printer\downloads\AgAD-hUAAk2-uEk.pdf'
	acroread=r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'
	#'"%s"'is to wrap double quotes around paths
	# as subprocess will use list2cmdline internally if we pass it a list
	#which escapes double quotes and Adobe Reader doesn't like that
	cmd='"%s" /N /T "%s" "%s"'%(acroread,pdffile,printer)
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr=proc.communicate()
	exit_code=proc.wait()

getTransactions()
# printsomehting()
# https://pypi.org/project/pywin32/
# https://docs.pyrogram.org/
