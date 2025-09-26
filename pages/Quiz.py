import streamlit as st
import random # Standard library module, no need to add to requirements.txt

# Title and description
st.title("Which Jujutsu Kaisen Character Are You?")
st.write("Answer these questions to find out which sorcerer from the world of Jujutsu Kaisen matches your personality!")

# Use session state to manage quiz flow
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.results = None

# Start the quiz button
if not st.session_state.quiz_started:
    if st.button("Begin the Culling Game"):
        st.session_state.quiz_started = True
        st.session_state.scores = {"Yuji Itadori": 0, "Megumi Fushiguro": 0, "Nobara Kugisaki": 0, "Satoru Gojo": 0, "Kento Nanami": 0}

if st.session_state.quiz_started:
    # Use columns to lay out your quiz questions and images
    q1_col, q2_col = st.columns(2)

    with q1_col:
        st.header("Question 1")
        q1 = st.radio(
            "How do you prefer to exorcise a powerful curse?",
            ("Go all out with raw power", "Use careful planning and wait for the perfect moment", "Engage directly with a clever, tactical approach")
        )

        st.header("Question 2")
        q2 = st.multiselect(
            "What qualities do you value most in your companions?",
            ["Loyalty", "Intelligence", "Strength", "Respect for oneself"]
        )

    with q2_col:
        # Use an image related to Jujutsu Kaisen [required]
        st.image("Images/group.jpg")

        st.header("Question 3")
        q3 = st.number_input(
            "On a scale of 1-10, how well do you deal with overwhelming situations?",
            min_value=1, max_value=10
        )

    st.header("Question 4")
    q4 = st.selectbox(
        "What is your philosophy on life?",
        ("I don't want to regret the way I lived.", "I'll save people who want to be saved.", "I want the confidence to feel like it's okay to live.")
    ) #NEW

    st.header("Question 5")
    q5 = st.slider(
        "How would you rate your sense of humor?",
        0, 10, 5
    ) #NEW

    # Add a button to submit answers
    if st.button("See Your Domain Expansion"):
        # Calculate scores based on the new JJK questions
        if q1 == "Go all out with raw power":
            st.session_state.scores["Yuji Itadori"] += 1
            st.session_state.scores["Satoru Gojo"] += 1
        elif q1 == "Use careful planning and wait for the perfect moment":
            st.session_state.scores["Megumi Fushiguro"] += 1
            st.session_state.scores["Kento Nanami"] += 1
        else:
            st.session_state.scores["Nobara Kugisaki"] += 1

        if "Loyalty" in q2:
            st.session_state.scores["Yuji Itadori"] += 1
            st.session_state.scores["Megumi Fushiguro"] += 1
        if "Intelligence" in q2:
            st.session_state.scores["Satoru Gojo"] += 1
            st.session_state.scores["Megumi Fushiguro"] += 1
        if "Strength" in q2:
            st.session_state.scores["Yuji Itadori"] += 1
            st.session_state.scores["Satoru Gojo"] += 1
        if "Respect for oneself" in q2:
            st.session_state.scores["Nobara Kugisaki"] += 1
            
        # Add logic for number_input and slider
        if q3 > 7:
             st.session_state.scores["Satoru Gojo"] += 1
        else:
            st.session_state.scores["Yuji Itadori"] += 1

        if q4 == "I don't want to regret the way I lived.":
            st.session_state.scores["Yuji Itadori"] += 1
        elif q4 == "I'll save people who want to be saved.":
            st.session_state.scores["Megumi Fushiguro"] += 1
        else:
            st.session_state.scores["Nobara Kugisaki"] += 1

        if q5 > 7:
            st.session_state.scores["Satoru Gojo"] += 1
        elif q5 < 3:
            st.session_state.scores["Kento Nanami"] += 1
        else:
            st.session_state.scores["Yuji Itadori"] += 1

        # Determine the result based on the highest score
        result_char = max(st.session_state.scores, key=st.session_state.scores.get)
        st.session_state.results = result_char

if st.session_state.results:
    st.header("Your Jujutsu Kaisen Counterpart:")
    
    # Display the result and image
    st.success(f"You are {st.session_state.results}!")
    
    # Use images for each result [required]
    if st.session_state.results == "Yuji Itadori":
        st.image("Images/yuji.avif", caption="Yuji Itadori: The Vessel of Sukuna")
    elif st.session_state.results == "Megumi Fushiguro":
        st.image("Images/megumi.jpg", caption="Megumi Fushiguro: The Calculated Sorcerer")
    elif st.session_state.results == "Nobara Kugisaki":
        st.image("Images/nobara.avif", caption="Nobara Kugisaki: The Vicious Jujutsu Sorcerer")
    elif st.session_state.results == "Satoru Gojo":
        st.image("Images/gojo4.jpg", caption="Satoru Gojo: The Honored One")
    else: # Kento Nanami
        st.image("Images/nanami.jpg", caption="Kento Nanami: The Grumpy Adult")

    # Display confetti for the result [required]
    st.balloons() #NEW

    if st.button("Start Again"):
        st.session_state.quiz_started = False
        st.session_state.results = None
        st.rerun()

