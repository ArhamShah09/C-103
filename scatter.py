from re import X
import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x = "Country", y = "Population", size = "InternetUsers", color = "Country")

fig.show()