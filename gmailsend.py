#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
from stat import *
import smtplib
from getpass import getpass

from simple_aes_cipher import AESCipher, generate_secret_key

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from mimetypes import guess_type


class gmailsend(object):

	def __init__(self, passpharse, passfile = '.gmailsend', relativepath = True ):
		host, port, account, password = gmailsend.get_passfile(passpharse, passfile, relativepath)
		self.host = host
		self.port = port
		self.account = account
		self.password = password
		
		# conection test #################################
		smtp = smtplib.SMTP_SSL(self.host, self.port)
		smtp.ehlo()
		smtp.login(self.account, self.password)
		smtp.quit()

	def send(self, subject, body, to_addr, from_addr = None, attach_filepath=None ):
		if( from_addr == None ):
			from_addr = self.account
		msg = self._create_message(from_addr, to_addr, subject, body, attach_filepath )
		self._sendmail(from_addr, to_addr, msg)

	def _create_message(self, from_addr, to_addr, subject, body, attach_filepath=None ):
		msg = MIMEMultipart()
		msg["Subject"] = subject
		msg["From"] = from_addr
		msg["To"] = to_addr
		
		body = MIMEText(body)
		msg.attach(body)
		
		for att in attach_filepath:
			filename = os.path.basename(att)

			# get mime-type by checking file extension 
			content_type = guess_type(att)[0]
			main_type, sub_type = content_type.split('/', 1)

			# add attached file with base64 encode
			sub_part = MIMEBase(main_type, sub_type)
			sub_part['Content-ID'] = filename
			sub_part.set_payload(open(att,'rb').read())
			encoders.encode_base64(sub_part)
			sub_part.add_header('Content-Type', content_type, name=filename)
			msg.attach(sub_part)
		return msg

	def _sendmail(self, from_addr, to_addr, msg):
		smtp = smtplib.SMTP_SSL(self.host, self.port)
		smtp.ehlo()
		smtp.login(self.account, self.password)
		smtp.sendmail(from_addr, to_addr, msg.as_string())
		smtp.quit()

	def get_passfile( passphrase, passfile = '.gmailsend', relativepath = True ):
		if( relativepath ):
			passfile = os.path.dirname(__file__) + '/' + passfile

		with open(passfile, 'r') as fin:
			host = fin.readline()
			port = fin.readline()
			account = fin.readline()
			password = fin.readline()

		cipher = AESCipher(generate_secret_key(passphrase))
		host = cipher.decrypt( host )
		port = int( cipher.decrypt( port ) )
		account = cipher.decrypt( account )
		password = cipher.decrypt( password )
		return host, port, account, password

	def gen_passfile( passfile = '.gmailsend', relativepath = True ):
		if( relativepath ):
			passfile = os.path.dirname(__file__) + '/' + passfile

		print('''
passfile includes all infromation to access your mail account.
PLEASE BE AWARE THE RISK!

If you understand the risk, please type "yes" and enter.
''')
		understood = input()
		if( understood.lower() == 'yes' ):
			print('''
*******************************************************
passphrase will be appeared in plain text in your code.
*******************************************************
''')

			passphrase = input( 'passphrase: ' )
			
			host = input( 'smtp host (defult: smtp.gmail.com): ' )
			if( host == '' ):
				host = 'smtp.gmail.com'
			
			port = input( 'port (defult: 465): ' )
			if( port == '' ):
				port = '465'
			account = input('account: ')
			
			flg = True
			while( flg ):
				password = getpass('password: ')
				password_conf = getpass('password (confirm): ')
				if( password == password_conf ):
					flg = False
				else:
					print('Not matched...')
			
			cipher = AESCipher(generate_secret_key(passphrase))
			
			host = cipher.encrypt( host )
			port = cipher.encrypt( port )
			account = cipher.encrypt( account )
			password = cipher.encrypt( password )
			with open(passfile, 'w') as fout:
				fout.write(host+'\n')
				fout.write(port+'\n')
				fout.write(account+'\n')
				fout.write(password+'\n')
			os.chmod(passfile, S_IRUSR|S_IWUSR )


if( __name__ == '__main__'):
	gmailsend.gen_passfile()

	passphrase = input('passphrase: ')
	gmail = gmailsend(passphrase)
	
	subject = 'subject'
	body = 'body'
	to_addr = ''

	attach_filepath = ['gmailsend.py']
	
	gmail.send(subject, body, to_addr, attach_filepath=attach_filepath )

# http://qiita.com/tadaken3/items/d39a16486c3a89ffa709
# http://t2y.hatenablog.jp/entry/20090705/1246772990

