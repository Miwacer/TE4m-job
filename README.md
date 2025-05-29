# Te4am_job

**Te4am_job** is a Django-based web application for organizing team collaboration and task management. It allows you to create teams, assign and track tasks, manage projects, and monitor task completion — all within a clean Bootstrap interface.

## 🚀 Features

- 🔐 **Personal Dashboard**:
  - View your assigned tasks
  - Toggle task status (complete / incomplete)

- ✅ **Task Management**:
  - Create tasks and assign them to team members
  - Set deadlines, priorities, and task types
  - Browse all existing tasks

- 👥 **Team Collaboration**:
  - Create and manage teams
  - Add or remove team members
  - View members and their positions

- 🗂️ **Projects**:
  - View and create projects
  - Assign tasks and teams to each project

- 🔎 **Entities**:
  - All tasks
  - All task types
  - All workers and their roles

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML/CSS with [Bootstrap](https://getbootstrap.com/)
- **Database**: SQLite (default) or PostgreSQL
- **Authentication**: Django built-in auth

## 🧩 Task Details

- Priorities: **Urgent**, **High**, **Medium**, **Low**
- Tasks have types and can be linked to one or more projects

## ⚙️ Installation

   ```bash
- git clone https://github.com/miwacer/Te4am_job.git
- cd Te4am_job
- python -m venv venv
- source venv/bin/activate  # or `venv\Scripts\activate` on Windows
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## 👤 Test User

- Username: miwa  
- Password: 1234
---
