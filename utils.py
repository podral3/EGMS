import regex as re
def get_date_columns(columns):
    for idx, col in enumerate(columns):
        if re.fullmatch('\d{8}', col):
            return columns[idx:]
        
def match_dates(asc, dsc, days): #lists of dates in asc and dsc
    d = {}
    for asc_point in asc:
        for dsc_point in dsc: #TODO do optymalizacji!!!
            dsc_parsed = parse_to_date(dsc_point)
            asc_parsed = parse_to_date(asc_point)
            if(dsc_parsed - asc_parsed > timedelta(days=days)):
                break
            if dsc_parsed > asc_parsed: #jeżeli dsc nie jest przed asc to dodaje do dict
                if asc_point in d:
                    d[asc_point].append(dsc_point)
                else:
                    d[asc_point] = [dsc_point]
    return d

from datetime import datetime, timedelta
def parse_to_date(date):
    date_string = date
    date_format = "%Y%m%d"
    return datetime.strptime(date_string, date_format)

