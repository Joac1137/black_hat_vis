import altair as alt
import pandas as pd
from vega_datasets import data




data = pd.read_csv("denver_avgtemp.csv")

print(data)
chart = alt.Chart(data).mark_line().encode(
    x='year:O',
    y=alt.Y('avg_temp:Q', scale=alt.Scale(reverse=True))
).interactive()
chart.show()