#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello1')

sys.stdout = open('stdout.log', 'w')

print('Hello2')

sys.stdout.close()
sys.stdout = sys.__stdout__

print('Hello3')

with open('stdout.log','r') as fin:
	print( fin.read() )


# http://d.hatena.ne.jp/alicehimmel/20110213/1297611415
