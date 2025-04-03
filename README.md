# FastAPI Concurrency Example

This project demonstrates different types of concurrency handling in FastAPI applications.

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

### 1. Blocking Endpoint (`/1`)
- Demonstrates blocking I/O operations using `time.sleep()`
- Blocks the entire server for 10 seconds
- Sequential execution
- Not recommended for production use

### 2. Non-Blocking Endpoint (`/2`)
- Demonstrates non-blocking I/O operations using `asyncio.sleep()`
- Allows other requests to be processed while waiting
- Concurrent execution
- Recommended for production use
- Uses FastAPI's async capabilities

### 3. Threaded Endpoint (`/3`)
- Demonstrates synchronous execution in a separate thread
- Blocks only the current request, not the entire server
- Each request runs in its own thread
- Useful for CPU-bound operations
- Note: Threading has overhead and is not recommended for I/O-bound operations

## Accessing the API Documentation

1. Swagger UI: http://localhost:8000/docs
2. ReDoc: http://localhost:8000/redoc

## Testing the Endpoints

1. Blocking Endpoint (`/1`):
```bash
curl http://localhost:8000/1
```
- This will block the server for 10 seconds
- Other requests will be queued

2. Non-Blocking Endpoint (`/2`):
```bash
curl http://localhost:8000/2
```
- This will not block the server
- Other requests can be processed while waiting
- **Important Note**: When testing the non-blocking behavior locally, use two different browsers to make the API calls. Many browsers use HTTP keep-alive connections, which might not demonstrate the true asynchronous behavior when using the same browser or connection.

3. Threaded Endpoint (`/3`):
```bash
curl http://localhost:8000/3
```
- This will block only the current request
- Other requests can be processed in separate threads

## Understanding the Differences

1. **Blocking Endpoint (`/1`)**:
   - Uses `time.sleep()`
   - Blocks the entire event loop
   - Sequential execution
   - Not suitable for production

2. **Non-Blocking Endpoint (`/2`)**:
   - Uses `asyncio.sleep()`
   - Yields control back to the event loop
   - Concurrent execution
   - Best for I/O-bound operations

3. **Threaded Endpoint (`/3`)**:
   - Uses synchronous code in a separate thread
   - Each request gets its own thread
   - Useful for CPU-bound operations
   - Has thread management overhead

## Best Practices

1. Use async/await for I/O-bound operations
2. Use threading for CPU-bound operations
3. Avoid blocking operations in async endpoints
4. Consider using background tasks for long-running operations

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