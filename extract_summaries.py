import os
import subprocess

def extract_text_from_pdf(pdf_path):
    try:
        # Extract first 3 pages for Abstract/Intro
        result_start = subprocess.run(['pdftotext', '-f', '1', '-l', '3', pdf_path, '-'], capture_output=True, text=True)
        text_start = result_start.stdout
        
        # Extract last 2 pages for Conclusion
        # We don't know the page count, so we can't easily specify -f last_page.
        # But pdftotext without -f/-l extracts everything. That might be too much.
        # Let's just extract everything and slice in python? No, too slow/memory heavy for 50 files?
        # Actually, pdftotext is fast. Let's try extracting everything and taking head/tail.
        
        result_all = subprocess.run(['pdftotext', pdf_path, '-'], capture_output=True, text=True)
        full_text = result_all.stdout
        
        if not full_text:
            return "No text extracted"

        # Simple heuristic to find Abstract and Conclusion
        abstract = ""
        conclusion = ""
        
        # Look for Abstract
        lower_text = full_text.lower()
        abs_idx = lower_text.find('abstract')
        if abs_idx != -1:
            abstract = full_text[abs_idx:abs_idx+1500] # Take 1500 chars after "Abstract"
        else:
            abstract = full_text[:1500] # Fallback to start of file
            
        # Look for Conclusion
        conc_idx = lower_text.rfind('conclusion')
        if conc_idx != -1:
            conclusion = full_text[conc_idx:conc_idx+1500]
        else:
            conclusion = full_text[-1500:] # Fallback to end of file
            
        return f"--- ABSTRACT ---\n{abstract}\n\n--- CONCLUSION ---\n{conclusion}"
        
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def main():
    directory = "/home/ssg/Documentos/ANH951_H2_storage/h2-storage/02_research/articulos"
    output_file = "extracted_summaries.txt"
    
    with open(output_file, "w") as outfile:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".pdf"):
                filepath = os.path.join(directory, filename)
                print(f"Processing {filename}...")
                extracted = extract_text_from_pdf(filepath)
                
                outfile.write(f"### FILE: {filename}\n")
                outfile.write(extracted)
                outfile.write("\n\n" + "="*50 + "\n\n")

if __name__ == "__main__":
    main()
