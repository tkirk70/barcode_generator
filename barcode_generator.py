import streamlit as st
import pandas as pd

st.title('TCG BarCode Generator')
st.divider()
st.header('Select BarCode type and enter value')

bc_types = ['code128',
             'code39',
             'ean',
             'ean13',
             'ean14',
             'ean8',
             'gs1_128',
             'gtin',
             'isbn10',
             'issn',
             'itf',
             'pzn',
             'upc',
             'upca']

col1, col2 = st.columns(2)
with col1:
    bc_type = st.selectbox('BarCode Type', (bc_types))
with col2:
    bc_value = st.text_input('BarCode Value')