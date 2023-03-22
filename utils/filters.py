from django.utils.dateparse import parse_date
from datetime import datetime

def formata_data(date):
    try:
        dateptime = parse_date(date)
    except:
        date = date[:8] + '01'
        print(date)
        dateptime = parse_date(date)
    return dateptime.strftime("%d %b %Y")