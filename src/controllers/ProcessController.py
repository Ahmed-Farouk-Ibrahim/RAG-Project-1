from .BaseController import BaseController
from .ProjectController import ProjectController
import os
# TextLoader and PyMuPDFLoader are document loaders for text and PDF files :
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter #  a utility for splitting text into chunks. 
# One of the best splitters as it respects sentences and avoid cutting the middle of a sentence
from models import ProcessingEnum 

# Class inherits from BaseController.
class ProcessController(BaseController):

    def __init__(self, project_id: str):
        super().__init__()

        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)

    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1] # Get the extension

    def get_file_loader(self, file_id: str):

        file_ext = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )

        # There are many file_extensions, they are constant so they should be stored as enumerate to be professional ==> create ProcessingEnum
        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding="utf-8") 
            # encoding="utf-8" make your app more robust & capable of handling a wide variety of text files & languages without running into encoding issues.

        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None

    def get_file_content(self, file_id: str):

        loader = self.get_file_loader(file_id=file_id)
        return loader.load()
    ''' that returned loader.load() : Langchain says that once we use loader.load(), we get a list of this file_content
            Each element in this file_content list is described as Document which contains 2 properties: page_content & metadata'''    

    def process_file_content(self, file_content: list, file_id: str,
                            chunk_size: int=100, overlap_size: int=20):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
        )

        file_content_texts = [
            rec.page_content
            for rec in file_content
        ]

        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]

        # The create_documents() method splits the provided text content into chunks based on the specified chunk_size and chunk_overlap.
        chunks = text_splitter.create_documents(
            file_content_texts,
            # We need that the metadata of the main file_content to be send each time with each chunk
            metadatas=file_content_metadata
        )

        return chunks


    

