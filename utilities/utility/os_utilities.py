import os

def mkdir_if_not_exists(dir_name:str) -> int:
    try:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        return 200
    except:
        return 1