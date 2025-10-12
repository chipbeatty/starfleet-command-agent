import streamlit as st
from src.agents.graph import starfleet_agent

# Page config
st.set_page_config(
    page_title="Starfleet Command Assistant",
    page_icon="🖖",
    layout="wide"
)

# Custom CSS for Star Trek LCARS theme
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    .stChatMessage {
        background-color: #1a1a2e;
        border-left: 4px solid #ff9966;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    h1 {
        color: #ff9966;
        font-family: 'Arial', sans-serif;
    }
    .stChatInput {
        background-color: #1a1a2e;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🖖 Starfleet Command Assistant")
st.caption("USS Enterprise NCC-1701 • Main Computer Interface")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.thread_id = "streamlit-session-001"

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Enter command..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                response = starfleet_agent.invoke(
                    {"messages": [("user", prompt)]},
                    config={"configurable": {"thread_id": st.session_state.thread_id}}
                )
                
                agent_response = response["messages"][-1].content
                st.markdown(agent_response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": agent_response
                })
                
            except Exception as e:
                st.error(f"System error: {e}")

# Sidebar with info
with st.sidebar:
    st.header("System Status")
    st.success("🟢 All systems operational")
    
    st.header("Available Systems")
    st.markdown("""
    - 🔍 Stellar Cartography Database
    - 🧮 Engineering Computer Core
    - 📝 Mission Log System
    """)
    
    st.header("Current Session")
    st.info(f"Thread ID: {st.session_state.thread_id}")
    st.info(f"Messages: {len(st.session_state.messages)}")
    
    if st.button("🔄 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()