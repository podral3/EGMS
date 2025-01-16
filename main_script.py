import numpy as np
import pandas as pd
import os
from utils import *

asc_path = "dane_pociete/ascLodz.csv"
dsc_path = "dane_pociete/desc_Lodz.csv"
asc_df = pd.read_csv(asc_path, on_bad_lines='skip', sep=';', decimal=',', nrows=100)
dsc_df = pd.read_csv(dsc_path, on_bad_lines='skip', sep=';', decimal=',', nrows=100)
print("Files loaded")

def calculate_for_each_point(asc_df: pd.DataFrame, dsc_df: pd.DataFrame,
                             output_file_name: str = '',
                             log: bool = True,
                             latitude_col_name: str = "latitude",
                             longitude_col_name: str = "longitude",
                             incidence_col_name: str = "incidence_",
                             track_angl_col_name: str = "track_angl"):
    asc_cols = get_date_columns(asc_df.columns)
    dsc_cols = get_date_columns(dsc_df.columns)
    matching_dates = match_dates(asc_cols, dsc_cols, 6)

    create_new_csv('output/dap.csv', asc_cols, ';')
    create_new_csv('output/dhald.csv', asc_cols, ';')

    for idx, asc in asc_df.iterrows(): #dla kazdego wiersza w ASC
        dap = []
        dhald = []
        asc_tuple = (asc[latitude_col_name], asc[longitude_col_name])
        nn_idx = nn_kdtree(asc_tuple, dsc_df[['pid', 'latitude', 'longitude']], 5)
        #nn_idx = radius_kdtree(asc_tuple, dsc_df[['pid', 'latitude', 'longitude']], 0.001)
        nn_points = dsc_df.iloc[nn_idx]
        for asc_date in matching_dates: #dla kazdej daty w jednym wierszu ASC
            dsc_dates = matching_dates[asc_date]#POLICZ WZOR
            w = wzor_pierwszy(asc[asc_date], nn_points[dsc_dates].mean(), 
                              asc[incidence_col_name], 
                              nn_points[incidence_col_name].mean(), 
                              asc[track_angl_col_name], 
                              nn_points[track_angl_col_name].mean())
            
            if(log):
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                print("Calculated for point",[idx+1], " out of ", len(asc_df))   # Log the message
            #tutaj zamiast append mean to wzor podstawiamy
            dap.append(w[0])
            dhald.append(w[1])
            
        save_row_to_csv('output/dap.csv', asc['pid'],dap,';')
        save_row_to_csv('output/dhald.csv', asc['pid'],dhald,';')
            

calculate_for_each_point(asc_df, dsc_df, log=True)

from grid import grid
#data = grid(asc_df, dsc_df , 0.5)