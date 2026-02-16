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
└── main.py        # Application entry point & lifespan events```
