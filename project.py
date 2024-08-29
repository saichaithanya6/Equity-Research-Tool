import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()
#da
#Initialization of Title and sidebar
st.title("Research tool")
st.sidebar.title("News Article URLs")

urls=[]
#Input URLs
for i in range(2):
    url= st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)
    
process_url_clicked= st.sidebar.button("Create Vectors")
file_path = "faiss_openai.pkl"

llm = OpenAI(model_name="davinci-002")
main_placefolder = st.empty()

if process_url_clicked:
    #load data from urls using loader
    loaders= UnstructuredURLLoader(urls= urls)
    data= loaders.load()
    main_placefolder.text("Data Loaded")
    #Spliting the data using separators
    text_splitter= RecursiveCharacterTextSplitter(
    chunk_size= 500,
    separators=['\n\n', '\n', '.', ',']
    )
    
    documents= text_splitter.split_documents(data)
    main_placefolder.text("Text Split Done")
    #Create Embeddings and save it to FAISS
    embeddings= OpenAIEmbeddings()
    vectorindex_openai= FAISS.from_documents(documents, embeddings)
    main_placefolder.text("Embedding Vector started")
    #Save the FAISS index to pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorindex_openai, f)

query= main_placefolder.text("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore= pickle.load(f)
            chain= RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever= vectorstore.as_retriever())
            result= chain({"question": query}, return_only_outputs=True)
            
            st.header("Answer")
            st.subheader(result["answer"])
            
            sources= result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n") 
                for source in sources_list:
                    st.write(source)