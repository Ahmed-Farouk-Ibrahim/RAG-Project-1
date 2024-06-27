from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):  # Inherits from BaseController. This means it has access to all methods & attributes of BaseController.
    
    def __init__(self):
        super().__init__()

    # get_project_path() is designed to generate and ensure the existence of a directory for a given project. 
    # It takes a project_id as an argument and constructs a directory path based on this ID. If the directory does not already exist, it creates it.
    def get_project_path(self, project_id: str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )
        
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir

    
