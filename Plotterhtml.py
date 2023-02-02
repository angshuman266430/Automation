import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import base64
from io import BytesIO

csv_dir = "ResultsMaker_output"
csv_files = glob.glob(csv_dir+"//*.csv")

plot_folder = 'plots'

figures = []
for file in csv_files:
    df = pd.read_csv(file)
    file_name = file.split('\\')[-1].split(".")[0]

    fig, ax = plt.subplots()
    ax.plot(df['Times'], df['Values'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Q (cfs)')
    ax.set_title(file_name)
    figures.append(fig)

with open("plots/plots.html", "w") as f:
    f.write("<html><body><table>")
    for i in range(len(figures)):
        buffer = BytesIO()
        figures[i].savefig(buffer, format='png')
        buffer.seek(0)
        img = buffer.getvalue()
        encoded = base64.b64encode(img).decode('utf-8')
        f.write(f"<td><img src='data:image/png;base64,{encoded}'></td>")
        if (i+1) % 4 == 0:
            f.write("</tr><tr>")
    f.write("</tr></table></body></html>")
