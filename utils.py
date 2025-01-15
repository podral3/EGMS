import regex as re
def get_date_columns(columns):
    for idx, col in enumerate(columns):
        strip = re.sub(r'\D', '', col)
        if re.fullmatch('\d{8}', strip):
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
    date_string = re.sub(r'\D', '', date)
    date_format = "%Y%m%d"
    return datetime.strptime(date_string, date_format)

from math import sqrt, inf
def euclidean_distance(x1: int, x2: int, y1: int, y2: int):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def nearest_neighbour(asc_cords_and_id, dsc_cords_list_with_ids, n_count) -> list[int]:
    """
    Zwraca indeksy n najbliższych sąsiadów punktów DSC
    """
    nn = [] 
    for _ in range(n_count):
        dist = inf
        small_idx = -1
        
        for idx, dsc in dsc_cords_list_with_ids.iterrows():
            c_dist = euclidean_distance(asc_cords_and_id[0], dsc['longitude'], asc_cords_and_id[1], dsc['latitude'])
            
            if c_dist < dist and idx not in nn:
                small_idx = idx
                dist = c_dist
        
        if small_idx != -1:
            nn.append(small_idx)
    
    return nn

import math
def wzor_pierwszy(v_asc,v_dsc, incident_asc, incident_dsc, track_angle_asc, track_angle_dsc):
    a1 = math.cos(incident_asc * math.pi / 180)
    a2 = math.sin(incident_asc * math.pi / 180) / math.cos((track_angle_asc - track_angle_dsc) * math.pi / 180)
    a3 = math.cos(incident_dsc * math.pi / 180)
    a4 = math.sin(incident_dsc * math.pi / 180)
    w1 = (a1 * a4) - (a2 * a3)
    w2 = (v_asc * a4)- (a2 * v_dsc)
    w3 = (a1 * v_dsc) - (a3 * v_asc)
    dap = w2 / w1
    dhald = w3 / w1
    return (dap, dhald)

def find_by_radius(asc_cords, dsc_cords_list_with_ids, radius):
    points_in_radius = []

    for idx, dsc in dsc_cords_list_with_ids.iterrows():
            distance = euclidean_distance(asc_cords[0], dsc['longitude'], asc_cords[1], dsc['latitude'])
            
            if distance <= radius:
                points_in_radius.append(idx)
    
    return points_in_radius

