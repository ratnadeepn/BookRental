# BookRental
A web application for student book rentals.Students can rent a book for one month without any charge. If they desire to keep the book beyond the initial month, a fee is charged determined by the book's page count divided by 100.

# Book Rental System

This project is a Django-based book rental system that integrates with the Open Library API to fetch book data. The project consists of two main apps: `adminapp` and `rental`.

## Software Requirements

- Python
- Django
- Django REST framework

**Note:** An internet connection is required as data is fetched from [Open Library](https://openlibrary.org/).

### Order of Execution of Commands

- python manage.py makemigrations
- python manage.py migrate
- python manage.py makemigrations rental
- python manage.py migrate rental
- python manage.py createsuperuser  (to access the /admin endpoint)
- python manage.py runserver

#### There are two apps in this project
1. adminapp
2. rental

#### adminapp manages all the admin related functionalities, which are:
1. adding a new user (could also be done from /admin endpoint)
2. adding a new rental - where a book is fetched from https://openlibrary.org/ using the title
3. delete an existing rental
4. prolong a rental
5. fetch all books rented by a user

#### rental app deals with basic data fetching. All Models are defined here.
1. get all books
2. get all rentals
3. get all users

#### The Endpoints in order of its execution are:
1. v1/manage/newuser/	(create a new user)
2. v1/manage/newrental/ (create a new rental. The title of the book must be provided as - the+lord+of+the+rings)
3. v1/manage/booksbyuser/<int:user_id>/ (get all books by a user. Eg- v1/manage/booksbyuser/2/)
4. v1/manage/prolongrental/<int:rental_id>/ (get charges to be beared by the user for a rental. Eg- v1/manage/prolongrental/1/)
5. v1/rental/allrentals/ (get all existing rentals. Could be accessed from /admin also)
6. v1/rental/users/ (get all users. Could be accessed from /admin also)
7. v1/rental/books/ (get all existing books. Could be accessed from /admin also)
8. v1/manage/deleterental/<int:rental_id>/ (delete an existing rental. Eg- v1/manage/deleterental/1/)

