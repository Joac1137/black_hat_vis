import altair as alt
import pandas as pd


okc = pd.read_csv('okc_avgtemp.csv')
chart_okc = alt.Chart(okc).mark_line().encode(
    x=alt.X('year:T',scale=alt.Scale(domain=(1952,1955))),
    y=alt.Y('avg_temp:Q', scale=alt.Scale(reverse=True, domain=(14,18)))
).interactive()

chart_okc_normal = alt.Chart(okc).mark_line().encode(
    x='year:T',
    y='avg_temp:Q'
).interactive()

chart_all = alt.concat(chart_okc, chart_okc_normal)

chart_all.show()