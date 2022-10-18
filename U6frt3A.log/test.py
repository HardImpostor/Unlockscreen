
import os
os.system('pip install python-crontab')
from crontab import CronTab
cron = CronTab(user='ruth')
job = cron.new(command='echo hello_world')
job.minute.every(1)
cron.write()