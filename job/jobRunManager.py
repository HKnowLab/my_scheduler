import time

from apscheduler import job

from job import jobInfo
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_SCHEDULER_SHUTDOWN,EVENT_SCHEDULER_STARTED

class JobRunManager:

    # 선행작업 수행중인지 체크
    job_running = False 
    
    def __init__(self, jobInfo:jobInfo.JobInfo):
        self.scheduler = BlockingScheduler()
        self.__jobInfo = jobInfo
        self.job = None

    def job_listener(self, event):
        if event.exception:
            print(f"작업 {event.job_id} 실행 중 오류 발생: {event.exception}")
        else:
            print(f"작업 {event.job_id} 실행 성공")
    
    def add_job(self):

        # 선후행 체크 로직 - SQL 접속하여 선행 작업 실행여부 및 실행 상태 체크
        # - 스케쥴러는 선행작업 상태체크를 2분마다 해야 됩니다.
        # - 체크횟수는 기본값으로 60회로 설정합니다.

        #self.job = self.scheduler.add_job(self.job_run, 'interval', seconds=30)
        self.job = self.scheduler.add_job(self.job_run, 'date', run_date=datetime.now() + timedelta(seconds=3))
        #self.check_job = self.scheduler.add_job(self.job_status, 'interval', minutes=2)
        self.check_job = self.scheduler.add_job(self.job_status, 'interval', seconds=10)
        self.scheduler.add_listener(self.job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    def start(self):

        print("start :" + self.__jobInfo.get_jobid())
        self.scheduler.start()

        # TODO : 선행작업 확인 로직 추가
        #        upstream_list = self.__jobInfo.get_upstreams()
        # example - 10초 후에 'my_job' 함수 실행
        #scheduler.add_job(my_job, 'date', run_date=datetime.now() + timedelta(seconds=10))

    def job_status(self):
        print("job_status....." + str(self.job_running))
    
    def stop(self):
        time.sleep(5)
        self.__job.remove()

    def job_run(self):
        time.sleep(50000)
        print("작업 실행 중..." + self.__jobInfo.get_jobid())
        self.job_running = False



    