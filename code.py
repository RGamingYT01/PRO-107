import plotly.express as px
import pandas as pd 
import csv
df = pd.read_csv("C-107\project\data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig= px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()
