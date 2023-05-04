import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from questions import depression_questions, options
import pickle
from sklearn.svm import SVC
from plot import plot_graph
import matplotlib.pyplot as plt
import numpy as np

state = st.session_state

state.responses = []
state.model_stress = pickle.load(open('./models/anxiety.pkl', 'rb'))

st.subheader("Answer the questions below")

def display_questions(questions):
    for i in range(len(questions)):
        st.write(f"{i +1 }. {questions[i]}")
        response = st.radio(label = "Choose one", options = [
            'Did not apply to me at all',
            'Applied to me to some degree, or some of the time',
            'Applied to me to a considerable degree, or a good part of the time',
            'Applied to me very much, or most part of the time'
        ], key = f"{i}") 

        st.write("")
        state.responses.append(response)

def convertor(lst):
    res = []
    for i in lst:
        if i == 'Did not apply to me at all':
            res.append(0)
        if i == 'Applied to me to some degree, or some of the time':
            res.append(1)
        if i == 'Applied to me to a considerable degree, or a good part of the time':
            res.append(2)
        if i == 'Applied to me very much, or most part of the time':
            res.append(3)
    return [res]

with st.expander("Expand for Questionnaire"):
    display_questions(depression_questions)

    submit_button = st.button("Submit")
    
if submit_button:
    state.prediction = state.model_stress.predict(convertor(state.responses))
    st.markdown("<h1 style = 'text-align: center;'> Model Predictions </h1>", unsafe_allow_html=True)  
    st.pyplot(plot_graph(state.prediction[0], 'Stress'))

st.write("")

home_button_end = st.button("🏠 Take me to Home Page", key = 'end')

if home_button_end:
    switch_page("Home")

