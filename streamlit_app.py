import streamlit as st 
import pandas as pd
# import requests
# from st_aggrid import AgGrid

house = pd.read_csv('house_clean.csv')

def main() :
  st.header('Halaman Streamlit Muhammad Abdul Baasith')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

  st.dataframe(house)

  st.write('Metrics')
  st.metric(label="Temperature", value="30.3 °C", delta="1.4 °C")

  # AgGrid(house)
  # st.table([x for x in range(1,5)])

if __name__ == '__main__' : 
  main()
