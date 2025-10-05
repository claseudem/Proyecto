# Contenido de la página 2

import streamlit as st
import yfinance as yf

st.title("Información de Ticker")

# Barra de búsqueda para ingresar el ticker
ticker = st.text_input("Ingrese el Ticker (ejemplo: GLD, AAPL, MSFT)", value="GLD")

if ticker:
	data = yf.Ticker(ticker)
	info = data.info
	st.write(f"Aquí tienes información relevante sobre el ticker: **{ticker}**")
	# Campos principales
	campos_principales = [
		("Nombre", info.get('longName', 'N/A')),
		("Descripción", info.get('longBusinessSummary', 'N/A')),
		("Precio Actual", info.get('currentPrice', 'N/A')),
		("Cambio Diario", f"{info.get('regularMarketChangePercent', 'N/A')}%"),
		("Máximo 52 Semanas", info.get('fiftyTwoWeekHigh', 'N/A')),
		("Mínimo 52 Semanas", info.get('fiftyTwoWeekLow', 'N/A')),
	]

	# Mostrar los campos principales fuera de las columnas
	for label, value in campos_principales:
		st.write(f"**{label}:** {value}")

	# Subtítulo para información adicional
	st.subheader("Información adicional")

	# Mostrar el resto de los campos en dos columnas
	col1, col2 = st.columns(2)
	exclude_keys = ['longName', 'longBusinessSummary', 'currentPrice', 'regularMarketChangePercent', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow']
	restantes = [
		(key[:1].upper() + key[1:], info.get(key, 'N/A'))
		for key in info if key not in exclude_keys and key != 'companyOfficers'
	]
	for i, (label, value) in enumerate(restantes):
		if i % 2 == 0:
			col1.write(f"**{label}:** {value}")
		else:
			col2.write(f"**{label}:** {value}")

# Botón para ir a la página de gráficos con el ticker seleccionado
if st.button(f"Ver Gráficos de *{ticker}*"):
	st.experimental_set_query_params(ticker=ticker)
	st.switch_page("pages/graficos.py")

if st.button("Volver al Menú Principal"):
	st.switch_page("app.py")
