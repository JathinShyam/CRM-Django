# CRM-Django
Customer Relationship Management app using Django

# Customer Relationship Management System

## Overview

This project is a Django-based Customer Relationship Management (CRM) system designed to help you manage and maintain strong customer relationships, streamline communication, and improve overall customer satisfaction. It offers robust features to manage customer data, handle customer queries, and assign tasks to support leads. The application employs user authentication, responsive design, contact management, and more to enhance your CRM capabilities.

## Key Features

1. **Customer Management**
   - Add, edit, and view customer details, including name, email, phone, address, and more.
   - Display a list of all customers with search and pagination options.

2. **Customer Queries**
   - Customers can submit queries related to their interactions.
   - Submitted queries are tracked and can be assigned to leads for resolution.

3. **Lead Management**
   - Manage leads (customer support representatives) with their professional details.
   - Assign queries to leads for resolution.

4. **Task and Reminder System**
   - Allow users to set tasks and reminders related to customer interactions.
   - Send notifications and reminders to users for upcoming tasks.

5. **User Authentication and Permissions**
   - Users can be categorized as regular users (customers), leads, or superusers.
   - Different access permissions based on user roles.

6. **Responsive Design**
   - The application is designed to be responsive, ensuring a seamless user experience on various devices.

## Installation and Usage

1. Clone the repository:
   ```shell
   git clone https://github.com/JathinShyam/CRM-Django.git

2. Install dependencies:
   ```shell
   pip install -r requirements.txt

3. Apply database migrations:
   ```shell
   python manage.py migrate

4. Create a superuser for initial login:
   ```shell
   python manage.py createsuperuser

5. Start the development server:
   ```shell
   python manage.py runserver

6. Access the CRM system via your web browser: http://localhost:8000/

7. Log in using your superuser credentials to access the admin panel.