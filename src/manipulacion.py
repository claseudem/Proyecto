import yfinance as yf
import streamlit as st

oro = yf.Ticker("GLD")

oro.info

oro.calendar

oro.analyst_price_targets

oro.quarterly_income_stmt.T.reset_index()

