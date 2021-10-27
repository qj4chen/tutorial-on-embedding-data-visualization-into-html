import tushare as ts
import pandas as pd
import plotly.graph_objects as go
token = '6a721053ea3e70bb52605d6c0972caeda9ff080d3671f69bd8b6b434'
pro = ts.pro_api(token)
df = pro.daily(ts_code='600519.SH', start_date='20000101', end_date=20211027)

print(df.columns)
df.index = df['trade_date']
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)

# calculate k lines using 'open', 'high', 'low', 'close', 'vol'
fig = go.Figure(data=[
    go.Candlestick(x=df.index.strftime("%Y/%m/%d"),
                   open=df.open,
                   high=df.high,
                   low=df.low,
                   close=df.close,
                   increasing=dict(line_color='red'),
                   decreasing=dict(line_color='green')
                   )
])

fig.write_html('sample_plot.html')
