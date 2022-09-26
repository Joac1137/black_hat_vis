import altair as alt
import pandas as pd


dallas = pd.read_csv('dallas_avgtemp.csv')
denver = pd.read_csv("denver_avgtemp.csv")
okc = pd.read_csv('okc_avgtemp.csv')
seattle = pd.read_csv('seattle_avgtemp.csv')

chart_dallas = alt.Chart(dallas).mark_line().encode(
    x='year:T',
    y='avg_temp:Q'
).interactive()

chart_denver = alt.Chart(denver).mark_line().encode(
    x='year:T',
    y='avg_temp:Q'
).interactive()

chart_okc = alt.Chart(okc).mark_line().encode(
    x='year:T',
    y='avg_temp:Q'
).interactive()

chart_seattle = alt.Chart(seattle).mark_line().encode(
    x='year:T',
    y='avg_temp:Q'
).interactive()

chart_all = alt.concat(chart_dallas, chart_denver, chart_okc, chart_seattle)
chart_all.show()


# data = pd.read_csv("denver_avgtemp.csv")

# chart = alt.Chart(data).mark_line().encode(
#     x='year:O',
#     y=alt.Y('avg_temp:Q', scale=alt.Scale(reverse=True))
# ).interactive()
# chart.show()