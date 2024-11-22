import pandas as pd
import matplotlib as plt

df_csv = pd.read_csv("pm10.csv")
df_csv.plot(x="Giorno", figsize=(9,6), kind="bar")
# TODO: plt.