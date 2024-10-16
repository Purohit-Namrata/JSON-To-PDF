import json
from fpdf import FPDF 
#from fpdf import FPDF

def json_to_pdf(json_path, pdf_path):
    # Read JSON file
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Convert JSON data to a pretty printed string
    json_str = json.dumps(data, indent=4)  #converts python object(like a dictionarty to JSON formatted string)
    
    # Create a PDF instance
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Split the string into lines
    lines = json_str.split('\n')
    
    # Add each line to the PDF
    for line in lines:
        pdf.multi_cell(0, 10, line)
    
    # Save the PDF to the specified path
    pdf.output(pdf_path)

# Usage example
json_path = 'C:/Users/BLAUPLUG/Documents/Python_programs/JSONtoPDF/Emp_data.json'
pdf_path = 'C:/Users/BLAUPLUG/Documents/Python_programs/JSONtoPDF/Emp_data.pdf'
json_to_pdf(json_path, pdf_path)