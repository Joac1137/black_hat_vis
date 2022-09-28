import altair as alt
import pandas as pd


dallas = pd.read_csv('dallas_avgtemp.csv')
denver = pd.read_csv("denver_avgtemp.csv")
okc = pd.read_csv('okc_avgtemp.csv')
seattle = pd.read_csv('seattle_avgtemp.csv')

df_overall_avg = dallas
avg_column = (dallas['avg_temp'] + denver['avg_temp'] + okc['avg_temp'] + seattle['avg_temp']) / 4

df_overall_avg['avg_temp'] = avg_column

print(denver)
print(df_overall_avg)

chart_overall_avg = alt.Chart(df_overall_avg).mark_line().encode(
    x='year:T',
    y='avg_temp:Q'
).interactive()

chart_overall_avg_reverse = alt.Chart(df_overall_avg).mark_line().encode(
    x=alt.X('year:Q', scale=alt.Scale(reverse=True), axis=alt.Axis(labels=False)),
    y=alt.Y('avg_temp:Q', scale=alt.Scale(reverse=True, domain=(11,15)), axis=alt.Axis(labels=False))
).interactive()

chart_denver = alt.Chart(denver).mark_line().encode(
    x=alt.X('year:Q', scale=alt.Scale(reverse=True)),
    y=alt.Y('avg_temp:Q', scale=alt.Scale(reverse=True, domain=(7,12)))
).interactive()

chart = alt.concat(chart_overall_avg, chart_overall_avg_reverse, chart_denver)

chart.show()