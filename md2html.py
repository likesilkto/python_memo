#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markdown
import glob
import os.path

gfm = markdown.Markdown(output_format='html5', extensions=['gfm'])

files = glob.glob('*.md')
for file in files:
	basename = os.path.basename(file)
	titlename = os.path.splitext(basename) [0]
	
	with open(file, 'r') as fin:
		md = fin.read()
	html = gfm.convert(md)
	
	with open(titlename+'.html','w') as fout:
		fout.write(html)
	
	print( file + ' -> ' + titlename+'.html')
	
