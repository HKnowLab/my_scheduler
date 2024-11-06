###############################################################
# Batch 관련 정보
###############################################################
import os

class Enviroment:

    def __init__(self, root_dir):
       # 현재 스크립트의 경로
       self.cfg_dir = os.path.join(root_dir, 'cfg')
       self.sql_dir = os.path.join(root_dir, 'sql')

    def get_cfg_dir(self):
        return self.cfg_dir
    
    def get_sql_dir(self):
        return self.sql_dir