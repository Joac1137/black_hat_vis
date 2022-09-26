import altair as alt
import pandas as pd
from vega_datasets import data

cars = data.cars()

chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

chart.show()


data = pd.read_csv("denver_avgtemp.csv")


alt.Chart(data.reset_index()).mark_line().encode(
    x='index:T',
    y='value:Q'
)