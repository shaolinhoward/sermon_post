#!/usr/bin/python
# Jan 2014 Updates ID3 tag in mp3 recordings

import sys
import utils
import datetime
from ID3 import *

p_description = sys.argv[1]
p_description = p_description.replace("_", " ")
today = datetime.date.today()

# read centrally defined var vals
sermon_vars = utils.read_msg_bundle('/home/howard/git_repos/sermon_post/sermon_vars')

file_prefix = today.strftime('Hoc4Service%y%b%d_')
date_prefix = today.strftime("%b %d, %Y ")
id3_year = today.strftime("%Y")

# opening 
try:
	file_name = file_prefix + 'opening' + '.mp3'
	id3_title =  date_prefix + " Opening"

	id3info = ID3(file_name)
	print id3info
	id3info['TITLE'] = id3_title
	id3info['ARTIST'] = sermon_vars['id3_artist_worship']
	id3info['GENRE'] = int(sermon_vars['id3_genre'])
	id3info['ALBUM'] = sermon_vars['id3_album']
	id3info['TRACK'] = 1
	id3info['YEAR'] = id3_year
	for k, v in id3info.items():
		print k, ":", v
	id3info.write()
except:
	pass

# sermon
try:
	file_name = file_prefix + 'sermon' + '.mp3'
	id3_title =  date_prefix + p_description
	
	id3info = ID3(file_name)
	print id3info
	id3info['TITLE'] = id3_title
	id3info['ARTIST'] = sermon_vars['id3_artist_sermonizer']
	id3info['GENRE'] = int(sermon_vars['id3_genre'])
	id3info['ALBUM'] = sermon_vars['id3_album']
	id3info['TRACK'] = 2
	id3info['YEAR'] = id3_year
	for k, v in id3info.items():
		print k, ":", v
	id3info.write()
except InvalidTagError, message:
	print "Invalid ID3 tag (sermon):", message
	
# response 
try:
	file_name = file_prefix + 'response' + '.mp3'
	id3_title =  date_prefix + " Response"

	id3info = ID3(file_name)
	print id3info
	id3info['TITLE'] = id3_title
	id3info['ARTIST'] = sermon_vars['id3_artist_worship']
	id3info['GENRE'] = int(sermon_vars['id3_genre'])
	id3info['ALBUM'] = sermon_vars['id3_album']
	id3info['TRACK'] = 3
	id3info['YEAR'] = id3_year
	for k, v in id3info.items():
		print k, ":", v
	id3info.write()
except:
	pass

