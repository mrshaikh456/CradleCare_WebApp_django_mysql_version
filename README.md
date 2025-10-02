# CradleCare 👶💖  
**The Newborn & Mother Wellness Companion (MySQL Version)**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://www.djangoproject.com/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Last Commit](https://img.shields.io/github/last-commit/mrshaikh456/CradleCare_MySQL)](https://github.com/mrshaikh456/CradleCare_WebApp_django_mysql_version/commits/main)  
[![Issues](https://img.shields.io/github/issues/mrshaikh456/CradleCare_MySQL)](https://github.com/mrshaikh456/CradleCare_WebApp_django_mysql_version/issues)  
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?logo=github)](../../issues)

CradleCare is a **full-stack web application** designed as an all-in-one wellness tracker for newborns and their mothers.  
It provides a clean, intuitive interface to help new mothers log, track, and visualize essential health data — reducing stress during the postpartum period.

![Screenshot](https://github.com/user-attachments/assets/185307cd-5de3-40c6-aadc-4ed3f62a4b8c)  
![Screenshot](https://github.com/user-attachments/assets/d5ae9f4b-bfbc-423c-9ba3-0817dbabe4a4)

---

## ✨ Features
- 🔐 **Secure User Accounts** – Private, secure accounts for each mother  
- 👶 **Baby Profile Management** – Add and manage profiles for one or more babies  
- 📊 **Comprehensive Trackers**  
  - Growth Tracker with dynamic charts  
  - Sleep Logger with automatic duration calculation  
  - Feeding Logger (breastmilk, formula, solids)  
  - Appointment Tracker (pediatric visits)  
  - Milestone Tracker (special moments)  
- 💉 **Dynamic Vaccination Schedule** – Auto-calculated from DOB, mark vaccines complete  
- 📖 **Content Management** – Recipe Book & Personal Journal (via Django Admin)  
- 📝 **Full CRUD Functionality** – Create, view, and delete logs  

---

## 🛠 Tech Stack
- **Backend:** Python / Django  
- **Database:** **MySQL 8.x**  
- **Frontend:** HTML5 / CSS3  
- **Styling:** Custom CSS (component-based)  
- **Charts:** Chart.js  

---

## ⚙️ Setup & Installation

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/)  
- [MySQL 8.x](https://dev.mysql.com/downloads/)  
- [MySQL Client / Connector](https://pypi.org/project/mysqlclient/)  

### Steps
1. **Clone the repository**  
   ```bash
   git clone https://github.com/mrshaikh456/CradleCare_WebApp_django_mysql_version.git
   cd CradleCare_MySQL

2. **Create & activate a virtual environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    ```bash
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies
    ```bash
    pip install -r requirements.txt

4. Update your database settings (in settings.py) with your MySQL credentials:
    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cradlecare_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        }
    }

5. Apply migrations
    ```bash
    python manage.py migrate
    
6. Create a superuser (for Admin Panel)
    ```bash
    python manage.py createsuperuser

7. Run the development server
    ```bash
    python manage.py runserver
App will be live at: http://127.0.0.1:8000/

---

## 🚀 Usage
###Admin Panel (Content Management)

- Go to: http://127.0.0.1:8000/admin/
- Log in with your superuser account
- Add vaccines, recipes, or other content

### Main Application

- Visit http://127.0.0.1:8000/
- Register or log in as a user
- Create a baby profile and start using the trackers

## 📌 Roadmap

- 📱 Mobile-first responsive design
- 🌙 Dark mode support
- 📈 Health analytics & reports
- 🔔 Push/email reminders for vaccines & appointments
- 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Open an issue
 or create a pull request.

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgements

- Django
- Chart.js
- New mothers everywhere — for inspiration & strength 💖


