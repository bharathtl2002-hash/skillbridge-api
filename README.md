# SkillBridge Attendance Management API

## Overview:
This project is a backend API for a prototype attendance management system built as part of a take-home assignment. It supports multiple user roles and allows tracking attendance across training sessions.

## Links:
- Project Repository: https://github.com/bharathtl2002-hash/skillbridge-api  
- Live Deployment: https://skillbridge-api-u4a1.onrender.com  
- API Base URL: https://skillbridge-api-u4a1.onrender.com/api/
## Tech Stack:
- Python
- Django
- Django REST Framework
- SQLite (used for local development)
- JWT Authentication (SimpleJWT)

## Features Implemented:
- User signup with role selection
- User login with JWT token generation
- Role-based access control (student, trainer, etc.)
- Trainer can create batches
- Trainer can create sessions
- Student can mark attendance
- Trainer can view attendance for a session

## API Endpoints

### Authentication
- POST /api/signup/ → Register new user  
- POST /api/login/ → Login and receive JWT token  

### Batch & Session
- POST /api/batches/ → Create batch (trainer only)  
- POST /api/sessions/ → Create session (trainer only)  

### Attendance
- POST /api/attendance/mark/ → Mark attendance (student only)  
- GET /api/sessions/{id}/attendance/ → View attendance (trainer only)  

## Authentication Flow
- Login returns a JWT token  
- Token must be passed in request headers:

Authorization: Bearer <token>

- Role is stored inside the token and validated in the backend before allowing access  

## How to Run

1. Clone the repository  
2. Install dependencies:
   pip install -r requirements.txt  

3. Run migrations:
   python manage.py makemigrations  
   python manage.py migrate  

4. Start server:
   python manage.py runserver  

## Sample Test Users

Trainer:
- email: trainer@gmail.com  
- password: 123  

Student:
- email: student@gmail.com  
- password: 123  

## Notes:
- SQLite is used for local development for simplicity  
- The project can be configured to use PostgreSQL for production  
- Core functionality (authentication and role-based access control) is implemented  

## Limitations:
- Batch invite system not implemented  
- Programme-level summary APIs not included  
- Monitoring officer scoped token not implemented  
- Basic validation can be improved  

## Conclusion:
The focus of this implementation was on building a working API with proper authentication and role-based access control. Due to time constraints, priority was given to core features.