import os
import shutil

print(__name__)
print("prova de que isso veio daqui")

'''
def find_xml_files(base_folder):
    """Recursively find all XML files in the base folder."""
    xml_files = {}
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.xml'):
                xml_name = os.path.splitext(file)[0]
                xml_files[xml_name] = root
                print(f"Found XML: {file} in {root}")
    return xml_files

def move_pdf_to_xml_folder(pdf_folder, xml_files):
    """Move PDF files matching XML filenames to the respective XML folder."""
    for root, _, files in os.walk(pdf_folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_name = os.path.splitext(file)[0]
                if pdf_name in xml_files:
                    pdf_path = os.path.join(root, file)
                    destination_folder = xml_files[pdf_name]
                    destination_path = os.path.join(destination_folder, file)
                    
                    # Move the PDF file
                    shutil.move(pdf_path, destination_path)
                    print(f"Moved '{pdf_path}' to '{destination_path}'.")

def main():
    xml_base_folder = 'I:/.shortcut-targets-by-id/1ghlKQQOndN3wMxNW4qM3pTPDbtrYJmTa/GestorDFe/Documentos/CONSORCIO INTERMUNICIPAL DE SAUDE ALTO DAS VERTENTES'  # Update this path
    pdf_base_folder = 'C:/Users/USER/Documents/GitHub/Sakana-Tool/docs/residuo'  # Update this path
    
   
    print("Searching for XML files...")
    xml_files = find_xml_files(xml_base_folder)

    print("Searching for PDF files and moving them to matching XML folders...")    
    move_pdf_to_xml_folder(pdf_base_folder, xml_files)

    print("Process complete.")
    
if __name__ == "__main__":
    main()

### teste

'''