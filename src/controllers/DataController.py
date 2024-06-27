from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile  # to handle uploaded files.
from models import ResponseSignal  # provides constants for different response signals.
import re
import os

# This class is responsible for handling data-related operations, particularly validating and managing uploaded files.
class DataController(BaseController):  # Inherits from BaseController. This means it has access to all methods & attributes of BaseController.
    
    def __init__(self):
        super().__init__()  # Call the parent's constructor ( BaseController init() )
        self.size_scale = 1048576 # convert MB to bytes as we will need with FILE_MAX_SIZE


    def validate_uploaded_file(self, file: UploadFile):
        # This method checks the validity of an uploaded file. It returns a tuple where the second element is a ResponseSignal value.
        # we have 3 cases, each case we needs True/False & the cause. But the cause should be stored as enumerate to be professional
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value # .value Bkz it's enumeration
        
        # file.size returns size with Byte, whereas we defined FILE_MAX_SIZE with MegaByte, so we multiply by 1048576
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value

    # Generating a Unique File Path
    def generate_unique_filepath(self, orig_file_name: str, project_id: str):
        # generate_random_string() from BaseController: Generate a random string to ensure the filename is unique.
        random_key = self.generate_random_string()

        # Get the project directory path using ProjectController.
        project_path = ProjectController().get_project_path(project_id=project_id)
        # Clean the original file name to remove special characters.
        cleaned_file_name = self.get_clean_file_name(
            orig_file_name=orig_file_name
        )

        # Combine the project path, random key, and cleaned file name.
        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )

        # Ensure the generated file path is unique by checking if it exists and regenerating if necessary.
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_file_name
            )

        return new_file_path, random_key + "_" + cleaned_file_name

    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name


