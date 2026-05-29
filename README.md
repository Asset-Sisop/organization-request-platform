# Organization Request Platform

## Overview

Organization Request Platform is a web application developed with FastAPI for managing organizations, users, and requests through a centralized REST API.

The platform provides a foundation for automating business processes, digital services, and request management workflows.

## Features

* User registration and authentication
* Organization management
* Request creation and processing
* REST API architecture
* PostgreSQL database support
* JWT-based security
* Modular project structure

## Technology Stack

* Python 3
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* Uvicorn

## Project Structure

backend/

├── app/

│ ├── api/

│ ├── models/

│ ├── schemas/

│ ├── database.py

│ ├── dependencies.py

│ ├── security.py

│ └── main.py

├── requirements.txt

└── README.md

## Installation

Clone repository:

git clone https://github.com/Asset-Sisop/organization-request-platform.git

Install dependencies:

pip install -r requirements.txt

Run application:

uvicorn app.main:app --reload

## API Documentation

After starting the application:

http://127.0.0.1:8000/docs

## Use Cases

The platform can be used for:

* Organization registration systems
* Request management systems
* Internal business process automation
* Digital service platforms
* Government and corporate portals

## Status

MVP (Minimum Viable Product)
