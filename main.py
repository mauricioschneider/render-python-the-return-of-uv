from fastapi import FastAPI

# 1. Create a FastAPI application instance
app = FastAPI()

# 2. Define the route for the root URL ("/") using the GET HTTP method
@app.get("/")
def read_root():
    """Returns a Python dictionary, which FastAPI automatically converts to JSON."""
    
    # 3. Return the dictionary. FastAPI handles the JSON serialization 
    # and sets the Content-Type header to application/json.
    return {"message": "Hello, World!"}