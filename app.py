import streamlit as st
import fitz

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Contract Review Bot",
    layout="wide",
    page_icon="📄"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #ffffff;
}
.stTextArea textarea {
    background-color: #1e293b !important;
    color: white !important;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}
.risk-high {
    color: white;
    background-color: #dc2626;
    padding: 6px 10px;
    border-radius: 8px;
}
.risk-medium {
    color: white;
    background-color: #f59e0b;
    padding: 6px 10px;
    border-radius: 8px;
}
.risk-safe {
    color: white;
    background-color: #16a34a;
    padding: 6px 10px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.title("📘 About")
    st.markdown("""
    **AI Contract Review Bot**

    🔍 Extract key clauses  
    ⚠ Detect risk flags  
    📝 Generate plain summary  

    Designed for business automation.
    """)

# ---------------- TITLE ---------------- #

st.title("📄 AI Contract & Document Review Bot")
st.markdown("Upload a contract or paste text below to analyze clauses and risks.")

# ---------------- PDF EXTRACTION ---------------- #

def extract_text_from_pdf(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

# ---------------- MOCK LLM ---------------- #

def mock_llm_analysis(contract_text):
    text = contract_text.lower()

    parties = "Not Found"
    if "between" in text:
        try:
            parties = contract_text.split("between")[1].split(".")[0].strip()
        except:
            parties = "Parties mentioned but unclear"

    duration = "Duration detected" if "month" in text or "year" in text else "Not Found"
    payment_terms = "Payment clause detected" if "₹" in contract_text or "payment" in text else "Not Found"
    termination_clause = "Termination clause detected" if "terminate" in text else "Not Found"
    renewal_terms = "Auto-renewal clause detected" if "auto-renew" in text else "Not Found"

    auto_renewal_risk = "Contract auto-renews. Review carefully." if "auto-renew" in text else "Not Found"
    liability_risk = "Liability clause detected. Check exposure." if "liability" in text or "indemnify" in text else "Not Found"
    missing_exit_clause = "No clear exit clause found." if "termination" not in text else "Not Found"

    summary = "This contract outlines commercial terms including duration, payment, renewal, and termination. Review highlighted risks before signing."

    return {
        "parties": parties,
        "duration": duration,
        "payment_terms": payment_terms,
        "termination_clause": termination_clause,
        "renewal_terms": renewal_terms,
        "risk_flags": {
            "auto_renewal_trap": auto_renewal_risk,
            "liability_risk": liability_risk,
            "missing_exit_clause": missing_exit_clause
        },
        "plain_english_summary": summary
    }

# ---------------- INPUT ---------------- #

uploaded_file = st.file_uploader("Upload Contract PDF", type=["pdf"])
raw_text = st.text_area("OR Paste Contract Text Here")

# ---------------- ANALYZE ---------------- #

if st.button("Analyze Contract", use_container_width=True):

    if uploaded_file:
        contract_text = extract_text_from_pdf(uploaded_file)
    elif raw_text:
        contract_text = raw_text
    else:
        st.warning("Please upload or paste contract text.")
        st.stop()

    with st.spinner("Analyzing contract..."):
        result = mock_llm_analysis(contract_text)

    st.success("Analysis Complete")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"<div class='card'><h3>👥 Parties</h3>{result['parties']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><h3>📅 Duration</h3>{result['duration']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><h3>💰 Payment Terms</h3>{result['payment_terms']}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div class='card'><h3>🚪 Termination</h3>{result['termination_clause']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><h3>🔁 Renewal</h3>{result['renewal_terms']}</div>", unsafe_allow_html=True)

    st.subheader("⚠ Risk Flags")

    risks = result["risk_flags"]

    if risks["auto_renewal_trap"] != "Not Found":
        st.markdown(f"<span class='risk-high'>Auto Renewal Risk</span> {risks['auto_renewal_trap']}", unsafe_allow_html=True)

    if risks["liability_risk"] != "Not Found":
        st.markdown(f"<span class='risk-medium'>Liability Risk</span> {risks['liability_risk']}", unsafe_allow_html=True)

    if risks["missing_exit_clause"] != "Not Found":
        st.markdown(f"<span class='risk-medium'>Missing Exit Clause</span> {risks['missing_exit_clause']}", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"<div class='card'><h3>📝 Plain English Summary</h3>{result['plain_english_summary']}</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Built by Srikanth Gudla | AI Engineer Hiring Task MVP")