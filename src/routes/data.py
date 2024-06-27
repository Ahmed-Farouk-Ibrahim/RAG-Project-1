from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
'''     status is a module from the FastAPI package that provides a set of HTTP status codes as constants. 
These constants make your code more readable and maintainable by replacing numerical status codes with descriptive names.    

Purpose and Usage
The status module includes a comprehensive set of HTTP status codes. Here are some examples of how you can use these constants:

Informational Responses:   status.HTTP_100_CONTINUE    ||   status.HTTP_101_SWITCHING_PROTOCOLS  
Successful Responses:   status.HTTP_200_OK   ||  status.HTTP_201_CREATED  ||  status.HTTP_204_NO_CONTENT
Redirection Messages:   status.HTTP_301_MOVED_PERMANENTLY   ||   status.HTTP_302_FOUND
Client Error Responses:   status.HTTP_400_BAD_REQUEST   ||  status.HTTP_401_UNAUTHORIZED   ||   status.HTTP_404_NOT_FOUND
Server Error Responses:   status.HTTP_500_INTERNAL_SERVER_ERROR   ||   status.HTTP_502_BAD_GATEWAY   
'''
from fastapi.responses import JSONResponse # JSONResponse: Used to send JSON responses with a specific HTTP status code.
import os
from helpers.config import get_settings, Settings

# We wrote in __init__.py of the directory controller that 
from controllers import DataController, ProjectController
import aiofiles # aiofiles: Library for handling asynchronous file operations and working with Chunks.
from models import ResponseSignal
import logging

# Logger: Configures a logger to log errors and messages using the Uvicorn logger.
logger = logging.getLogger('uvicorn.error')

# Create a router with a prefix of /api/v1/data and tag it with api_v1 and data.
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

# Endpoint Definition :
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
        
    
    # validate the file properties using validate_uploaded_file() function in controllers.DataController.py file.
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    # status.HTTP_400_BAD_REQUEST: This constant represents the HTTP status code 400, 
    # indicating that the server could not understand the request due to invalid syntax (e.g., an unsupported file type or file size).
    if not is_valid:
        return JSONResponse(
            # without next line, it displayed 200 in all cases, even if it was invalid it displayed 200 not 400, so we added next line:
            status_code=status.HTTP_400_BAD_REQUEST,  # status_code=400 is Accepted also
            content={
                "signal": result_signal
            }
        )

    # File Path Generation :
    # project_dir_path is the Project Directory
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    # File Upload :
    '''
    When we upload a file, it will be stored in a temporary file until it be completed then the system pass it to FastApi
      to decide based on the accompanied logic where to save. This way isn't memory effecient, as it needs all the file be loaded in 
      the temporary file in memory. To be effecient, it needs to be divided to Chunks, and upon a chunk is completed be passed to API '''
    try:
        async with aiofiles.open(file_path, "wb") as f: #  aiofiles.open: Opens the file asynchronously for writing in binary mode.
            # file.read: Reads the file in chunks, using the chunk size defined in the settings.
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            
                # file.write: Writes each chunk to the file: 
                await f.write(chunk)
    except Exception as e:
        # We put the error in Log where we as developer can check but the user can't see these sensitive info,
        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, #This constant is used here to indicate that something went wrong during the file upload process.
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    # Next, a status code is not explicitly specified, so the default status code for a successful response, 200 (OK), will be used
    return JSONResponse(
            content={
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )
