import datetime

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


if __name__ == "__main__":
    print(get_age())

