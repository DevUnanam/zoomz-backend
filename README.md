This is the backend folder for the webappZoomz 
zoomz is a webapp where users can go online to shop for cars, book testdrives e.t.c

virtual environment started with --> source zoomz_env/bin/activate

Endpoints created:
 List of Endpoints for the Zoomz API
User Authentication Endpoints:

POST /api/register/: Register a new user(works)
POST /api/login/: Login an existing user and return a token(works)
POST /api/logout/: Log out a user (session based authetication works)
GET /api/user/: Retrieve logged-in user's details (authentication required)
Car Listings Endpoints:

GET /api/cars/: Get a list of all cars, with optional query parameters to filter by make, model, price, location, etc.
POST /api/cars/: Create a new car listing (admin or dealership-only access)
GET /api/cars/<id>/: Get details of a specific car by ID
PUT /api/cars/<id>/: Update a specific car listing (admin or dealership-only access)
DELETE /api/cars/<id>/: Delete a car listing (admin or dealership-only access)
Dealership Endpoints:

GET /api/dealerships/: Get a list of dealerships
POST /api/dealerships/: Add a new dealership (admin or authorized users only)
GET /api/dealerships/<id>/: Get details of a specific dealership
PUT /api/dealerships/<id>/: Update dealership details
DELETE /api/dealerships/<id>/: Remove a dealership from the platform
Search and Filtering Endpoints:

GET /api/search/: Search for cars based on various criteria (e.g., make, model, price range, location)
GET /api/filters/: Get available filter options, like car makes, models, price ranges, etc.
Car Image Uploads:

POST /api/cars/<id>/upload/: Upload images for a specific car listing
GET /api/cars/<id>/images/: Retrieve images for a specific car
Contact Endpoints:

POST /api/contact/: Allow users to send inquiries to dealerships about a car listing
Admin Endpoints (if you have an admin panel for managing cars and dealerships):

GET /api/admin/cars/: Admin can view all cars listed on the platform
GET /api/admin/dealerships/: Admin can view all dealerships
GET /api/admin/users/: Admin can view all users
