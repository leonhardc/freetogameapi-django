from django.utils.dateparse import parse_date


def formata_data(date):
    dateptime = parse_date(date)
    return dateptime.strftime("%d %b %Y")