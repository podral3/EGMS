from utils import save_row_to_csv
import pandas as pd 
from utils import wzor_pierwszy, get_date_columns, match_dates
import os

dap = []
dhald = []

def grid(asc_points: pd.DataFrame,
        dsc_points: pd.DataFrame, grid_size,
        output_filename: str = '',
        log: bool = True,
        latitude_col_name: str = "latitude",
        longitude_col_name: str = "longitude",
        incidence_col_name: str = "incidence_",
        track_angl_col_name: str = "track_angl"):
    min_x = min(pd.concat([asc_points[latitude_col_name], dsc_points[latitude_col_name]]))
    min_y = min(pd.concat([asc_points[longitude_col_name], dsc_points[longitude_col_name]]))

    max_x = max(pd.concat([asc_points[latitude_col_name], dsc_points[latitude_col_name]]))
    max_y = max(pd.concat([asc_points[longitude_col_name], dsc_points[longitude_col_name]]))

    asc_cols = get_date_columns(asc_points.columns)
    dsc_cols = get_date_columns(dsc_points.columns)
    matching_dates = match_dates(asc_cols, dsc_cols, 6)

    small_min_x = min_x
    small_min_y = min_y
    cords_with_value = []
    while small_min_x <= max_x:
        while small_min_y <= max_y:
            filtered_asc = get_from_bounding_box(asc_points, grid_size, small_min_x, small_min_y, latitude_col_name, longitude_col_name)
            filtered_dsc = get_from_bounding_box(dsc_points, grid_size, small_min_x, small_min_y, latitude_col_name , longitude_col_name)
            if(len(filtered_asc) != 0 and len(filtered_dsc) != 0):
                #iteracja po datach, powielenie kodu
                for asc_date in matching_dates:
                    dsc_dates = matching_dates[asc_date]
                    w = wzor_pierwszy(filtered_asc[asc_date].mean(), filtered_dsc[dsc_dates].mean(), filtered_asc[incidence_col_name].mean(),
                                filtered_dsc[incidence_col_name].mean(), filtered_asc[track_angl_col_name].mean(), filtered_dsc[track_angl_col_name].mean())
                    #pandas.series.series jako wynik
                    cords_with_value.append([small_min_x, small_min_y, w[0], w[1]])
                    if log:
                        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                        print("Calculated for grid", small_min_x, small_min_y)   # Log the message
                print(type(w[0]))        
                dap.append(w[0][1])
                dhald.append(w[1][1])
                save_row_to_csv('OutputGrid_Lodz.csv',(str(small_min_x) + ',' + str(small_min_y)) , dap,';')            
            small_min_y += grid_size
        small_min_y = min_y
        small_min_x += grid_size
    return cords_with_value

def get_from_bounding_box(points, grid_size, min_x, min_y, lat_col, lon_col):
    return points[
                (points[lat_col] >= min_x) & (points[lat_col] < min_x + grid_size)
                &
                (points[lon_col] >= min_y) & (points[lon_col] < min_y + grid_size)
                ]