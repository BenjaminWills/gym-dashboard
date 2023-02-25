import datetime,os

from numpy import floor


def get_age(DOB:str = "07/03/2001") -> int:
    """Will return your current age given your DOB

    Parameters
    ----------
    DOB : str, optional
        Date of birth in the format dd/mm/yyyy, by default "07/03/2001"

    Returns
    -------
    int
        Current age as an integer
    """
    dob_datetime = datetime.datetime.strptime(DOB,'%d/%m/%Y')
    current_date = datetime.datetime.now()
    difference =  current_date - dob_datetime
    difference_in_years = difference.days / 365
    return int(floor(difference_in_years))

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")

def mkdir_if_not_exists(dir_name:str) -> int:
    try:
        if os.path.exists(dir_name):
            os.mkdir(dir_name)
        return 200
    except:
        return 1