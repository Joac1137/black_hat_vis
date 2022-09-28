import altair as alt
import pandas as pd


okc = pd.read_csv('denver_avgtemp.csv')
chart_okc = alt.Chart(okc).mark_line().encode(
    x=alt.X('year:Q',scale=alt.Scale(domain=(1930,1936))),
    y=alt.Y('avg_temp:Q', scale=alt.Scale(reverse=True, domain=(7.5,11)))
).interactive()

chart_okc_normal = alt.Chart(okc).mark_line().encode(
    x='year:Q',
    y='avg_temp:Q'
).interactive()

chart_all = alt.concat(chart_okc, chart_okc_normal)

chart_all.show()