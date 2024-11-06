###############################################################
# ※ JobInfo Class
#    - app.py 실행시 전달되는 json 파일의 정보를 parsing하여 저장
###############################################################
import json
from job import jobInfo

class JobInfoManager():
    
    def __init__(self, batch_dir, job_id):
        self.__batch_dir = batch_dir
        self.__job_id = job_id
        print("__init__ JobInfoManager : " + batch_dir)
        self.job_info = self.__json_file_load()
        
    def get_jobinfo(self):
        return self.job_info
    
    def __json_file_load(self):
        
        try:

        ###########################################################################
        # ※ 작업정보 json 형식
        #    "job_id"         // 작업ID 
        #    "sql_filepath"   // 해당 작업에서 수행할 SQL 파일 경로
        #    "upstreams"      // 선행작업 리스트
        #    "compute_tables" // 해당 작업 완료 후 통계정보 갱신이 필요한 테이블 리스트
        ###########################################################################
        
            # jobs 폴더에 관리하는 job_id 정보 로드
            # TODO : 파일 불러오기 및 파싱처리
            with open(self.__batch_dir + '\\' + self.__job_id + '.json', 'r', encoding='utf-8') as file:
                json_string = json.load(file)

            return jobInfo.JobInfo(json_string)
      
        except:
            # TODO : 에러처리
            self._job_info = None
            print("JobManager.set_jobInfo() Error" + '\r\n')