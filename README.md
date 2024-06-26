**# Full Stack Project

This project demonstrates a full-stack web application using PostgreSQL, FastAPI (backend), and React (frontend).

## Overview

This project consists of a backend API built with FastAPI, which interacts with a PostgreSQL database using a DAO (Data Access Object) pattern. The backend provides endpoints to perform CRUD operations on the database. The frontend is built using React and consumes the backend API to display data and interact with the user.

## Features

- Fetch data from a PostgreSQL database using FastAPI endpoints.
- Display data in a React frontend application.
- Perform CRUD operations via the frontend UI.

## Requirements

- Python (v3.7 or higher)
- PostgreSQL database
- FastAPI backend endpoint
- React frontend development

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Swathihanumanthappa123/Full-Stack-Project.git


2. **Install Python dependencies for the backend:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies for the frontend:**
   ```bash
   cd my-react-app
   npm install
   ```

## Running Locally

### Backend (FastAPI)

1. **Set up environment variables:**
    - Create a `.env` file in the directory.
    - Edit your .env file parameters according to your Postgres configuration.

2. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the backend API:**
   Open `http://localhost:8000/top-authors` in your web browser.

   To check the individual sales total of top authors:
   Example: `http://127.0.0.1:8000/top-authors?author_name=Rory%20Gilmore`

### Frontend (React)

1. **Start the React development server:**
   ```bash
   cd my-react-app
   npm start
   ```

2. **Access the React frontend:**
   Open `http://localhost:3000` in your web browser.

## Deployment

### Backend (FastAPI)

- Deploy the FastAPI backend to a hosting platform (e.g., Heroku, AWS, DigitalOcean).
- Set up environment variables in the hosting platform for database connection details.

### Frontend (React)

1. **Build the React frontend for production:**
   ```bash
   cd my-react-app
   npm run build
   ```

2. **Deploy the frontend build:**
   Host the contents of the `build` directory on Netlify, Vercel, or a similar platform for static site hosting.
   Update the API base URL in the frontend to point to the deployed backend API.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
