# Website Backend (Django) for Shumanay medicine department
This is a backend for the Shumanay medicine department website. It is built with Django and Django Rest Framework. It provides the following features:
## Features
- Anyone can view information about the medicine department
- Admin can add, update, delete all information about the medicine department
- OTP code is sent to the user's email when they forget their password

## Technologies
- Django
- Django Rest Framework
- Docker
- Docker Compose
- Django Rest Framework Simple JWT
- drf-yasg
- Redis
- Django Cors Headers
- Celery

## Installation
1. Clone the repository
```bash
git clone https://github.com/Diyarbekoralbaev/shumanay_rmb_backend_drf
```
2. Change directory 
```bash
cd shumanay_rmb_backend_drf
```
3. Setup the application
```bash
make setup
```
4. Build the application
```bash
make build
```
5. Run the application
```bash
make run
```

## API Endpoints
### Auth app
- POST `/users/login/` - Login user
- POST `/users/logout/` - Logout user
- POST `/users/signup/` - Register user
- POST `/users/forgot-password/` - Forgot password (send email)
- POST `/users/reset-password/` - Reset password (via otp code sent to email)
- POST `/users/change-password/` - Change password (current user)
- POST `/users/login/refresh/` - Refresh token
- GET `/users/me/` - Get current user

### Documents app
- GET `/documents/` - Get all documents
- POST `/documents/` - Create a new document
- GET `/documents/{id}/` - Get document by id
- PUT `/documents/{id}/` - Update document by id
- PATCH `/documents/{id}/` - Partial update document by id
- DELETE `/documents/{id}/` - Delete document by id

### Gallery app
- GET `/gallery/` - Get all gallery images
- POST `/gallery/` - Create a new gallery image
- GET `/gallery/{id}/` - Get gallery image by id
- PUT `/gallery/{id}/` - Update gallery image by id
- PATCH `/gallery/{id}/` - Partial update gallery image by id
- DELETE `/gallery/{id}/` - Delete gallery image by id

### News app
- GET `/news/` - Get all news
- POST `/news/` - Create a new news
- GET `/news/{id}/` - Get news by id
- PUT `/news/{id}/` - Update news by id
- PATCH `/news/{id}/` - Partial update news by id
- DELETE `/news/{id}/` - Delete news by id

### Admissions app
- GET `/shrmb/admissions/` - Get all admissions
- POST `/shrmb/admissions/` - Create a new admission
- GET `/shrmb/admissions/{id}/` - Get admission by id
- PUT `/shrmb/admissions/{id}/` - Update admission by id
- DELETE `/shrmb/admissions/{id}/` - Delete admission by id

### Departments app
- GET `/shrmb/departments/` - Get all departments
- POST `/shrmb/departments/` - Create a new department
- GET `/shrmb/departments/{id}/` - Get department by id
- PUT `/shrmb/departments/{id}/` - Update department by id
- DELETE `/shrmb/departments/{id}/` - Delete department by id

### Doctors app
- GET `/shrmb/doctors/` - Get all doctors
- POST `/shrmb/doctors/` - Create a new doctor
- GET `/shrmb/doctors/{id}/` - Get doctor by id
- PUT `/shrmb/doctors/{id}/` - Update doctor by id
- DELETE `/shrmb/doctors/{id}/` - Delete doctor by id

### History app
- GET `/shrmb/history/` - Get all history
- POST `/shrmb/history/` - Create a new history
- GET `/shrmb/history/{id}/` - Get history by id
- PUT `/shrmb/history/{id}/` - Update history by id
- DELETE `/shrmb/history/{id}/` - Delete history by id

### Vacancies app
- GET `/shrmb/vacancies/` - Get all vacancies
- POST `/shrmb/vacancies/` - Create a new vacancy
- GET `/shrmb/vacancies/{id}/` - Get vacancy by id
- PUT `/shrmb/vacancies/{id}/` - Update vacancy by id
- DELETE `/shrmb/vacancies/{id}/` - Delete vacancy by id

### Useful tips app
- GET `/shrmb/useful-tips/` - Get all useful tips
- POST `/shrmb/useful-tips/` - Create a new useful tip
- GET `/shrmb/useful-tips/{id}/` - Get useful tip by id
- PUT `/shrmb/useful-tips/{id}/` - Update useful tip by id
- DELETE `/shrmb/useful-tips/{id}/` - Delete useful tip by id


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Author
- [Diyarbek Oralbaev](https://github.com//Diyarbekoralbaev/)
- [Email](mailto:diyarbekdev@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/diyarbek-oralbaev-66a020316/)
- [Telegram](https://t.me/Diyarbek_Dev)

## Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Django Rest Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [Redis](https://redis.io/)
- [Django Cors Headers](https://pypi.org/project/django-cors-headers/)