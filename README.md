# FastAPI Sample Project

This project is a sample **FastAPI** application integrated with **Docker**, **Celery**, **Redis**, and **MongoDB**. It is designed to demonstrate how these services can work together in a containerized environment using **Docker Compose**.

## Features

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **Celery**: A distributed task queue for asynchronous task processing.
- **Redis**: An in-memory data store, used for caching and task queuing with Celery.
- **MongoDB**: A NoSQL database for storing data.

## Docker Image

You can easily pull the pre-built Docker image for this project from Docker Hub by running the following command:

```bash
docker pull sydulamin/fastapi-sample-project
