import streamlit as st
import pandas as pd
import barcode

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

# try:
#     EAN = barcode.get_barcode_class(bc_type)
#     my_ean = EAN(bc_value)
#     fullname = my_ean.save(f'{bc_type}_barcode')
#     st.write(fullname)
# except Exception as e:
#     st.write(f'Skipping {bc_type} because {e}')

# import EAN13 from barcode module 
from barcode import EAN13 

# import ImageWriter to generate an image file 
from barcode.writer import ImageWriter 

# Make sure to pass the number as string 
number = '5901234123457'

# Now, let's create an object of EAN13 class and 
# pass the number with the ImageWriter() as the 
# writer 
my_code = EAN13(number, writer=ImageWriter()) 

# Our barcode is ready. Let's save it. 
my_code.save("new_code1")

st.image(my_code)
st.image(fullname)


