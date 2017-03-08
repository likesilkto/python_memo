#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for no display
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

import pandas as pd


#plt.plot( [3,1,4,1,5,9,2,6,5], label='data1' )
#plt.legend()
#plt.savefig('csvplot.png')

def csvplot( csvfile, figfile, plotdata ):
	df = pd.read_csv( csvfile )
	for data in plotdata:
		plt.plot( list(df[data]), label=data )
	plt.legend()
	plt.savefig(figfile)

if( __name__ == '__main__' ):
	csvplot( csvfile = 'csvplot.csv', figfile = 'csvplot.png', plotdata=['loss', 'val_loss'] )

# matplotlib
# http://yubais.net/doc/matplotlib/introduction.html
# http://yubais.net/doc/matplotlib/modify.html

# pandas
# http://qiita.com/hik0107/items/d991cc44c2d1778bb82e
# http://qiita.com/richi40/items/6b3af6f4b00d62dbe8e1
