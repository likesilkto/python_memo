#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################
try:
	raise ValueError('error!')
	print('test')
	
except ValueError as e:
	print(e)

########################################

def a():
	print('begin a')
	raise ValueError('Error from a')
	print('end a')

def b():
	print('begin b')
	try:
		a()
	except:
		raise ValueError('Error from b')
	print('end b')

try:
	b()
except ValueError as e:
	print(e)

########################################

# http://uxmilk.jp/39845
