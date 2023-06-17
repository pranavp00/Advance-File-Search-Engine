import os
import glob
import textract
from PyPDF2 import PdfReader
from thefuzz import fuzz




def collecting_files(root_dir, query):
    
    files = [f for f in glob.glob(os.path.join(root_dir, '**'), recursive=True) if os.path.isfile(f)]

    matches = []
   
    for f in files:
        percentage = search_file(f,query)
        if  percentage != None:
            matches.append({'file_path': f,'percentage_type':percentage})
    
    return matches



def open_file(file_path):
    
    
    try: 
        if file_path.endswith('.pdf'):
            reader = PdfReader(file_path)
            no_of_pages = len(reader.pages)
            text = ''
            for i in range(no_of_pages):
                page = reader.pages[i]
                text += page.extract_text()
            
            return text.lower()
        
        else:
            x = textract.process(file_path).decode().lower()
            
            return x
        
    
    except:
        
        return ""


def search_file(file_path, query):
    
    
    done = False
    
    if query.lower() in os.path.basename(file_path):
        done = True
        return 'filename'
    if done == False:
        content = open_file(file_path)
        if content == "": 
            return
        content_ratio = fuzz.token_set_ratio(query, open_file(file_path))
        if content_ratio > 50:
            done = True
            return content_ratio
    else:
        return None
    


    
def preparing_matches(root_dir,query):
    
    match_list = collecting_files(root_dir,query)
    file_list = [d for d in match_list if d['percentage_type'] == 'filename']
    content_list = sorted([d for d in match_list if d['percentage_type'] != 'filename'], key=lambda x: x['percentage_type'], reverse=True)
    result = file_list + content_list
    return result

