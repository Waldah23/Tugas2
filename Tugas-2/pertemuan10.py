# pertemuan10
# 07 November 2024
# Streamlit

import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf

kamus_ticker = {
    'GOOGL': 'Google',
    'AAPL' : 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD' : 'McDonalds',
    'BBNI': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI' : 'Bank Mandiri (Persero) Tbk PT',
    'BBRI' : ' Bank Rakyat Indonesia (Persero) Tbk PT'
}
st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")
st.write("# Pendahuluan")


tickerSymbol = st.selectbox(
    'Silakan pilih kode perusahaan:',
    kamus_ticker.keys()
)

st.write(f'{kamus_ticker.keys()}')

st.write(f'Harga saham {kamus_ticker[tickerSymbol]}.')

tickerData = yf.Ticker(tickerSymbol)
pilihan_periode = st.selectbox(
    'Pilih periode:',
    ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y']
)
tickerDF = tickerData.history(
    period=pilihan_periode,
    start='2024-10-01',
    end= '2024-11-06'
)
st.write(tickerDF.info())
flag_tampil = st.checkbox('Tampilkan tabel')
if flag_tampil: 
    st.write(tickerDF.head(10))

flag_grafik = st.checkbox('Tampilkan grafik')
if flag_grafik:
    pilihan_atribut = st.multiselect(
        'Silahkan pilih atribut yang akan ditampilkan:',
        ['Low', 'High','Open', 'Close', 'Volume']
    )
    grafik = px.line(
        tickerDF,
        title=f'Harga Saham {tickerSymbol}',
        y = pilihan_atribut    
    )
    st.plotly_chart(grafik)
#df_bps
        