from fpdf import FPDF  

def generate_pdf(name, plan):  
    pdf = FPDF()  
    pdf.add_page()  
    pdf.set_font("Arial", size=12)  
    pdf.cell(200, 10, txt=f"Client: {name}", ln=1)  
    pdf.cell(200, 10, txt=f"Plan: {plan}", ln=1)  
    pdf.output(f"{name}_contract.pdf")  
    return pdf  
