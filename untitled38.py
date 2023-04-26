# -*- coding: utf-8 -*-
"""Untitled38.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zjC7dH0_d4SIuCcajiaYj3OvVfRkauvf
"""

import streamlit as st

st.set_page_config(page_title="Tweet Sentiment Predictor",layout="wide")

with st.container():
  st.title("Tweet Sentiment Predictor")
  st.subheader("Twitter has become a popular platform for users to express their opinions, including their experiences with various airlines. With the increasing volume of tweets related to US airlines, it has become essential for airlines to understand the sentiment of these tweets to gauge customer satisfaction and make data-driven decisions for improving their services. This App has tried to simplify this task by creating a sentiment predictor")

#%%writefile app.py
import streamlit as st
from textblob import TextBlob

#st.title("Sentiment Analysis App")

text = st.text_input("Enter some text")

if text:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        st.success("Positive")
    elif sentiment < 0:
        st.success("Negative")
    else:
        st.success("Neutral")
  

    polarity_visual = (sentiment + 1) / 2  # Normalize polarity to range [0, 1]
    polarity_scale = st.slider('Polarity Scale', min_value=-1.0, max_value=1.0, value=polarity_visual, step=0.01)
    #st.slider("Sentiment Polarity", min_value=-1.0, max_value=1.0, value=sentiment)
    #polarity_visual = (sentiment + 1) / 2  # Normalize polarity to range [0, 1]
    #polarity_scale = st.slider('Polarity Scale', min_value=-1.0, max_value=1.0, value=polarity_visual, step=0.01)
    #st.write('Polarity Scale:')
    #st.write(f'{"Negative":-<20} {"Positive":->20}')
    #st.write('|', '-'*int((polarity_scale+1)*20), 'o', '-'*int((1-polarity_scale)*20), '|')
    #st.write(f'{"-"*40} 0 {"-"*40} 1 {"-"*40}')
    #st.write('|', '-'*int((polarity_scale+1)*40/2), 'o', '-'*int((1-polarity_scale)*40/2), '|')

# Set app title
#st.title('Sentiment Analysis and Polarity Detection on Airline Tweets')