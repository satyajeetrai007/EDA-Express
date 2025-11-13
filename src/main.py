import pandas as pd
import numpy as np

import streamlit as st
import sweetviz as sv
st.set_page_config(layout="wide") 
st.title("EDA Express")

file1 = st.file_uploader("Upload first CSV (e.g., Train)", type="csv")
file2 = st.file_uploader("Upload second CSV (e.g., Test)", type="csv")



if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    perform_eda = st.button("Perform EDA")

    report = sv.compare([df1, "First Dataset"], [df2, "Second Dataset"])
    report.show_html("sweetviz_compare.html", open_browser=False)

    # Display in Streamlit
    with open("sweetviz_compare.html", "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=1000, scrolling=True)



elif file1:
    df = pd.read_csv(file1)
    st.success("file uploaded successfully")
    target = st.text_input("Exact Name of Target Column")
    perform_eda = st.button("Perform EDA")

    if perform_eda:
        eda_html_sv = sv.analyze(df,target_feat = target)
        eda_html_sv.show_html("eda_html_sv.html", open_browser = False)
        with open("eda_html_sv.html","r", encoding= "utf-8") as f:
            html_content = f.read()

        st.components.v1.html(html_content, height = 10000, scrolling = True)


elif file2:
    df = pd.read_csv(file2)
    st.success("file uploaded successfully")
    target = st.text_input("Exact Name of Target Column")
    perform_eda = st.button("Perform EDA")

    if perform_eda:
        eda_html_sv = sv.analyze(df,target_feat = target)
        eda_html_sv.show_html("eda_html_sv.html", open_browser = False)
        with open("eda_html_sv.html","r", encoding= "utf-8") as f:
            html_content = f.read()

        st.components.v1.html(html_content, height = 10000, scrolling = True)
