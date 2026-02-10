🚗 Car Scout - Intelligent Car Buying & Selling Platform

Car Scout is a comprehensive web-based platform designed to simplify the process of buying and selling used and new vehicles. It acts as a bridge between sellers (individuals or dealerships) and buyers, offering advanced features like AI-based vehicle inspection, real-time negotiation, and test drive scheduling.

This project was developed as a Final Year Internship Project.

---

## 📋 Table of Contents

* [Project Overview](#-project-overview)
* [Key Features](#-key-features)
* [Tech Stack](#-tech-stack)
* [Database Schema](#-database-schema)
* [Installation & Setup](#-installation--setup)
* [How to Run](#-how-to-run)
* [Screenshots](#-screenshots)

---

## 📖 Project Overview

The primary objective of Car Scout is to bring transparency and efficiency to the car marketplace. Unlike traditional classifieds, Car Scout integrates an **AI Inspection Report** system that provides buyers with a confidence score (0-10) regarding the car's condition, reducing the risk of fraud.

---

## ✨ Key Features

### 👤 User Roles

* **Buyers:** Can search, filter, book test drives, and make financial offers.
* **Sellers:** Can list vehicles, upload photos, and manage incoming offers.
* **Admin:** Verifies users and manages reported listings.

### 🚀 Core Functionalities

1. **Advanced Search:** Filter cars by Make, Model, Year, Price, and Location.
2. **AI Inspection Report:** Automated condition scoring (0.0 - 10.0) based on vehicle history and inputs.
3. **Negotiation System:** Buyers can make offers; Sellers can Accept, Reject, or Counter.
4. **Test Drive Booking:** Integrated scheduling system for physical car inspections.
5. **Secure Transactions:** Records payment methods and transaction history.
6. **360° Virtual Tour:** (Planned) Support for virtual vehicle walkthroughs.

---

## 🛠 Tech Stack

* **Backend Framework:** Django (Python)
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap (or Tailwind)
* **Version Control:** Git

---

## 🗄 Database Schema

The project uses a relational database with the following core models:

* **User:** Custom user model supporting Buyer/Seller roles.
* **Vehicle:** Stores static car data (VIN, Make, Model, Year).
* **Listing:** Links a Seller to a Vehicle with Price and Status.
* **InspectionReport:** Stores the AI score and accident history.
* **Offer:** Manages the price negotiation lifecycle.
* **TestDrive:** Manages appointment schedules.
* **Transaction:** Records final sales.

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1. Prerequisites

* Python 3.8 or higher installed.
* Git installed.

### 2. Clone the Repository

```bash
git clone https://github.com/thakorsumit/car-scout.git
cd car-scout

```

### 3. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 4. Install Dependencies

```bash
pip install django
# If you have a requirements.txt file:
# pip install -r requirements.txt

```

### 5. Database Setup

Initialize the database and apply migrations.

```bash
python manage.py makemigrations
python manage.py migrate

```

### 6. Create Superuser (Admin)

Create an admin account to manage the platform.

```bash
python manage.py createsuperuser

```

---

## 🚀 How to Run

### Start the Server

```bash
python manage.py runserver

```

Open your browser and visit: `http://127.0.0.1:8000/`

### Populate Demo Data (Optional)

To quickly fill the database with Indian context data (Users, Cars, Listings), you can use the provided Python script via the shell:

```bash
python manage.py shell
# (Copy and paste the data population script here)

```

---

## 📸 Screenshots

*(You can add screenshots of your project here)*

* *Home Page*
* *Car Detail View with AI Score*
* *Negotiation Dashboard*

---

## 📝 License

This project is developed for educational purposes.

**Author:** Sumit Thakor
**Batch:** BE 8th sem
**Institute:** Kalol Institute of Technology and Research, Kalol
