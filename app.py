# Write your code here
from groq import Groq
import streamlit as st

# Load the api key
api_key = st.secrets["API_KEY"]

# Load groq client
client  = Groq(api_key=api_key)

# Write a function to Generate model respose in a stream
def generate_response(query: str):
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        stream= True,
        stop= None
    )

    for chunk in completion:
        yield chunk.choices[0].delta.content or ""

# Build the streamlit app
st.set_page_config(page_title="llama Chatbot")

# Provide title to the app
st.title("llama Chatbot")
st.subheader("by Rohan Biradar")

# Provide a text area for user input
query = st.text_area("Please ask any question : ")

# Create a button
button = st.button("submit", type="primary")

# If button is pressed Generate the response
if button:
    st.subheader("Response :")
    with st.spinner("Generating..."):
        st.write_stream(generate_response(query))
        
# --- UI Enhancements ---

# Sidebar
with st.sidebar:
    st.markdown("## 🧠 About")
    st.markdown("""
    This is an interactive chatbot powered by **LLaMA-4** via **Groq API**.  
    Ask any question and get a real-time response streamed to you.

    **Tech Stack:**  
    - 🐍 Python  
    - 🦙 LLaMA 4  
    - 🔗 Groq API  
    - 📊 Streamlit
    """)

    st.markdown("---")
    st.markdown("👨‍💻 **Developer:** [Rohan Biradar](mailto:rohanbiradar438@gmail.com)")
    st.markdown("💬 Feel free to ask anything!")

# Footer
st.markdown("""
<style>
footer {visibility: hidden;}
</style>
<hr style="border:1px solid #f0f0f0; margin-top: 2em"/>
<div style="text-align: center; font-size: 0.9em;">
    Made with ❤️ using <b>Streamlit</b> & <b>Groq</b> | © 2025 Rohan Biradar
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="background-color:#007acc;padding:1.2rem;border-radius:10px">
<h1 style="color:white;text-align:center;">🤖 Welcome to LLaMA Chatbot</h1>
<p style="color:white;text-align:center;">Powered by Groq • Built with Streamlit • Crafted by Rohan Biradar</p>
</div>
""", unsafe_allow_html=True)


def chat_bubble(text, sender="bot"):
    color = "#e6f2ff" if sender == "bot" else "#d9fdd3"
    align = "left" if sender == "bot" else "right"
    st.markdown(f"""
    <div style='text-align:{align}; background-color:{color}; 
                padding: 10px; margin: 10px 0; border-radius: 10px;
                max-width: 80%; display: inline-block;'>
        {text}
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<style>
button[kind="primary"] {
    background-color: #007acc;
    color: white;
    border-radius: 10px;
    padding: 0.5em 1em;
    font-size: 16px;
}
textarea {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: flex-end;
    background-color: #f0f0f0;
    padding: 10px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
    font-size: 15px;
}
.navbar a {
    text-decoration: none;
    color: #007acc;
    margin-left: 20px;
}
.navbar a:hover {
    text-decoration: underline;
}
</style>

<div class='navbar'>
    <a href='#about'>About</a>
    <a href='mailto:rohanbiradar438@gmail.com'>Contact</a>
</div>
""", unsafe_allow_html=True)

