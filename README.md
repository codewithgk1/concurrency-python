# FastAPI Concurrency Example

This project demonstrates the usage of FastAPI with asynchronous endpoints and concurrency handling.

## Project Structure

```
.
├── main.py          # Main FastAPI application file
├── requirements.txt # Project dependencies
└── README.md       # This file
```

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Basic Run Command
To run the application in development mode with auto-reload:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

### Advanced Uvicorn Options

You can customize the server configuration using various command-line options:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
```

#### Command Options Explained:

1. `--host 0.0.0.0`:
   - Specifies the host address to bind the server
   - `0.0.0.0` means the server will be accessible from any IP address
   - Default is `127.0.0.1` (localhost only)

2. `--port 8080`:
   - Sets the port number for the server
   - Default is `8000`
   - Choose any available port number (1-65535)

3. `--workers 4`:
   - Number of worker processes to run
   - Each worker handles requests independently
   - Recommended: (2 x number_of_cores) + 1
   - Default is 1 worker
   - Only works with `--reload` disabled

4. `--reload`:
   - Enables auto-reload on code changes
   - Useful for development
   - Should be disabled in production
   - Cannot be used with multiple workers

Example with all options:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4 --reload
```

## API Endpoints

### GET /1
- A test endpoint that simulates a long-running operation
- Uses `time.sleep(10)` to demonstrate blocking behavior
- Prints "Hello" at the start and "Bye" after completion

## Understanding the Code

The main application (`main.py`) demonstrates:
- Basic FastAPI setup
- Async endpoint definition
- Simulated long-running operations

## Development Notes

- The `--reload` flag in uvicorn enables auto-reload during development
- The server will automatically restart when code changes are detected
- This is a development-only feature and should not be used in production
- For production, use multiple workers and disable auto-reload

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## License

MIT License 