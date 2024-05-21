# Project

## Installation Instructions

### Prerequisites
Make sure to have Python and pip installed on your system. You can download them from [Python's official website](https://www.python.org/downloads/).

### Frontend Installation

Navigate to the `fastai/frontend` folder and run the following commands to set up the frontend of the application:

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application using Streamlit:
   ```bash
   streamlit run app.py
   ```

### Backend Installation

Navigate to the `fastai/backend` folder and execute these commands to set up the backend:

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the backend server (choose one of the following methods):
   - Using Uvicorn with live reloading:
     ```bash
     uvicorn app:app --reload
     ```
   - Directly running the Python script:
     ```bash
     python app.py
     ```

### Using Docker

To containerize and run the project using Docker, perform the following steps:

1. Build the Docker images:
   ```bash
   docker-compose build
   ```

2. Launch the containers:
   ```bash
   docker-compose up
   ```