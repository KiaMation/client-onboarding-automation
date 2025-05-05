import json
import sys
from fpdf import FPDF

def generate_pdf(data):
    try:
        payload = json.loads(data)
        client_data = payload["client_payload"]
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt=f"Client Agreement", ln=1, align='C')
        pdf.cell(200, 10, txt=f"Client: {client_data['name']}", ln=1)
        pdf.cell(200, 10, txt=f"Email: {client_data['email']}", ln=1)
        pdf.cell(200, 10, txt=f"Plan: {client_data['plan']}", ln=1)
        
        filename = f"contract_{client_data['email'].split('@')[0]}.pdf"
        pdf.output(filename)
        return filename
        
    except Exception as e:
        print(f"PDF generation failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = f.read()
    else:
        data = sys.stdin.read()
    generate_pdf(data)
