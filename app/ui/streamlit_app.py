import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Support System", layout="wide")

# -----------------------------
# Sidebar (Business Context)
# -----------------------------
st.sidebar.title("⚙️ System Overview")
st.sidebar.markdown("""
**Autonomous AI System**
- Multi-Agent Orchestration (LangGraph)
- Support + Fraud + Retention
- RAG + Memory Enabled

**Business Impact**
- ⏱ Faster response time  
- 🤖 Reduced manual effort  
- 🛡 Fraud detection  
- 💰 Retention optimization  
""")

# -----------------------------
# Title
# -----------------------------
st.title("🤖 Autonomous Customer Support Platform")
st.caption("AI-powered support • fraud detection • retention intelligence")

# -----------------------------
# Chat State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Layout
# -----------------------------
col_chat, col_insights = st.columns([2, 1])


user_id = st.selectbox(
    "Select User",
    [f"user_{i}" for i in range(1, 101)]
)

# -----------------------------
# Chat Section
# -----------------------------
with col_chat:
    st.subheader("💬 Customer Interaction")

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask about refunds, returns, issues...")

    if user_input:
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Call API
        response = requests.post(
            API_URL,
            json={"user_id": "demo", "message": user_input}
        )

        if response.status_code == 200:
            result = response.json()

            bot_response = result.get("response")

            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response,
                "meta": result
            })

            st.rerun()
        else:
            st.error("API error")

# -----------------------------
# Insights Panel
# -----------------------------
with col_insights:
    st.subheader("📊 AI Insights")

    if st.session_state.messages:
        last_msg = st.session_state.messages[-1]

        if last_msg["role"] == "assistant":
            meta = last_msg.get("meta", {})

            st.markdown("### 🔍 Decision Engine")

            st.metric("Intent", meta.get("intent"))
            st.metric("Route", meta.get("route"))

            fraud_score = meta.get("fraud_score", 0)
            decision = meta.get("fraud_decision", "unknown")

            st.markdown("### 🛡 Fraud Risk Analysis")

            if decision == "block":
                st.error(f"🚨 BLOCKED ({fraud_score})")
            elif decision == "review":
                st.warning(f"⚠️ Needs Review ({fraud_score})")
            else:
                st.success(f"✅ Approved ({fraud_score})")

            st.markdown("---")

            st.markdown("### 🧠 System Behavior")
            st.write("✔ Context-aware response")
            st.write("✔ Policy-grounded answer")
            st.write("✔ Multi-agent routing")

    else:
        st.info("Ask a question to see AI insights")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built with FastAPI • LangGraph • Azure OpenAI • RAG")