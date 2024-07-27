from PyPDF4 import PdfFileMerger
import os

def merge_pdfs():
    try:
        merger = PdfFileMerger()
        pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]

        if not pdf_files:
            print("No PDF files found to merge.")
            return

        print(f"Found {len(pdf_files)} PDF files: {pdf_files}")
        for pdf in pdf_files:
            try:
                print(f"Appending {pdf}...")
                merger.append(pdf)
            except Exception as e:
                print(f"Error appending {pdf}: {e}")

        try:
            merger.write("final_pdf.pdf")
            merger.close()
            print("Merged PDF created successfully: final_pdf.pdf")
        except Exception as e:
            print(f"Error writing final PDF: {e}")

    except Exception as e:
        print(f"Error during PDF merging: {e}")

def remove_original_pdfs():
    try:
        pdf_files = [file for file in os.listdir() if file.endswith('.pdf') and file != 'final_pdf.pdf']

        if not pdf_files:
            print("No original PDF files to remove.")
            return

        for pdf in pdf_files:
            try:
                print(f"Removing {pdf}...")
                os.remove(pdf)
            except Exception as e:
                print(f"Error removing {pdf}: {e}")

        print("Original PDFs removed successfully.")
    except Exception as e:
        print(f"Error during PDF removal: {e}")

if __name__ == "__main__":
    try:
        print("Starting PDF merge process...")
        merge_pdfs()
        print("Starting original PDF removal process...")
        remove_original_pdfs()
    except Exception as e:
        print(f"Error in main execution: {e}")
