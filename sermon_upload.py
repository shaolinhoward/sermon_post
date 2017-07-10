#!/usr/bin/python

import datetime
import utils
from ftplib import FTP
from sys import argv
import subprocess

today = datetime.date.today()
print today

# read centrally defined var vals
sermon_vars = utils.read_msg_bundle('/home/howard/git_repos/sermon_post/sermon_vars')

ftp = FTP(sermon_vars['ftp_url'])
ftp.login(sermon_vars['ftp_username'], sermon_vars['ftp_password'])
year = today.strftime('%Y')
ftp.cwd(year)
fileName = today.strftime('Hoc4Service%y%b%d_sermon.mp3')
fileHandle = file(fileName,'rb')
ftp.storbinary('STOR '+ fileName, fileHandle)
ftp.quit()

# upload to google drive (hoc4root)
#gdrive upload Hoc4Service17Feb19_opening.mp3 --parent 0B-55NH9KtvhmNmExUVBkaFBFejQ
#upload = 'gdrive'
#cmd = 'upload '
#fileName = today.strftime('Hoc4Service%y%b%d_opening.mp3')
#parent_flag = ' --parent '
#parent_folder = sermon_vars['gdrive_recording_folderid']
##os.system(upload_cmd + fileName + parent_folder)
#subprocess.call([upload, cmd, fileName, parent_flag, parent_folder], shell=True);
