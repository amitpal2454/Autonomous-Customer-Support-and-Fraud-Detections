import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Support System", layout="wide")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.markdown("## 🤖 Autonomous AI System")

st.sidebar.markdown("""
### ⚙️ Capabilities
- 🧠 Multi-Agent AI  
- 🎯 Intent Detection  
- 🛡 Fraud Detection  
- 📚 Policy Validation  

---

### 💼 Business Impact
- ⏱ Faster Support  
- 🤖 Reduced Manual Work  
- 🛡 Risk Detection  
- 💰 Retention Ready  
""")

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Customer Support Platform")
st.caption("Autonomous Support • Fraud Detection • Smart Decisions")

# -----------------------------
# User Selector
# -----------------------------
user_id = st.selectbox(
    "👤 Select User",
    [f"user_{i}" for i in range(1, 101)]
)

# -----------------------------
# Layout
# -----------------------------
col_chat, col_insight = st.columns([2, 1])

# -----------------------------
# Chat Section
# -----------------------------
with col_chat:
    st.subheader("💬 Customer Interaction")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # 🖼 Image Upload
    uploaded_file = st.file_uploader("📸 Upload product image (optional)", type=["jpg", "png"])

    user_input = st.chat_input("Describe your issue...")

    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        files = None
        if uploaded_file:
            files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            API_URL,
            json={
                "user_id": user_id,
                "message": user_input
            }
        )

        if response.status_code == 200:
            result = response.json()

            st.session_state.messages.append({
                "role": "assistant",
                "content": result.get("response"),
                "meta": result
            })

            st.rerun()
        else:
            st.error("API Error")

# -----------------------------
# Insights Panel
# -----------------------------
with col_insight:
    st.subheader("📊 AI Insights")

    if st.session_state.messages:
        last = st.session_state.messages[-1]

        if last["role"] == "assistant":
            meta = last.get("meta", {})

            # 🎯 Intent with emoji
            intent = meta.get("intent")

            intent_icon = {
                "refund": "💸",
                "complaint": "⚠️",
                "inquiry": "❓"
            }.get(intent, "🔎")

            st.markdown("### 🎯 Intent")
            st.markdown(f"{intent_icon} **{intent}**")

            # 🛡 Fraud Score
            fraud_score = meta.get("fraud_score", 0)
            decision = meta.get("fraud_decision")

            st.markdown("### 🛡 Fraud Risk")

            if decision == "block":
                st.error(f"🚨 BLOCKED ({fraud_score})")
            elif decision == "review":
                st.warning(f"⚠️ REVIEW ({fraud_score})")
            else:
                st.success(f"✅ APPROVED ({fraud_score})")

            # 🧠 Fraud Reasons
            st.markdown("### 🧠 Why this decision?")
            reasons = meta.get("fraud_reason", [])

            if reasons:
                for r in reasons:
                    st.write(f"• {r}")
            else:
                st.write("No risk signals detected")

            # 🤖 LLM Explanation
            st.markdown("### 🤖 AI Explanation")
            st.write(meta.get("fraud_explanation", "No explanation"))

            # 🧠 Issue Detection (Object-like classification)
            st.markdown("### 📦 Issue Detected")
            st.write(meta.get("issue_type", "Not detected"))

    else:
        st.info("Start conversation to see insights")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Powered by LangGraph • Azure OpenAI • RAG • Fraud Intelligence")