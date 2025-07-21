import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
from pathlib import Path
from quotation import generate_quotation_pdf  # Your custom PDF generator
from chatbot import setup_chatbot  # Your custom LangChain/ChromaDB chatbot

# --- Page Configuration ---
st.set_page_config(page_title="SNDK Meta Quotation Generator", layout="wide")
st.title("Sai Nandhini Digital Kingdom")
st.subheader("Meta Advertising Package Quotation Generator")

# --- Sidebar for Chatbot ---
st.sidebar.title("SNDK - Meta Quote Chatbot")
# Placeholder for RAG chatbot integration (see next section)
chatbot_placeholder = st.sidebar.empty()
user_input = st.sidebar.text_input("Ask about Meta Quote packages:")
if user_input:
    response = "RAG chatbot response will go here. Connect to chatbot.py for full implementation."
    st.sidebar.write(response)

# --- Main Form ---
with st.form("quotation_form"):
    st.header("Client Information")
    client_name = st.text_input("Client Name", key="client_name")
    business_name = st.text_input("Business Name", key="business_name")
    location = st.text_input("Location", key="location")

    st.header("Package Selection")
    package_type = st.radio("Package Type", ["Limited", "Unlimited"], key="package_type")
    duration = st.selectbox("Package Duration", ["1 Month", "3 Months", "6 Months", "12 Months"], key="duration")
    advance_date = st.date_input("50% Advance Payment Confirmation Date", key="advance_date")

    submitted = st.form_submit_button("Generate Quotation & Summary")

if submitted:
    # --- Validate Inputs ---
    if not all([client_name, business_name, location, advance_date]):
        st.error("Please fill in all fields.")
        st.stop()

    # --- Business Logic ---
    if package_type == "Limited" and duration != "1 Month":
        st.error("Limited package is only available for 1 Month.")
        st.stop()

    # --- Calculate Dates and Pricing ---
    months = int(duration.split()[0])
    start_date = advance_date
    end_date = start_date + relativedelta(months=+months)
    
    if package_type == "Limited":
        price = 10000
        campaign_limit = "2-3 campaigns only"
    else:
        price_map = {"1 Month": 25000, "3 Months": 70000, "6 Months": 140000, "12 Months": 280000}
        price = price_map[duration]
        campaign_limit = "Unlimited campaigns, ad sets, ad copies"

    # --- Payment Schedule ---
    advance_amount = price // 2
    due_dates = []
    if months > 1:
        due_dates.append((start_date + relativedelta(months=+1), advance_amount // 2))
        if months > 3:
            due_dates.append((start_date + relativedelta(months=+3), advance_amount // 2))

    # --- WhatsApp-Style Summary ---
    st.subheader("Quotation Summary (WhatsApp Format)")
    summary = f"""Dear {client_name},
{business_name}
{location}
Your {duration} package activated.
✅ {duration} Package – Meta Advertising
✅ Total Package Amount: ₹{price:,}/-
✅ Advance Payment: ₹{advance_amount:,}/- on {start_date.strftime('%d-%b-%Y')}
👉🏻 Meta Platforms – Advertisement
✅ {campaign_limit}
✅ Posters/Videos for advertisement campaign purpose only
❗ Ad Cost – Minimum ₹500 per day (Not included in the package. To be maintained separately by client)
(Advertisement Video shooting / Voice Over not included)
✅ Start Date: {start_date.strftime('%d-%b-%Y')}
✅ End Date: {end_date.strftime('%d-%b-%Y')}"""
    for idx, (due_date, due_amount) in enumerate(due_dates, 1):
        summary += f"\n✅ {idx}st Due: ₹{due_amount:,} on {due_date.strftime('%d-%b-%Y')}"
    summary += "\nThank You\nAuto Chat\nSai Nandhini Digital Kingdom"
    st.text_area("Copy this message for client:", value=summary, height=200)

    # --- PDF Generation ---
    pdf_data = {
        "client_name": client_name,
        "business_name": business_name,
        "location": location,
        "package_type": package_type,
        "duration": duration,
        "start_date": start_date.strftime('%d-%b-%Y'),
        "end_date": end_date.strftime('%d-%b-%Y'),
        "price": f"₹{price:,}/-",
        "advance_amount": f"₹{advance_amount:,}/-",
        "advance_date": start_date.strftime('%d-%b-%Y'),
        "campaign_limit": campaign_limit,
        "due_dates": due_dates,
        "agency_address": "3/81, Kaveri Main St, SRV Nagar, Thirunagar, Madurai - 625006",
        "agency_phone": "9600900965",
        "agency_email": "support@sainandhini.com",
        "agency_website": "www.sainandhini.com",
        # Add more fields as needed
    }
    pdf_path = generate_quotation_pdf(pdf_data)
    with open(pdf_path, "rb") as f:
        st.download_button("Download Quotation PDF", f, file_name=f"SNDK_Quotation_{client_name.replace(' ','_')}.pdf")

# --- Custom PDF Generator (quotation.py) ---
# See next section for sample code

# --- Custom Chatbot (chatbot.py) ---
# See next section for sample integration

# --- Footer ---
st.markdown("""
---
**Sai Nandhini Digital Kingdom**  
3/81, Kaveri Main St, SRV Nagar, Thirunagar, Madurai - 625006  
+91 96009 00965 | support@sainandhini.com | www.sainandhini.com
""")
