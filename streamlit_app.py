import streamlit as st 
import pandas as pd
import requests
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

 
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
      st.write('Anda Setuju')
  
  
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)
  
  #slider 
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)
  
  #Input (Typing)
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))


#sidebar 
  sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
  sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])
  
  #columns :
  col1, col2, col3 = st.columns(3)

  with col1:
     st.header("A cat")
     st.image("https://static.streamlit.io/examples/cat.jpg")
  #atau dengan assignment 
  image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

  with col2:
     st.header("A dog")
     st.image("https://static.streamlit.io/examples/dog.jpg")

  with col3:
     st.header("An owl")
     st.image("https://static.streamlit.io/examples/owl.jpg")
  #expander 
  #dengan with atau dengan assignment 
  expander = st.expander("Klik Untuk Detail ")
  expander.write('Anda Telah Membuka Detail')

with st.form("Data Diri"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

if __name__ == '__main__' : 
  main()
