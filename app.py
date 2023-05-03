import streamlit as st
from questions import depression_questions, anxiety_questions, stress_questions, options
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page

streamlit_style()

st.image('logo.png')


# Add header
st.title('Sad2Happy - Your Emotional Wellness Companion')

# Add description
st.write('Sad2Happy is an innovative web application that uses Machine Learning algorithms to predict mental health risks. With our user-friendly questionnaires, we enable early diagnosis and intervention for depression, stress, and anxiety. Select any of the disorders below to continue')
st.header(' ')

# Add call buttons to navigate pages

def main():

    depression, anxiety, stress = st.columns(3)

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