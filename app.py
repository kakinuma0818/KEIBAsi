# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

st.title("競馬予想テストアプリ")

st.write("CSVファイルをアップロードすると中身を表示します")

uploaded_file = st.file_uploader("CSV をアップロードしてください", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("読み込み成功！")
        st.dataframe(df)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
