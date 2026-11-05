<div align="center">

# ✅ Django Todo

**A clean, minimal todo application built with Django and the Django admin.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-2.2-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-GPLv3-blue)

⭐ If you find this project useful, consider giving it a star!

</div>

---

## ✨ Features

- 📝 Create, list and delete todos
- ✔️ Mark todos as finished / unfinished
- 🔎 Each todo has a title, description and timestamp
- 🛠️ Full management through the built-in Django admin
- 🗃️ Zero-config SQLite database — runs out of the box

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 2.2 (Python) |
| Database | SQLite |
| Templates | Django template engine |

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/unitenist/todo.git
cd todo

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
cd djangoadmin
python manage.py migrate

# 5. (Optional) Create an admin user
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.
The admin panel is available at **http://127.0.0.1:8000/admin/**.

## 📁 Project Structure

```
todo/
├── requirements.txt
└── djangoadmin/
    ├── manage.py
    ├── djangoadmin/      # Project settings (settings, urls, wsgi)
    ├── unitenist/        # Todo app (models, views, urls, admin)
    └── template/         # HTML templates
```

## 📋 Routes

| Path | Description |
|---|---|
| `/` | List all todos |
| `/create` | Add a new todo |
| `/about` | About page |
| `/admin/` | Django admin panel |

## 📄 License

This project is licensed under the GNU General Public License v3.0 — see the [LICENSE](LICENSE) file for details.
