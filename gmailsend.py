#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from simple_aes_cipher import AESCipher, generate_secret_key
from getpass import getpass

import os.path
import datetime
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from mimetypes import guess_type

import os
from stat import *

passphrase = "ig%zl:8v!7GgiQ,]v'*r9vb*[k!&`94NU3[e'!UvT1?1L:tj$l:,~.$@)&^Fl*I6"
cipher = AESCipher(generate_secret_key(passphrase))

class gmailsend(object):

	def __init__(self, passfile = '.gmailsend', relativepath = True, host = 'smtp.gmail.com', port = 465 ):
		if( relativepath ):
			passfile = os.path.dirname(__file__) + '/' + passfile
		account, password = gmailsend.get_accountpass(passfile)
		self.account = account + '@gmail.com'
		self.password = password
		self.host = host
		self.port = port
		
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

	def gen_passfile( passfile = '.gmailsend' ):
		account = input('account (without @gmail.com): ')
		password = getpass('password: ')
		account = cipher.encrypt( account )
		password = cipher.encrypt( password )
		with open(passfile, 'w') as fout:
			fout.write(account+'\n')
			fout.write(password+'\n')
		os.chmod(passfile, S_IRUSR|S_IWUSR )

	def get_accountpass( passfile = '.gmailsend' ):
		with open(passfile, 'r') as fin:
			account = fin.readline()
			password = fin.readline()
		account = cipher.decrypt( account )
		password = cipher.decrypt( password )
		return account, password



if( __name__ == '__main__'):
	gmailsend.gen_passfile()

	account, password =  gmailsend.get_accountpass()
	print(account)
	print(password)

	subject = 'subject'
	body = 'body'
	to_addr = ''

	attach_filepath = ['gmailsend.py']
	
	gmail = gmailsend()
	gmail.send(subject, body, to_addr, attach_filepath=attach_filepath )

# http://qiita.com/tadaken3/items/d39a16486c3a89ffa709
# http://t2y.hatenablog.jp/entry/20090705/1246772990

