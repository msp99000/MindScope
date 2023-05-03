import streamlit as st
from questions import depression_questions, anxiety_questions, stress_questions, options
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page

streamlit_style()

# App Logo
st.image('logo.png')

# Add header
st.title('MindScope - Navigate Your Mind')

# Add description
description = '''
    Mindscope is an AI-powered application that helps individuals understand and manage their mental health. By analyzing responses to a questionnaire, it predicts the intensity of stress, depression, and anxiety. Mindscope provides personalized recommendations to improve mental well-being, including exercises and guided meditations. Its user-friendly interface and easy-to-understand insights make it an essential tool for anyone seeking to enhance their mental health.
'''
st.write(description)
st.header(' ')

def main():

    depression, anxiety, stress = st.columns(3)

    # Add call buttons to navigate pages
    with depression:
        dep_btn = st.button("Do you feel Depressed?")
        if dep_btn:
            switch_page("Depression")

    with anxiety:
        anx_btn = st.button("Do you feel Anxiety?")
        if anx_btn:
            switch_page("Anxiety")
        
    with stress:
        stress_btn = st.button("Do you feel Stressed?")
        if stress_btn:
            switch_page("Stress")

if __name__ == '__main__':
    main()