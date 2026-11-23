
import streamlit as st
from retriever import load_vector_store, get_retriever
from connect import create_llm, question_answer
from interview_mode import (
    generate_question,
    evaluate_answer,
    generate_followup_question
)
vector_store = load_vector_store()
retriever = get_retriever(vector_store)
llm = create_llm()
st.markdown(
    "<h1 style='text-align:center;'>AI/ML Interview Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "Your personal AI/ML learning and interview partner"
    "</p>",
    unsafe_allow_html=True
)

st.divider()


st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #111111;
    color: #F5F5F5;
}

/* Main content */
.block-container {
    max-width: 900px;
    padding-top: 3rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1B1B1B;
    border-right: 1px solid #333333;
}

/* All text */
.stApp, .stApp p, .stApp label,
.stApp span, .stApp li {
    color: #E5E5E5;
}

/* Headings */
h1, h2, h3 {
    color: #FFFFFF !important;
}

/* Buttons */
.stButton button {
    background-color: #D97757;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 20px;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #C56647;
    color: white;
}

/* Text input */
.stTextInput input,
.stTextArea textarea {
    background-color: #242424;
    color: white;
    border: 1px solid #444444;
    border-radius: 10px;
}

/* Input placeholder */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #999999;
}

/* Dropdown */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #242424;
    color: white;
    border: 1px solid #444444;
    border-radius: 10px;
}

/* Dropdown selected text */
.stSelectbox div[data-baseweb="select"] * {
    color: white;
}

/* Containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 12px;
}

/* Divider */
hr {
    border-color: #333333;
}

</style>
""", unsafe_allow_html=True)

mode = st.selectbox(
    "Select Mode",
    ["Learning Mode","Interview Mode"]
)
if mode=="Learning Mode":
    st.header("Learning Mode")
    question=st.text_input("Ask your AI/ML question")
    if st.button("Get Answer"):
       if question:
            try:
                result = question_answer(
                    question,
                    retriever,
                    llm
                )
                st.subheader("Answer")
                st.write(result["answer"])

            except Exception as e:
                st.error(f"API Error: {e}")
elif mode == "Interview Mode":
    st.header("Interview Mode")
    topic = st.selectbox(
        "Select Topic",
        ["Machine Learning", "Deep Learning", "NLP", "SQL"]
    )
    if st.button("Generate Question"):
        question = generate_question(
            topic,
            retriever,
            llm
        )
        st.session_state.question = question
    if "question" in st.session_state:
        st.subheader("Interview Question")
        st.write(st.session_state.question)
        candidate_answer = st.text_area(
            "Enter your answer"
        )
        if st.button("Evaluate Answer"):
            if candidate_answer:
                feedback = evaluate_answer(
                    st.session_state.question,
                    candidate_answer,
                    retriever,
                    llm
                )
                st.subheader("Evaluation")
                st.write(feedback)
                followup = generate_followup_question(
                    st.session_state.question,
                    candidate_answer,
                    feedback,
                    retriever,
                    llm
                )
                st.subheader("Follow-up Question")
                st.write(followup)

