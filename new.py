import pandas as pd
from pandas.core.frame import DataFrame
import plotly_express as pe

df = pd.read_csv("pro.csv")
print(df)
figure = pe.scatter(df,x="date",y="cases")
figure.show()