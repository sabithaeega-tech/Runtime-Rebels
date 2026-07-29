import streamlit as st

from workflow.langgraph_workflow import graph

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="SecureOps AI",
    page_icon="🛡️",
    layout="wide"
)
# -------------------------------
# Custom Styling
# -------------------------------
st.markdown("""
<style>

/* =========================
   Main App
========================= */

.main {
    background-color: #f4f7fb;
    color: #0f172a;
}

.stApp {
    background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
}

.title {
    color: #0f172a;
}

.highlight {
    color: #0f766e;
}

/* =========================
   Cards
========================= */

.section-card {
    background: rgba(255,255,255,0.95);
    border-radius:18px;
    padding:24px;
    border:1px solid rgba(148,163,184,0.35);
    box-shadow:0 10px 30px rgba(15,23,42,0.08);
    margin-bottom:20px;
}

.feature-box {
    background:white;
    border-radius:16px;
    padding:20px;
    box-shadow:0 8px 20px rgba(15,23,42,.08);
}

.sample-query{
    color:#334155;
    font-style:italic;
}

/* =========================
   Sidebar
========================= */

section[data-testid="stSidebar"]{
    background:#f8fafc;
}

/* ==========================================================
   CHAT INPUT
========================================================== */

/* Outer Chat Box */

div[data-testid="stChatInput"]{
    background:#F3F4F6 !important;
    border:2px solid black !important;
    border-radius:20px !important;
    padding:8px !important;
    transition:all .2s ease;
}

/* Inner Box */

div[data-testid="stChatInput"] > div{
    background:white !important;
    border-radius:16px !important;
    border:none !important;
    box-shadow:none !important;
}

/* Text Input */

div[data-testid="stChatInput"] input{
    background:white !important;
    color:black !important;
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
    font-size:16px !important;
}

/* Placeholder */

div[data-testid="stChatInput"] input::placeholder{
    color:#6b7280 !important;
}

/* Remove Red Border */

div[data-testid="stChatInput"]:focus,
div[data-testid="stChatInput"]:focus-visible,
div[data-testid="stChatInput"]:focus-within{
    border:2px solid black !important;
    outline:none !important;
    box-shadow:none !important;
}

div[data-testid="stChatInput"] > div:focus,
div[data-testid="stChatInput"] > div:focus-visible,
div[data-testid="stChatInput"] > div:focus-within{
    outline:none !important;
    box-shadow:none !important;
    border:none !important;
}

div[data-testid="stChatInput"] input:focus,
div[data-testid="stChatInput"] input:focus-visible{
    outline:none !important;
    box-shadow:none !important;
    border:none !important;
}

/* Remove Browser Focus Ring */

*:focus{
    outline:none !important;
}

*:focus-visible{
    outline:none !important;
    box-shadow:none !important;
}

/* Send Button */

div[data-testid="stChatInput"] button{
    background:#0F766E !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;
}

div[data-testid="stChatInput"] button:hover{
    background:#115E59 !important;
}

/* =========================
   Chat Messages
========================= */

div[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:10px;
}

/* =========================
   Buttons
========================= */

.stButton>button{
    background:#0F766E;
    color:white;
    border:none;
    border-radius:10px;
}

.stButton>button:hover{
    background:#115E59;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("🛡️ SecureOps AI")

    st.write(
        "Modern SOC intelligence for alerts, incidents, identity, endpoints, and reports."
    )

    st.divider()

    st.subheader("Try these questions")

    st.markdown("""
What are the top 3 active incidents?
Show suspicious endpoint behavior.
Summarize the latest security report.
Find high-risk users.
""")

    st.divider()

    st.subheader("Quick Guidance")

    st.write(
        "Type a security question below and SecureOps AI will investigate alerts, incidents, endpoints, identities and reports."
    )

# -------------------------------
# Hero Section
# -------------------------------

hero_col1, hero_col2 = st.columns([2,1])

with hero_col1:

    st.title("🛡️ SecureOps AI")

    st.markdown(
        "### <span class='highlight'>Smart security operations with instant investigation, context, and analysis.</span>",
        unsafe_allow_html=True,
    )

    st.write(
        "SecureOps AI connects alert, incident, identity, endpoint, and report data into a friendly SOC conversation."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input

    user_query = st.chat_input(
        "Type your security question here..."
    )

    if user_query:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":user_query
            }
        )

        with st.chat_message("user"):
            st.markdown(user_query)

        with st.spinner("🔍 Analyzing security data..."):

            result = graph.invoke(
                {
                    "user_query":user_query,
                    "next_agent":"",
                    "response":""
                }
            )

            assistant_response = result["response"]

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":assistant_response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(assistant_response)

# -------------------------------
# Right Card
# -------------------------------

with hero_col2:

    st.markdown("<div class='section-card'>",unsafe_allow_html=True)

    st.subheader("🚀 Instant SOC Insights")

    st.markdown("""
Context-sensitive alert review

Incident prioritization

Endpoint health monitoring

Identity risk analysis

Report summarization
""")

    st.markdown("</div>",unsafe_allow_html=True)

# -------------------------------
# Features
# -------------------------------

st.markdown("## What SecureOps AI Can Do")

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("### ⚠️ Alerts")
    st.write("Surface suspicious alerts and explain how to respond.")

with col2:
    st.markdown("### 👤 Identity")
    st.write("Review user risk and investigate identity issues.")

with col3:
    st.markdown("### 💻 Endpoints")
    st.write("Analyze endpoint activity and detect anomalies.")

st.divider()

# -------------------------------
# Examples
# -------------------------------

left,right=st.columns(2)

with left:

    st.subheader("Example Questions")

    st.markdown("""
Show recent suspicious login alerts.

What incidents are currently open?

Summarize user identity risks.

Which endpoints are compromised?
""")

with right:

    st.subheader("Ready to Investigate?")

    st.write(
        "Ask SecureOps AI anything about alerts, incidents, reports, identities and endpoints."
    )

    st.info(
        "Try: Which users have recent high-risk alerts and what should I investigate first?"
    )