from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def generate_quotation_pdf(data):
    """
    Generate a Meta Platforms Quotation PDF for Sai Nandhini Digital Kingdom.
    :param data: dict containing all required client and package data
    :return: Path to the output PDF file
    """

    # Setup output path
    os.makedirs("output_pdfs", exist_ok=True)
    pdf_path = f"output_pdfs/SNDK_Quotation_{data['client_name'].replace(' ', '_')}.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    elements = []

    # --- Styles ---
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontSize=20,
        leading=28,
        alignment=1,
        spaceAfter=12,
        textColor=colors.HexColor("#1769aa")  # Your brand blue
    )
    heading_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        spaceAfter=10,
        textColor=colors.HexColor("#1769aa")
    )
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=11,
        leading=15,
        spaceAfter=8,
        textColor=colors.black
    )

    # --- Header: Logo and Address ---
    brand_logo_path = "static/logo.png"
    if os.path.exists(brand_logo_path):
        logo = Image(brand_logo_path, width=2.3*inch, height=0.8*inch)
        elements.append(logo)
        elements.append(Spacer(1, 0.05*inch))
    # Agency Name and Address
    elements.append(Paragraph("<b>Sai Nandhini Digital Kingdom</b>", title_style))
    elements.append(Paragraph(
        "3/81, Kaveri Main St, SRV Nagar, Thirunagar, Madurai - 625006<br/>"
        "96009 00965 | support@sainandhini.com | www.sainandhini.com",
        normal_style
    ))
    elements.append(Spacer(1, 0.25*inch))

    # --- Quotation Title ---
    elements.append(Paragraph("<b>Q u o t a t i o n</b>", heading_style))
    elements.append(Spacer(1, 0.15*inch))

    # --- Client Info and Package Summary Table ---
    summary_data = [
        ["Client Name", data["client_name"]],
        ["Business Name", data["business_name"]],
        ["Location", data["location"]],
        ["Package Type", data["package_type"]],
        ["Package Duration", data["duration"]],
        ["Start Date", data["start_date"]],
        ["End Date", data["end_date"]],
        ["Total Package Amount", data["price"]],
        ["Advance Payment", f"{data['advance_amount']} on {data['advance_date']}"],
    ]
    client_table = Table(summary_data, colWidths=[2.2*inch, 4*inch])
    client_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e7f0fa")),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor("#f5f5f5")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(client_table)
    elements.append(Spacer(1, 0.15*inch))

    # --- Meta Platforms - Advertisement Package Title ---
    elements.append(Paragraph("<b>META PLATFORMS - ADVERTISEMENT PACKAGE</b>", heading_style))

    # --- Package Inclusions ---
    elements.append(Paragraph("<b>Deliverables & Inclusions:</b>", heading_style))
    inclusions = [
        f"• {data['campaign_limit']}",
        "• Ad sets, Ads, Posters, Videos",
        "• Leads Automation, Audience Retargeting",
        "• Posters/Videos for advertisement campaign purpose only",
        "• Minimum Ad Cost: ₹500 per day (Not included; to be maintained by client)",
        "• (Advertisement Video shooting/Voice Over not included)",
    ]
    for item in inclusions:
        elements.append(Paragraph(item, normal_style))

    # --- Payment Schedule (if available) ---
    if data['due_dates']:
        elements.append(Spacer(1, 0.12*inch))
        elements.append(Paragraph("<b>Payment Schedule</b>", heading_style))
        due_data = [["Due Date", "Amount"]]
        for date, amount in data['due_dates']:
            due_data.append([date.strftime('%d-%b-%Y'), f"₹{amount:,}/-"])
        due_table = Table(due_data, colWidths=[2.3*inch, 2*inch])
        due_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f5f5f5")),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('GRID', (0, 0), (-1, -1), 0.2, colors.grey),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        ]))
        elements.append(due_table)

    # --- Meta Platforms Requirements (per July 2025 sample) ---
    elements.append(Spacer(1, 0.15*inch))
    elements.append(Paragraph("<b>Meta Platforms Requirements</b>", heading_style))
    requirements = [
        "FB Profile Setup: Company Business Page, Ad Account/Manager, Business Instagram Account, Business WhatsApp Number, Profile Ad Account.",
        "Payment Setup: Link a Credit Card or set up Prepaid Fund Loading through G Pay or QR Code scanning for the payment wallet.",
        "Brand Assets: Provide the company logo in original PNG HD format, finalize official poster theme colors, and share the basic content for advertisements and video scripts.",
        "Point of Contact: Assign a dedicated person to manage all digital marketing activities for smooth coordination."
    ]
    for req in requirements:
        elements.append(Paragraph(f"• {req}", normal_style))

    # --- Important Note (per sample) ---
    elements.append(Spacer(1, 0.13*inch))
    elements.append(Paragraph("<b>Important Note</b>", heading_style))
    notes = [
        "Project Start: The project will commence upon receipt of a 50% advance payment for 3/6/12 months package.",
        "Exclusions: Video shooting expenses are not included in the project cost and will be billed separately if required.",
        "Monthly retainer Fees: Includes campaign setup, monitoring, optimization, and reporting."
    ]
    for note in notes:
        elements.append(Paragraph(f"• {note}", normal_style))

    # --- Brand Footer / Socials ---
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph(
        "@SaiNandhiniDigitalKingdom &nbsp; &nbsp; @sainandhinidigitalkingdom",
        normal_style
    ))

    doc.build(elements)
    return pdf_path
