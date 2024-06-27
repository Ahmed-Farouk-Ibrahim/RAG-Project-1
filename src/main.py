from fastapi import FastAPI

# From directory routes reach base.py file to call base_router decorator
from routes import base, data

app = FastAPI()

'''   Routers: In FastAPI, a router is a way to group related endpoints together. 
This makes it easier to organize your application, especially as it grows in complexity.

include_router: This method is used to include a router in the main FastAPI application.
It allows you to modularize your routes and include them in the main application.

base.base_router refers to a router defined in the base module of the routes package. This router might handle general or 
foundational routes for the application, such as the root endpoint, health checks, or other common routes.

data.data_router refers to a router defined in the data module of the routes package. This router might handle data-related routes,
such as file uploads, data processing, or other endpoints related to data management.   '''
app.include_router( base.base_router )
app.include_router( data.data_router )
