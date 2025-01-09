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

from math import sqrt, inf
def euclidean_distance(x1, x2, y1, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def nearest_neighbour(asc_cords_and_id, dsc_cords_list_with_ids, n_count):
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
    dhald = w3 / w1 #nie wiem o co chodzi
    return (dap, dhald)

def find_by_radius(asc_cords, dsc_cords_list_with_ids, radius):
    points_in_radius = []

    for idx, dsc in dsc_cords_list_with_ids.iterrows():
            distance = euclidean_distance(asc_cords[0], dsc['longitude'], asc_cords[1], dsc['latitude'])
            
            if distance <= radius:
                points_in_radius.append(idx)
    
    return points_in_radius

def find_min_max_points(points):
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    right_up_corner = None
    left_down_corner = None

    for point in points.iterrows():
        x, y = points['longitude'], points['latitude']

        # min wsp x
        if x < min_x:
            min_x = x
        
        # max wsp x
        if x > max_x:
            max_x = x
        
        # min wsp y
        if y < min_y:
            min_y = y
        
        # max wsp y
        if y > max_y:
            max_y = y

        return min_x, max_x, min_y, max_y

def search_grid(min_x, max_x, min_y, max_y, cell_size):
    left_up = (min_x, max_y)
    left_down = (min_x, min_y)
    right_up = (max_x, max_y)
    right_down = (max_x, min_y)

    width = euclidean_distance(left_up, right_up)
    height = euclidean_distance(left_up, left_down)

    cells_in_row = math.ceil(width / cell_size)
    cells_in_column = math.ceil(height / cell_size)

    square_list = []

    first_square = (left_up, (min_x + cell_size, max_y - cell_size))

    for row in range(cells_in_column):
        jump_in_row = 0
        jump_in_column = 0

        
        for col in range(cells_in_row):
            yes = 0 #byle co aby nie było błędu

    return left_up #to samo







