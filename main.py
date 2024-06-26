from fastapi import FastAPI
app = FastAPI()

# Use decorator so that if anyone send a request with my url + /welcome, convert him to this next function and execute its content:
@app.get("/welcome")
def welcome():
    return {
        "message": "Hello World!"
    }
