# FastAPI Modular API with MongoDB & Beanie ODM 🚀

A production-ready, asynchronous REST API built with FastAPI and MongoDB. This project implements a strict layered architecture (Separation of Concerns) using Beanie as the Object Document Mapper (ODM) and the Repository Pattern for database operations.

## ✨ Features
* **FastAPI**: Modern, fast (high-performance) web framework for building APIs.
* **Beanie ODM**: Asynchronous Python object-document mapper for MongoDB (built on Motor).
* **Layered Architecture**: Clear separation of routing, business logic, data contracts, and configuration.
* **Repository Pattern**: Centralized database interactions using a `UserService` class.
* **Dependency Injection**: Clean and testable injection of settings and services.
* **Pydantic V2**: Strict data validation and serialization (handling the BSON `ObjectId` to string friction).

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Framework:** FastAPI
* **Database:** MongoDB
* **ODM / Driver:** Beanie / Motor
* **Server:** Uvicorn

## 📂 Project Structure
```text
app/
├── core/          # Environment configs & database lifecycle
├── schemas/       # Pydantic models & Beanie documents (Data Contracts)
├── services/      # Business logic & Repository pattern (UserService)
├── routers/       # HTTP endpoints
└── main.py        # Application entry point & lifespan events
🚀 Getting Started
Prerequisites

    Python 3.12 or higher installed.

    MongoDB running locally (port 27017) or a MongoDB Atlas URI.

1. Clone the repository
git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
cd YourRepoName
2. Set up the virtual environment
Bash

python3 -m venv myenv
source myenv/bin/activate

3. Install dependencies
Bash

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the root directory and add your configurations:
Code snippet

MONGODB_URI=mongodb://localhost:27017
db_name=local_dev_db
SECRET_KEY=your_super_secret_key_here

5. Run the Application
Bash

uvicorn app.main:app --reload

📖 API Documentation

Once the server is running, FastAPI automatically generates interactive API documentation.
Visit your browser at:

    Swagger UI: http://127.0.0.1:8000/docs

    ReDoc: http://127.0.0.1:8000/redoc