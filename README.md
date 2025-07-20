# Python Web App with Docker

A simple "Hello World" web application built with Python and Flask, containerized using Docker. This project serves as a basic template for a containerized Python web service that can be easily deployed.

<!-- Optional: Add a screenshot of your application -->
<!-- ![App Screenshot](https://via.placeholder.com/720x480.png?text=Hello+World+App) -->

## Features

*   Simple and lightweight Flask application.
*   Containerized with Docker for consistent environments and easy deployment.
*   Customizable greeting message via an environment variable.
*   Serves a favicon for a professional look in the browser.

## Prerequisites

Before you begin, ensure you have the following installed:
*   [Docker](https://www.docker.com/get-started)
*   [Python 3](https://www.python.org/downloads/) (for local development)

---

## Getting Started

There are two ways to run this application: using the pre-built image from Docker Hub or building it from the source code.

### Option 1: Run with the Pre-built Docker Image (Recommended)

This is the quickest way to get the application up and running.

1.  **Pull the image from Docker Hub:**
    ```bash
    docker pull karahub/python-web-app:latest
    ```

2.  **Run the container:**
    This command starts the container in detached mode and maps port 8080 on your machine to port 5000 in the container.
    ```bash
    docker run -d -p 5000:5000   karahub/python-web-app:latest
    ```

3.  **View the application:**
    Open your web browser and navigate to [http://localhost:5000](http://localhost:5000). You should see the message "Hello 🙋‍♂️, World from Docker!".

### Option 2: Build and Run from Source Code

Use this method if you have cloned the repository and want to build the image yourself.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/karadhub/python-web-app.git
    cd python-web-app
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t python-web-app .
    ```

3.  **Run the container:**
    ```bash
    docker run -d -p 5000:5000 python-web-app
    ```

4.  **View the application:**
    Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

---

## Local Development (Without Docker)

To run the application on your local machine for development:

1.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    python app/main.py
    ```

4.  The application will be running on [http://localhost:5000](http://localhost:5000).

---

## Configuration

The application's greeting can be customized using an environment variable.

*   `NAME`: Sets the name displayed in the greeting message.
    *   **Default:** `Vaibhav`
    *   **Example (Docker):** `docker run -e NAME="Universe" ...`
    *   **Example (Local):** `NAME="Universe" python app/main.py`