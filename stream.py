import streamlit as st
import time 
st.header("Shapes Camculations")
st.sidebar.title("Configuration")
with st.sidebar:
 shape=st.selectbox("Choose shape:",["Circle","Rectangle"])
if shape=='Circle':
    rayon=st.number_input('Rayon',min_value=0,max_value=100,step=1)
    area=rayon*rayon*3.14
    perimeter=2*3.14*rayon
if shape=='Rectangle':
    width=st.number_input('width',0.,step=0.1)
    height=st.number_input('height',0.,step=0.1)
    area=width*height
    perimeter=2*(width+height)

compute_btn=st.button("compute area and perimeter")
if compute_btn:
  with st.spinner("Computing...."):
    time.sleep(2)
    st.balloons()
    st.write("area:",area)
    st.write('Perimeter:',perimeter)
