
class JobInfo():

    def __init__(self, json_string):
        self.__json_string = json_string
        
    def get_jobid(self):
        return self.__json_string['job_id']

    def get_sqlfilepath(self):
        return self.__json_string['sql_filepath']
    
    def get_upstreams(self):
        return self.__json_string['upstreams']

    def get_computetables(self):
        return self.__json_string['compute_tables']

