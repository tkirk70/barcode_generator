import streamlit as st
import barcode
from barcode.writer import ImageWriter
from PIL import Image
import cairosvg

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
    bc_value = st.text_input('BarCode Value', value='123456789012')

try:
    EAN = barcode.get_barcode_class(bc_type)
    my_ean = EAN(bc_value, writer=ImageWriter())
    fullname = my_ean.save(f'{bc_type}_barcode_{bc_value}')
    st.write(fullname)   
except Exception as e:
    st.write(f'Skipping {bc_type} because {e}')

st.image(fullname, caption="Generated Barcode")

with open(f'{fullname}', "rb") as file:
    btn_png = st.download_button(
        label="Download PNG",
        data=file,
        file_name=f"{fullname[:-4]}.png",
        mime="image/png",
    )


