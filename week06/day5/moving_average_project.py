import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
df = pd.read_csv(r'C:\Users\gabri\Documents\Practice files\Apple Stock Prices From 1981 to 2023\Apple Stock Prices (1981 to 2023).csv')

# Convert and clean
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')

# Keep last 200 rows (clean view)
df = df.tail(200)

# Moving averages
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# -----------------------------
# Create subplots (Price + Volume)
# -----------------------------
fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.05,
    row_heights=[0.7, 0.3]
)

# -----------------------------
# Candlestick
# -----------------------------
fig.add_trace(
    go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name="Candlestick"
    ),
    row=1, col=1
)

# -----------------------------
# Moving Averages
# -----------------------------
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['MA20'],
        mode='lines',
        name='MA20'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['MA50'],
        mode='lines',
        name='MA50'
    ),
    row=1, col=1
)

# -----------------------------
# Volume Bars
# -----------------------------
fig.add_trace(
    go.Bar(
        x=df['Date'],
        y=df['Volume'],
        name='Volume'
    ),
    row=2, col=1
)

# -----------------------------
# Layout (Zoom enabled automatically)
# -----------------------------
fig.update_layout(
    title="Interactive Stock Dashboard",
    xaxis_rangeslider_visible=True,   # 🔥 zoom slider
    template="plotly_dark",
    height=800
)

fig.show()