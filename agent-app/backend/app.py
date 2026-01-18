import html
import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import csv
from datetime import datetime
import PyPDF2
import io
import io
import time
import resend

# Load environment variables
load_dotenv()

# Initialize OpenAI Client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key and "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

# Initialize Resend
resend_api_key = os.getenv("RESEND_API_KEY")
if not resend_api_key and "RESEND_API_KEY" in st.secrets:
    resend_api_key = st.secrets["RESEND_API_KEY"]

if resend_api_key:
    resend.api_key = resend_api_key

# Page Config
st.set_page_config(page_title="Product Decision Agent", page_icon="🛡️")

# --- Constants & Helper Functions ---
PROMPT_FILE = "product_decision_agent_prompt.md"
MAX_SUBMISSIONS_PER_EMAIL = 3

class RateLimiter:
    def __init__(self):
        self.usage = {}

    def check(self, email):
        count = self.usage.get(email, 0)
        return count < MAX_SUBMISSIONS_PER_EMAIL

    def increment(self, email):
        self.usage[email] = self.usage.get(email, 0) + 1

@st.cache_resource
def get_rate_limiter():
    return RateLimiter()

# Initialize Global Rate Limiter
limiter = get_rate_limiter()

def load_system_prompt():
    """Load the system prompt from file."""
    try:
        with open(PROMPT_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "You are a product decision assistant."

def extract_pdf_text(uploaded_file):
    """Extract text from uploaded PDF."""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def generate_report(context):
    """Generate the evaluation report using OpenAI."""
    system_prompt = load_system_prompt()
    
    # Append instruction to output only the report, no chat.
    system_prompt += "\n\nIMPORTANT: The user has submitted their full context. Generate the final 'Evaluation Result' report immediately based on the provided inputs. Do not ask for more info. Output strictly in the specified Markdown format. Do not use JSON code blocks, just standard Markdown."

    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is my product context for evaluation:\n{context}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating report: {e}"

def save_email_to_resend(email):
    """
    Save email to Resend Audience.
    """
    audience_id = os.getenv("RESEND_AUDIENCE_ID")
    if not audience_id and "RESEND_AUDIENCE_ID" in st.secrets:
        audience_id = st.secrets["RESEND_AUDIENCE_ID"]
        
    if not audience_id:
        print("RESEND_AUDIENCE_ID not set. Skipping contact save.")
        return False
        
    try:
        resend.Contacts.create({
            "email": email,
            "audience_id": audience_id
        })
        return True
    except Exception as e:
        print(f"Error saving contact to Resend: {e}")
        return False

def send_email(email, report_content):
    """
    Send email using Resend.
    """
    if not resend.api_key:
        st.error("Resend API Key not found. Cannot send email.")
        return False

    try:
        r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": email,
            "subject": "Your Product Decision Report 🛡️",
            "text": report_content
        })
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# --- Session State Initialization ---
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- Main App Logic ---

if not st.session_state.submitted:
    st.title("Product Decision Agent 🛡️")
    st.markdown("""
    ### Unlock the 9 Levers Framework
    Ruthlessly evaluate your product ideas to combat cognitive biases and sunk cost fallacy.
    
    **Fill out the form below to receive your comprehensive decision report via email.**
    """)
    
    with st.form("levers_form"):


        st.subheader("The Basics")
        problem_solution = st.text_area("Problem & Solution", placeholder="What is the problem? How do you solve it?", height=100)
        
        st.subheader("High Impact Levers (3x)")
        market_window = st.text_area("1. Market Window (Timing)", placeholder="Why now? Is the window closing? (Regulation, competitor launch, etc.)")
        strategic_moat = st.text_area("2. Strategic Moat", placeholder="Defensible advantage? Patents? Exclusive data?")
        distribution = st.text_area("3. Distribution Edge", placeholder="Do you have an audience or signed partners?")
        
        st.subheader("Medium Impact Levers (2x)")
        col1, col2 = st.columns(2)
        with col1:
            conviction = st.text_area("4. Conviction Level", placeholder="What are you sacrificing? (Money, Job?)")
            option_value = st.text_area("5. Option Value", placeholder="What else does this unlock if it fails?")
            validation = st.text_area("6. External Validation", placeholder="Who has said 'Shut up and take my money'?")
        with col2:
            regulatory = st.text_area("7. Regulatory Ease", placeholder="Any legal barriers?")
            alternatives = st.text_area("8. Pipeline Alternatives", placeholder="Is this the best idea you have right now?")
        
        st.subheader("Penalty Lever (-1x)")
        sunk_cost = st.text_area("9. Sunk Cost Bias", placeholder="Are you doing this just because you already spent time/money?")
        
        st.subheader("Documents")
        uploaded_file = st.file_uploader("Upload Pitch Deck or Detailed Notes (PDF)", type=["pdf"])
        
        st.subheader("Send The Report To")
        email_input = st.text_input("Email Address", placeholder="you@example.com")
        
        submitted = st.form_submit_button("Generate Report")
    
    if submitted:
        if not email_input or "@" not in email_input:
            st.error("Please enter a valid email address.")
        elif not limiter.check(email_input):
            st.error(f"⚠️ Limit reached. You can only generate {MAX_SUBMISSIONS_PER_EMAIL} reports with this email in the demo.")
        else:
            # Increment usage immediately
            limiter.increment(email_input)
            
            with st.spinner("Analyzing your idea... this may take a moment."):
                full_context = f"""
# Product Context

## Problem & Solution
{problem_solution}

## 9 Levers Evidence
1. Market Window: {market_window}
2. Strategic Moat: {strategic_moat}
3. Distribution: {distribution}
4. Conviction: {conviction}
5. Option Value: {option_value}
6. Validation: {validation}
7. Regulatory: {regulatory}
8. Alternatives: {alternatives}
9. Sunk Cost: {sunk_cost}
"""
                if uploaded_file:
                    file_text = extract_pdf_text(uploaded_file)
                    full_context += f"\n\n## Uploaded Document Content\n{file_text}\n\n"
                
                # 1. Generate Report
                report = generate_report(full_context)
                
                # 2. Save Email (Resend only)
                save_email_to_resend(email_input)
                
                # 3. Send Email
                send_email(email_input, report)
                
                st.session_state.submitted = True
                st.rerun()

else:
    # Success Screen
    st.title("Report Sent! 🚀")
    st.success("Your detailed Product Decision Report has been sent to your email.")
    st.info("Check your inbox (and spam folder) for the 9 Levers analysis.")
    
    if st.button("Start New Analysis"):
        st.session_state.submitted = False
        st.rerun()

# --- Debug Section ---
with st.sidebar:
    st.divider()
    st.caption("DEBUG: Rate Limiter State")
    st.json(limiter.usage)

