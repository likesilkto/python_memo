#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

def timedelta2str( td, format='{y:04d}/{m:02d}/{d:02d} {H:02d}:{M:02d}:{S:02d}' ):
	seconds = int(td.total_seconds())
	periods = [
		('year',   60*60*24*365),
		('month',  60*60*24*30),
		('day',    60*60*24),
		('hour',   60*60),
		('minute', 60),
		('second', 1)
	]
	
	data = {}
	for period_name, period_seconds in periods:
		if( seconds > period_seconds ):
			period_value, seconds = divmod(seconds,period_seconds)
			data[period_name] = period_value
		else:
			data[period_name] = 0
	
	str = format.format(
		y = data['year'],
		m = data['month'],
		d = data['day'],
		H = data['hour'],
		M = data['minute'],
		S = data['second'],
		)
	return str

if( __name__ == '__main__' ):
	first_time = datetime(2016,3,4,5,6, 7)
	last_time =  datetime(2017,3,4,8,9,10)
	td = last_time - first_time
	print( timedelta2str( td ) )

# http://stackoverflow.com/questions/538666/python-format-timedelta-to-string
