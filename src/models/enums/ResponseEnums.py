'''  Enum: This import brings in the Enum class from Python's standard library. Enums (enumerations) are a way to define a set of 
named values, which can be used to represent constant values in a more readable and maintainable way.  '''
from enum import Enum

''' ResponseSignal: This class inherits from Enum, making it an enumeration class. 
Each member of the enumeration is a constant that represents a specific signal or status.

Purpose and Usage
- Constant Values: Enums provide a way to define named constant values. 
This makes your code more readable and less error-prone compared to using plain strings or integers.

- Readability and Maintainability: Using enums can make your code more readable and easier to maintain. 
Instead of using raw strings or numbers to represent statuses or signals, you use named constants which are more descriptive.

- Type Safety: Enums provide better type safety compared to plain strings or numbers. 
The values are constrained to a specific set of options, reducing the likelihood of invalid values being used.    '''

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAILED = "processing_failed"
