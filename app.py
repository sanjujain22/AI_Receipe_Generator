import streamlit as st
from receipe import generate_receipe

st.title("Automated Receipe Generator")
ingredients = st.text_input("Enter the Ingredients:")
diet_type =st.selectbox("Select Diet",["Veg","Vegan","High-Protien"])

if st.button("Generate Receipe"):
    if ingredients:
        receipe = generate_receipe(ingredients,diet_type)
        st.write(receipe)
    else:
        st.warning("Please Enter the ingredients")