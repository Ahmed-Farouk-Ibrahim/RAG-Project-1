from helpers.config import get_settings, Settings
import os
import random
import string

# BaseController : This is a base class that provides common functionality for other controllers.
class BaseController:
    
    # Constructor Method Initialization : Sets up application settings and common directories.    
    def __init__(self):
        # get_settings() is a .config function returns instances of ...
        # (( APP_NAME , APP_VERSION , OPENAI_API_KEY , FILE_ALLOWED_TYPES , FILE_MAX_SIZE , FILE_DEFAULT_CHUNK_SIZE ))
        self.app_settings = get_settings()
        
        # Determines the base directory of the project by taking the directory name of the parent directory of the current file.
        self.base_dir = os.path.dirname( os.path.dirname(__file__) ) # os.path.dirname(__file__)=parent dir of this BaseController.py
        '''__file__: This is a special variable in Python that contains the path to the current file. 
        In this case, it would be the path to BaseController.py.

        os.path.dirname(__file__): This gets the directory containing the current file (BaseController.py). 
        If BaseController.py is in src/controllers, this would be src/controllers.

        os.path.dirname(os.path.dirname(__file__)): This goes one level up from the directory containing the current file. 
        If BaseController.py is in src/controllers, this would resolve to src. 
        Therefore, self.base_dir is set to the path of the src directory.'''

        # Path to the assets/files directory within src. It is constructed by joining self.base_dir with assets/files.
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
        
    # Generate a random string of the specified length (default is 12 characters), useful method for creating unique identifiers.    
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
