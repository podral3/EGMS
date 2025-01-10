import pandas as pd 
from utils import wzor_pierwszy, get_date_columns, match_dates

def grid(asc_points: pd.DataFrame, dsc_points: pd.DataFrame, grid_size):
    min_x = min(pd.concat([asc_points['latitude'], dsc_points['latitude']]))
    min_y = min(pd.concat([asc_points['longitude'], dsc_points['longitude']]))

    max_x = max(pd.concat([asc_points['latitude'], dsc_points['latitude']]))
    max_y = max(pd.concat([asc_points['longitude'], dsc_points['longitude']]))

    asc_cols = get_date_columns(asc_points.columns)
    dsc_cols = get_date_columns(dsc_points.columns)
    matching_dates = match_dates(asc_cols, dsc_cols, 6)

    small_min_x = min_x
    small_min_y = min_y
    cords_with_value = []
    while small_min_x <= max_x:
        while small_min_y <= max_y:
            filtered_asc = get_from_bounding_box(asc_points, grid_size, small_min_x, small_min_y)
            filtered_dsc = get_from_bounding_box(dsc_points, grid_size, small_min_x, small_min_y)
            if(len(filtered_asc) != 0 and len(filtered_dsc) != 0):
                #iteracja po datach, powielenie kodu
                for asc_date in matching_dates:
                    dsc_dates = matching_dates[asc_date]
                    w = wzor_pierwszy(filtered_asc[asc_date].mean(), filtered_dsc[dsc_dates].mean(), filtered_asc['incidence_angle'].mean(),
                                filtered_dsc['incidence_angle'].mean(), filtered_asc['track_angle'].mean(), filtered_dsc['track_angle'].mean())
                    #print(w[0], w[1])
                    cords_with_value.append([small_min_x, small_min_y, w[0], w[1]])
            small_min_y += grid_size
        small_min_y = min_y
        small_min_x += grid_size
    return cords_with_value

def get_from_bounding_box(points, grid_size, min_x, min_y):
    return points[
                (points['latitude'] >= min_x) & (points['latitude'] < min_x + grid_size)
                &
                (points['longitude'] >= min_y) & (points['longitude'] < min_y + grid_size)
                ]