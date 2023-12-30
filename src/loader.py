import os
from langchain.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader

#########################################
def document_loader(file):

    file_path = os.path.join("./", file.name)
    _, extension = os.path.splitext(file_path)

    with open(file_path, 'wb') as f:
        f.write(file.read())

    if extension == '.pdf':
        loader = PyPDFLoader(file_path) 
    elif extension == '.txt':
        loader = TextLoader(file_path)
    elif extension == '.docx':
        loader = Docx2txtLoader(file_path)
    else:
        st.error("Unsupported file type.")
        return None
    
    return loader.load()
###############################################
def process_documents(files):
    documents = []
    for file in files:

        documents += document_loader(file=file)

    return documents
#############################################
