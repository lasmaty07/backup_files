import logging , smtplib , sys ,datetime , socket ,subprocess ,os, requests
from email.mime.text import MIMEText
import utils

# logs
logfile = 'backup.log'
logging.basicConfig(
		filename=logfile,
		format='%(asctime)s %(message)s',
		level=logging.INFO,
		datefmt='%Y-%m-%d %H:%M:%S')

try:
	with open('secrets.json', 'r') as s:
		secrets = json.load(s)
	with open('config.json', 'r') as f:
		config = json.load(f)
except IOError as e:
	logging.error(e)

shellscript = "/home/matt/backup/backup.sh"

logging.info("------------------- ")
logging.info("Start Script")

def email_update(subject,text):
	to = config["mail_to"]
	#solo el usuario sin el dominio
	gmail_user = secrets["gmail_user"]
	gmail_password = secrets["gmail_password"]
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_password)
	today = datetime.date.today()
	msg = MIMEText(text)
	msg['Subject'] = subject + ' ' + today.strftime('%d %b %Y')
	msg['From'] = 'Shell - Pluton'
	msg['To'] = to
	smtpserver.sendmail(gmail_user, [to], msg.as_string())
	smtpserver.quit()

def telegram_bot_sendtext(bot_message):
   bot_token = secrets["bot_token"]
   bot_chatID = secrets["bot_chatID"]
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


try:
	subprocess.call(shellscript)
	size= utils.size_converted('/media/samsung/backup_pluton/')
	body= 'backup of /home/matt completed with no errors. \nTotal backup size is: ' + size
	#email_update('Backup finished succesfully',body)
	telegram_bot_sendtext('**Backup finished succesfully**\n' + body)
	logging.info('Backup finished succesfully')
except Exception as e:
	#email_update('Error in backup',str(e)
	telegram_bot_sendtext("Error in backup " + str(e))
	logging.info(str(e))

logging.info("End Script")
logging.info("------------------- ")
sys.exit()
