
import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

st.title("Gráficos de Acciones con Yahoo Finance 📊")

# Barra de búsqueda para ingresar el ticker
ticker = st.text_input("Ingrese el Ticker (ejemplo: GLD, AAPL, MSFT)", value="GLD")


# Opciones de intervalo personalizadas
intervalos = [
    "1m", "2m", "5m", "15m", "30m", "60m", "90m", "2h", "4h", "6h", "1d", "3d", "5d", "1wk", "1mo", "3mo"
]

if ticker:
    st.subheader("Precio de Cierre")
    col1, col2, col3 = st.columns(3)
    with col1:
        periodicidad = st.selectbox("Periodicidad", ["1d", "5d", "1mo", "3mo", "6mo", "1y"], key="periodicidad_grafico")
    with col2:
        intervalo = st.selectbox("Intervalo", intervalos, key="intervalo_grafico")
    with col3:
        tipo_grafico = st.radio("Tipo de gráfico", ["Lineal", "Velas"], key="tipo_grafico_grafico")

    data = yf.Ticker(ticker)
    # Solicitar más datos para evitar espacios vacíos
    df = data.history(period=periodicidad, interval=intervalo, prepost=True, actions=True, auto_adjust=False)

    fig = go.Figure()
    if tipo_grafico == "Lineal":
        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Precio de Cierre'))
    else:
        fig.add_trace(go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'],
                                     name='Velas'))
    fig.update_layout(
        xaxis_title='Fecha/Hora',
        yaxis_title='Precio',
        xaxis_rangeslider_visible=True,
        height=600,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(size=14),
        dragmode='pan',
        hovermode='x',
    )
    fig.update_xaxes(showspikes=True, spikecolor="#333", spikemode="across", spikesnap="cursor", showline=True)
    fig.update_yaxes(showspikes=True, spikecolor="#333", spikemode="across", spikesnap="cursor", showline=True)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Volumen de Negociación")
    colv1, colv2, colv3 = st.columns(3)
    with colv1:
        periodicidad_vol = st.selectbox("Periodicidad", ["1d", "5d", "1mo", "3mo", "6mo", "1y"], key="periodicidad_volumen")
    with colv2:
        intervalo_vol = st.selectbox("Intervalo", intervalos, key="intervalo_volumen")
    with colv3:
        tipo_grafico_vol = st.radio("Tipo de gráfico", ["Barras", "Lineal"], key="tipo_grafico_volumen")

    # Solicitar más datos para el gráfico de volumen
    df_vol = data.history(period=periodicidad_vol, interval=intervalo_vol, prepost=True, actions=True, auto_adjust=False)
    fig_vol = go.Figure()
    if tipo_grafico_vol == "Barras":
        fig_vol.add_trace(go.Bar(x=df_vol.index, y=df_vol['Volume'], name='Volumen', marker_color='orange'))
    else:
        fig_vol.add_trace(go.Scatter(x=df_vol.index, y=df_vol['Volume'], mode='lines', name='Volumen', line=dict(color='orange')))
    fig_vol.update_layout(
        xaxis_title='Fecha/Hora',
        yaxis_title='Volumen',
        xaxis_rangeslider_visible=True,
        height=600,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(size=14),
        dragmode='pan',
        hovermode='x',
    )
    fig_vol.update_xaxes(showspikes=True, spikecolor="#333", spikemode="across", spikesnap="cursor", showline=True)
    fig_vol.update_yaxes(showspikes=True, spikecolor="#333", spikemode="across", spikesnap="cursor", showline=True)
    st.plotly_chart(fig_vol, use_container_width=True)
