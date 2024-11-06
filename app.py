import os
import sys

from common import enviroment
from job import jobInfoManager, jobRunManager, jobInfo
from db import databaseInfo, databaseManager

if __name__ == '__main__':

    # root 경로    
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print("root_dir : " + root_dir)

    # Enviroment 클래스 생성 - 환경정보 관리
    env = enviroment.Enviroment(root_dir)
    print("cfg_dir : " + env.get_cfg_dir())
    print("sql_dir : " + env.get_sql_dir())

    # jobinfo 생성 - job에 대한 정보를 저장하는 class
    # params  : app.py [job_id]
    #           ex) python app.py job_01
    jobInfoManager = jobInfoManager.JobInfoManager(env.get_cfg_dir(), sys.argv[1])
    jobInfo = jobInfoManager.get_jobinfo()

    print(jobInfo.get_jobid())
    print(jobInfo.get_computetables())
    print(jobInfo.get_upstreams())
    print(jobInfo.get_sqlfilepath())

    # job start
    jobRunManager = jobRunManager.JobRunManager(jobInfo)
    jobRunManager.add_job()

    # databaseManager 생성 - sql 관리하는 class
    datbaseInfo = databaseInfo.DatabaseInfo(env.get_cfg_dir())
    databaseManager = databaseManager.DatabaseManager(databaseInfo)

    #jobRunManager.job()
    #jobRunManager.start()
    #jobRunManager.stop()


    # 선후행 체크 로직 - SQL 접속하여 선행 작업 실행여부 및 실행 상태 체크
    # - 스케쥴러는 선행작업 상태체크를 2분마다 해야 됩니다.
    # - 체크횟수는 기본값으로 60회로 설정합니다.
    #jobRunManager = jobRunManager(jobInfoManager._job_info.)
    

    # BatchManager를 통해서 배치 선후행 처리
    # TODO : BatchManager 생성
    # TODO : SQLManager 생성
    # batchManager를 이용하여 배치 작업 수행
    #batchInfo = batchInfo.BatchInfo("job_01")

    # batchManager를 이용하여 배치 작업 수행
    #batchSchedulerManager = batchSchedulerManager.BatchScheduler(batchInfo)
    
    # db_info.json 파일에서 db 정보 로드

    # batch_info.json 파일에서 batch 정보 로드

    #_batchInfo = batchInfo.BatchInfo()

    #batchSchedulerManager = batchSchedulerManager.BatchScheduler("job_01")
    #print(batchSchedulerManager.job_id)

    #config_path = os.path.join(current_dir, 'cfg\db_info.json')
