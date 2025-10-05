import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt

st.title("Análisis de Acciones con Yahoo Finance")

# Entrada de usuario para el ticker
ticker_input = st.text_input("Introduce el ticker de la acción (por ejemplo, F para Ford):", value="F")

if ticker_input:
	ticker = yf.Ticker(ticker_input)
	st.subheader("Información General")
	st.subheader("Calendario")
	try:
		calendar = ticker.calendar
		st.dataframe(calendar)
	except Exception as e:
		st.warning(f"No se pudo obtener el calendario: {e}")

	st.subheader("Precio Objetivo de Analistas")
	try:
		price_targets = ticker.analyst_price_targets
		st.dataframe(price_targets)
	except Exception as e:
		st.warning(f"No se pudo obtener los precios objetivo: {e}")

	st.subheader("Estado de Resultados Trimestral")
	try:
		income_stmt = ticker.quarterly_income_stmt.T.reset_index()
		st.dataframe(income_stmt)
	except Exception as e:
		st.warning(f"No se pudo obtener el estado de resultados: {e}")

	st.subheader("Flujo de caja libre")
	try:
		cashflow = ticker.cashflow.T.reset_index()
		st.dataframe(cashflow)
		# Gráfico de flujo de caja libre
		fig, ax = plt.subplots()
		cashflow.set_index("index")["Free Cash Flow"].plot(kind="bar", title="Flujo de Caja Libre", ax=ax)
		ax.set_ylabel("USD")
		st.pyplot(fig)
	except Exception as e:
		st.warning(f"No se pudo obtener el flujo de caja libre: {e}")