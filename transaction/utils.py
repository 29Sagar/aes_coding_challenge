import random
import datetime
year = datetime.date.today().year


def create_new_tr_number():
    tr_number = 'TRN/'+str(random.randint(0, 99999))+'/'+str(year)
    return str(tr_number)
