import streamlit as st
import google.generativeai as genai
import io
api_key = "AIzaSyDrcJCbsNohn7CR6I8vDyGtYKXocTu0PRU"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
st.set_page_config(
    page_title="League Bot",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# CSS Styling
st.markdown("""
    <style>
        .header {
            font-size: 28px;
            color: #FFA500;
            text-align: center;
            margin-bottom: 20px;
            font-weight: bold;
        }
        .subheader {
            font-size: 20px;
            color: #00BFFF;
            margin-bottom: 10px;
        }
        .content {
            font-size: 16px;
            color: #000;
        }
        .streamlit-expanderHeader {
            font-size: 18px;
            font-weight: bold;
            color: #4CAF50;
        }
        .you-message {
            background-color: #1E1E1E;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .bot-message {
            background-color: #282828;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .recommendation {
            background-color: #333333;
            color: #00FF00;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .stats-section {
            background-color: #1E1E1E;
            color: #FFD700;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .counter-section {
            background-color: #333333;
            color: #FF4500;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
    <div class="header">League Bot</div>
""", unsafe_allow_html=True)
# Session state management
if 'sessions' not in st.session_state:
    st.session_state['sessions'] = {}
if 'current_session' not in st.session_state:
    st.session_state['current_session'] = None
if 'context' not in st.session_state:
    st.session_state['context'] = (
        "You are a 15-year-old boy with a casual, laid-back style of speaking. "
        "You are also an expert in League of Legends, providing builds and advice for various champions. "
    )
# Sidebar for settings
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Your Name", "")
theme_color = st.sidebar.color_picker("Pick A Color", "#00F900")
session_name = st.sidebar.text_input("Session Name", "")
if st.sidebar.button("Start New Session"):
    if session_name:
        st.session_state['sessions'][session_name] = []
        st.session_state['current_session'] = session_name
current_session = st.session_state['current_session']
if current_session:
    st.sidebar.write(f"Current Session: {current_session}")
    if st.sidebar.button("End Current Session"):
        st.session_state['current_session'] = None
# Summarize chat history
def summarize_chat_history(chat_history):
    summary = "Summary of chat history:\n"
    for role, text in chat_history:
        summary += f"{role}: {text}\n"
    return summary
if current_session:
    context = st.text_area("Update Context", value=st.session_state['context'])
    if st.button("Update Context"):
        chat_history = st.session_state['sessions'][current_session]
        summary = summarize_chat_history(chat_history)
        st.session_state['context'] = context + "\n\n" + summary
        st.success("Context updated successfully!")
# Get response from Gemini Pro model
def get_gemini_response(question, chat_history):
    try:
        context = st.session_state['context']
        for role, text in chat_history:
            context += f"{role}: {text}\n"
        context += f"You: {question}\nBot: "
        response = chat.send_message(context, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []
# Additional Data for Stats and Counter Picks
champion_data = {
    "Ahri": {
        "stats": "Health: 570, Mana: 418, Attack Damage: 53",
        "counters": "Zed, Yasuo, LeBlanc"
    },
    "Yasuo": {
        "stats": "Health: 490, Mana: None, Attack Damage: 60",
        "counters": "Malphite, Rammus, Quinn"
    },
    "Darius": {
        "stats": "Health: 582, Mana: 263, Attack Damage: 64",
        "counters": "Teemo, Garen, Quinn"
    }
    # Add more champions as needed
}
def get_champion_data(champion_name, data_type):
    data = champion_data.get(champion_name, {})
    return data.get(data_type, f"{data_type.capitalize()} not found.")
# User Input Section
input_text = st.text_input("Input:", key="input", placeholder="Ask about League of Legends builds, stats, or advice...")
submit = st.button("Ask the question", help="Click to get a response from Gemini.")
if submit and input_text and current_session:
    response = get_gemini_response(input_text, st.session_state['sessions'][current_session])
    if response:
        chat_history = st.session_state['sessions'][current_session]
        chat_history.append(("You", input_text))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            chat_history.append(("Bot", chunk.text))
        # Detect champion stats or counter requests
        champion_name = input_text.split()[-1].capitalize()
        if "stats" in input_text.lower():
            stats = get_champion_data(champion_name, "stats")
            st.markdown(f"<div class='stats-section'><strong>{champion_name} Stats:</strong> {stats}</div>", unsafe_allow_html=True)
        elif "counter" in input_text.lower():
            counters = get_champion_data(champion_name, "counters")
            st.markdown(f"<div class='counter-section'><strong>Counter Picks for {champion_name}:</strong> {counters}</div>", unsafe_allow_html=True)
# Display Chat History
st.subheader("The Chat History is")
if current_session:
    chat_history = st.session_state['sessions'][current_session]
    for role, text in chat_history:
        if role == "You":
            st.markdown(f"<div class='you-message'>{role}: {text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>{role}: {text}</div>", unsafe_allow_html=True)
else:
    st.write("No session selected. Start a new session to chat.")
# File Uploader for Batch Processing
uploaded_file = st.file_uploader("Choose a text file with questions", type="txt")
if uploaded_file is not None and current_session:
    questions = uploaded_file.read().decode("utf-8").splitlines()
    chat_history = st.session_state['sessions'][current_session]
    st.subheader("Batch Responses")
    for question in questions:
        response = get_gemini_response(question, chat_history)
        chat_history.append(("You", question))
        st.write(f"Question: {question}")
        for chunk in response:
            st.write(chunk.text)
            chat_history.append(("Bot", chunk.text))
# Upload and Inject Chat History into Context
uploaded_context_file = st.file_uploader("Upload Chat History to Use as Context", type="txt")
if uploaded_context_file is not None:
    chat_history_text = uploaded_context_file.read().decode("utf-8")
    st.session_state['context'] += "\n\n" + chat_history_text
    st.success("Chat history uploaded and added to the context successfully!")
# Download Chat History
if current_session:
    chat_history = st.session_state['sessions'][current_session]
    if chat_history:
        history_str = "\n".join([f"{role}: {text}" for role, text in chat_history])
        st.download_button(
            label="Download Chat History",
            data=history_str,
            file_name=f"{current_session}_chat_history.txt",
            mime="text/plain",
        )