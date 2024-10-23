# E2E Project using docker

This project demonstrates how to wrap a machine learning model in a FastAPI web application and Dockerize it for easy deployment. The application performs sentiment analysis using Hugging Face's `transformers` library, allowing users to analyze text via a simple API call.

## Project Purpose

The goal of this project is to learn how to:
- Build a basic API using FastAPI.
- Integrate a pre-trained machine learning model for sentiment analysis.
- Dockerize the application for deployment in a containerized environment.

## How to Build and Run

1. **Build the Docker image**:

   ```bash
   docker build -t fastapi-sentiment .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -d -p 8000:8000 fastapi-sentiment
   ```

3. **Test the API**:

   Open a browser or use a tool like `curl` or Postman to access:

   ```
   http://127.0.0.1:8000/analyze?input_string=I+love+this+app
   ```

   You will receive a JSON response with the sentiment and score.

## Learnings

- **Docker**: Containerized the FastAPI app for easy and scalable deployment.
- **FastAPI**: Created a simple web API for machine learning model inference.
- **Hugging Face `transformers`**: Integrated pre-trained NLP models for real-time inference.
