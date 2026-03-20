from fpdf import FPDF
import os

# Make sure this folder exists
CERT_FOLDER = "certificates"
os.makedirs(CERT_FOLDER, exist_ok=True)

def generate_certificate(name, skill):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 40, "Certificate of Completion", ln=True, align="C")

    pdf.set_font("Arial", "", 18)
    pdf.ln(20)
    pdf.multi_cell(0, 10, f"This certificate is proudly presented to {name}", align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"For successfully completing the skill assessment in {skill}", align="C")
    pdf.ln(20)
    pdf.multi_cell(0, 10, "Congratulations!", align="C")

    # Save PDF
    filename = f"{name}_certificate.pdf"
    path = os.path.join(CERT_FOLDER, filename)
    pdf.output(path)

    return path
