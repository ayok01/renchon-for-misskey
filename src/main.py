from apscheduler.schedulers.blocking import BlockingScheduler
from note import note
import logging

logging.basicConfig(level=logging.DEBUG)

sched = BlockingScheduler()
class Config(object):
    SCHEDULER_API_ENABLED = True

@sched.scheduled_job('cron', id='note', minute='*/15')
def cron_note():
    note()
    
if __name__ == "__main__":
    sched.start()
