# Flask Data Retrieval and Processing Application

## Description

This is a simple Flask application that simulates data retrieval from an external service, processes the data, and stores it in temporary in-memory storage. The application provides API endpoints to fetch, process, and retrieve processed data.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Subhinpreet03/bookish-journey.git
# Or use SSH:
git clone git@github.com:Subhinpreet03/bookish-journey.git
cd bookish-journey
```

### 2. Setting up Virtual Environment
```bash
python3 -m venv .venv  # Replace '.venv' with the name of your virtual environment if desired
```
### Activate the virtual environment:

- #### On macOS/Linux:
```bash
source .venv/bin/activate
```

- #### On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages  specified in the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application
```bash
python app.py
```

### 5. Test the API Endpoints
#### You can test the API endpoints using tools like Postman or curl.
- #### Fetch Data:
```bash
curl -X GET http://127.0.0.1:5000/fetch-data
```

- #### Process Data:
```bash
curl -X POST http://127.0.0.1:5000/process-data
```

- #### Get Processed Data:
```bash
curl -X GET http://127.0.0.1:5000/get-processed-data
```



