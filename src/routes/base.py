from fastapi import FastAPI, APIRouter, Depends
import os

from helpers.config import get_settings, Settings

'''Modify the access to base_router:
base_router is an instance of APIRouter with a prefix and tags.
prefix="/api/v1" means that all endpoints defined in this router will have /api/v1 prefixed to their paths.
tags=["api_v1"] is used for documentation purposes, grouping the endpoints under the api_v1 tag in the generated API docs.
'''
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


# Use decorator so that if anyone send a request with my url, convert him to this next function and execute its content:
''' Any application should have a function that handle if anyone enters the default route for many reasons. 
One of them is the Health Check. When we run on the server in the production, the DevOps engineer may ask u for a route to check
    whether the app is working good by getting a simple response message.
-Why I use app_settings: Settings = Depends(get_settings: app_settings is an external source of data we depends on to load this route.
But what if I loaded this route & for any reason we couldn't find app_settings. So Depends firsly loads this function firstly.
A parameter of type Settings = Depends(get_settings): Tells FastAPI to use the get_settings function to provide the app_settings parameter.
'''
@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version,
    }

