'''
Pydantic is a data validation & settings management library for Python. 
It ensures that the values provided to these fields conform to the specified types & provides default values for optional fields if none are provided.
BaseModel is a base class for creating Pydantic models which provides data validation and serialization.
'''
from pydantic import BaseModel 
from typing import Optional  # Optional is used to indicate that a value can be of a specified type or None.

# Class that inherits from BaseModel. By inheriting from BaseModel, ProcessRequest gains capabilities for data validation, serialization, & more.
# The ProcessRequest class defines a schema for processing requests with the following fields:
class ProcessRequest(BaseModel):
    file_id: str  # A required string that identifies the file.
    chunk_size: Optional[int] = 100 # An optional integer specifying the size of chunks to process, defaulting to 100.
    overlap_size: Optional[int] = 20 # An optional integer specifying the size of the overlap between chunks, defaulting to 20.
    do_reset: Optional[int] = 0 #  An optional integer indicating whether to reset the process, defaulting to 0.
