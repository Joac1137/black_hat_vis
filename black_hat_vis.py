import altair as alt
import pandas as pd
from vega_datasets import data




data_denver = pd.read_csv("denver_avgtemp.csv")
data_denver['year'] = data_denver['year'].astype(int)
data_denver = data_denver.rename(columns={'avg_temp': 'denver_avg_temp'}),

data_dallas = pd.read_csv("dallas_avgtemp.csv")
data_dallas = data_dallas.rename(columns={'avg_temp': 'dallas_avg_temp'})

data_denver = data_denver[0]
data_denver = data_denver.join(data_dallas["dallas_avg_temp"])
data_denver['dallas_avg_temp'] = data_denver['dallas_avg_temp'].astype(float)
data_denver['denver_avg_temp'] = data_denver['denver_avg_temp'].astype(float)


base = alt.Chart(data_denver).encode(
    alt.X('year:Q', axis=alt.Axis(title=None))
).properties(width=500)


line = base.mark_line(
    stroke='#5276A7', interpolate='monotone').encode(
    alt.Y('dallas_avg_temp', scale=alt.Scale(reverse=True),
    axis=alt.Axis(title='Dallas Average temperature', titleColor='#FF0000'))
).properties(width=500).interactive()

line2 = base.mark_line(
    stroke='#FF0000', interpolate='monotone').encode(
    alt.Y('denver_avg_temp',
          axis=alt.Axis(title='Denver average temperature', titleColor='#5276A6'))
).properties(width=500).interactive()


(line + line2).resolve_scale(
    y = 'independent'
).show()

