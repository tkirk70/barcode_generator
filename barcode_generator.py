import streamlit as st
import barcode
from barcode.writer import ImageWriter
from PIL import Image
import zipfile
import os

st.title('TCG BarCode Generator')
st.divider()
st.header('Select BarCode type and enter values')

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
    bc_values = st.text_area('BarCode Values (comma-separated)', value='123456789012,987654321098')

bc_values_list = [value.strip() for value in bc_values.split(',')]

zip_filename = 'barcodes.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for bc_value in bc_values_list:
        try:
            EAN = barcode.get_barcode_class(bc_type)
            my_ean = EAN(bc_value, writer=ImageWriter())
            fullname = my_ean.save(f'{bc_type}_barcode_{bc_value}')
            st.write(fullname)
            st.image(fullname, caption=f"Generated Barcode for {bc_value}")

            # Add PNG to ZIP file
            zipf.write(f'{fullname}')
        except Exception as e:
            st.write(f'Skipping {bc_type} for value {bc_value} because {e}')

with open(zip_filename, "rb") as file:
    btn_zip = st.download_button(
        label="Download All PNGs",
        data=file,
        file_name=zip_filename,
        mime="application/zip",
    )

# Custom CSS style for the text
custom_style = '<div style="text-align: right; font-size: 20px;">✨ A TDS Application ✨</div>'

# Render the styled text using st.markdown
st.markdown(custom_style, unsafe_allow_html=True)
