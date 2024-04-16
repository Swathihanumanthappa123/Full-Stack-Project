import os
from dotenv import load_dotenv, dotenv_values
from fastapi import FastAPI, HTTPException, Query
from dao import DAO
from pydantic import BaseModel
from typing import Optional, List, Tuple
from flask import Flask, render_template
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")
DBNAME = os.getenv("DBNAME")

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin (you can restrict this to specific origins)
    allow_methods=["GET"],  # Allow only GET requests (customize based on your requirements)
    allow_headers=["*"],  # Allow any headers
)

# Initialize DAO with database connection details
# Replace with your actual database connection details
dao = DAO(DBNAME, USER, PASSWORD, HOST, PORT)

# Pydantic models for request and response
class TopAuthorsResponse(BaseModel):
    author_name: str
    total_revenue: float

# Flask application instance for serving webpages
flask_app = Flask(__name__)

# API endpoint to get top 10 performing authors
@app.get("/top-authors")
async def get_top_performing_authors(author_name: Optional[str] = Query(None)) -> List[TopAuthorsResponse]:
    try:
        if author_name:
            # Check if author_name exists in database
            # Perform additional validation as needed
            total_revenue = dao.get_sales_total_for_author(author_name)
            if total_revenue == 0.0:
                raise HTTPException(status_code=404, detail="Author not found")

            return [TopAuthorsResponse(author_name=author_name, total_revenue=total_revenue)]
        else:
            # Get top 10 performing authors from database
            top_authors = dao.get_top_performing_authors(limit=10)
            if not top_authors:
                raise HTTPException(status_code=404, detail="No top authors found")

            return [TopAuthorsResponse(author_name=name, total_revenue=revenue) for name, revenue in top_authors]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")

# Shutdown event handler to close database connection
#@app.on_event("shutdown")
async def shutdown_event():
    # Perform cleanup or shutdown tasks here (if needed)
    print("Shutting down FastAPI application...")

# Register shutdown event handler using app.add_event_handler()
app.add_event_handler("shutdown", shutdown_event)

# Define route in Flask to render the HTML webpage
@flask_app.route('/')
def index():
    try:
        # Fetch top 10 performing authors from FastAPI endpoint
        response = get_top_performing_authors()
        return render_template('index.html', top_authors=response)

    except HTTPException as e:
        return render_template('index.html', error_message=f"Error: {e.detail}")

if __name__ == "__main__":
    # Run both FastAPI and Flask applications together using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)