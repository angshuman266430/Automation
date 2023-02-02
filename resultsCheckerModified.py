import pandas as pd
import numpy as np
import glob
csv_dir = "ResultsMaker_output"
csv_files = glob.glob(csv_dir+"//*.csv")
df_results_summary = pd.DataFrame()

for csv in csv_files:
    df = pd.read_csv(csv)
    dict = {
        'Name':[csv.split('\\')[-1].split(".")[0]],
        'MaxValue':[df['Values'].max()],
        'MaxIndex':[df['Values'].idxmax()]
       }
    df_result = pd.DataFrame(dict)
    df_results_summary = pd.concat([df_results_summary, df_result])
    #print(df_result)
    df_results_summary.to_csv("Results_Summary.csv")
