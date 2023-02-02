import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

csv_dir = "ResultsMaker_output"
csv_files = glob.glob(csv_dir+"//*.csv")
plot_folder = 'plotsNew'

for csv in csv_files:
    df = pd.read_csv(csv)
    file_name = csv.split('\\')[-1].split(".")[0]

    plt.plot(df['Times'], df['Values'])
    plt.xlabel('Times')
    plt.ylabel('Values')
    plt.title(file_name)
    plt.savefig(f'{plot_folder}/{file_name}.png', bbox_inches='tight')
    plt.clf()
