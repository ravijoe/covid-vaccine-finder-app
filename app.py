import pandas as pd
import streamlit as st
from get_results import fetch


# sincere thanks to bhavesh bhatt and krish naik
# https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability
# https://www.youtube.com/watch?v=IWWu9M-aisA


# @app.route('/')
def welcome():
    return "Welcome All"


def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Covid Vaccine Finder App. </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    POST_CODE = st.text_input("enter pin code :- ")
    result=None
    if st.button("Predict"):
        result = fetch(POST_CODE)
    st.success('The output is ')
    st.dataframe(result)
    if st.button("About"):
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
