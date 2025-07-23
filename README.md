#  Customer Support Ticketing System - Backend (Django + DRF)

This is the backend service for the **High-Performance Searchable Ticketing System** built using Django and Django REST Framework. It provides CRUD operations and high-performance searching/filtering/pagination capabilities for managing support tickets at scale.

---

##  Features

-  Create, View, Update, and Delete tickets
-  Full-text search on fields like name, email, issue
-  Filter by status, priority, and created date range
-  Pagination support with offset and limits
- Optimized queries using `Q` objects and indexing
-  Seeded with 100,000+ fake records using `Faker`
-  Modular and clean codebase with proper exception handling
-  Swagger UI for API testing and documentation

---

## Prerequisites:

- Python 3.10.0
- Django 5.2.4
- Django REST Framework
- MySql
- drf-yasg (for Swagger UI)
  

---

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ticketing-system-backend.git
cd ticketing-system-backend

 ```
### 2.Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate

 ```
### 3.Install Dependencies

```bash
     pip install -r requirements.txt


 ```
### 4.Run Locally

```bash
    Run Locally:

   python app.py runserver 0.0.0.0:8000

   Swagger URL:

    http://localhost:8000/Customer_Ticket_System/docs/



Quick Start:

Your directory tree should be like this,

TICKET_SYSTEMS/
├── .idea/                        
├── logs/                        
├── t_env/                        
├── ticket_app/                   
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                 
│   ├── serializers.py           
│   ├── tests.py
│   ├── urls.py                  
│   ├── views.py                 
│   ├── migrations/            
│   └── utils/                   
│       ├── __init__.py
│       └── response.py          
├── ticket_project/              
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              
│   ├── swagger_service.py      
│   ├── urls.py                 
│   └── wsgi.py
├── app.py                       
├── requirements.txt           
└── README.md                   




