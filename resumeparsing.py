@ -0,0 +1,44 @@
import os
import mysql.connector
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_and_store_text_from_pdfs(directory):
    db_connection = mysql.connector.connect(
        host="your_hostname",  
        user="your_username",  
        password="your_password",  
        database=database_name  
    )
    
    cursor = db_connection.cursor()

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):  
            pdf_path = os.path.join(directory, filename)
            print(f"Extracting text from: {filename}")
            text = extract_text_from_pdf(pdf_path)
            
            query = "INSERT INTO pdf_extracted_content (filename, content) VALUES (%s, %s)"
            values = (filename, text)
            cursor.execute(query, values)
            db_connection.commit()  

    cursor.close()
    db_connection.close()

pdf_directory = 'assets/pdf'

extract_and_store_text_from_pdfs(pdf_directory)

print("Text extraction and database insertion completed.")
