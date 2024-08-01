# University Courses Management Application

This project is a full-stack web application for managing university courses. It is built using Flask for the backend and Angular for the frontend.

## Prerequisites

- Python 3.10
- Node.js and npm
- MongoDB

## Backend Setup

1. **Navigate to the backend directory**:
    ```sh
    cd adcore/backend
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the Flask application**:
    ```sh
    flask run
    ```
   The backend server should now be running on `http://localhost:5000`.

## Frontend Setup

1. **Navigate to the frontend directory**:
    ```sh
    cd adcore/frontend
    ```

2. **Install the required packages**:
    ```sh
    npm install
    ```

3. **Run the Angular application**:
    ```sh
    ng serve
    ```
   The frontend application should now be running on `http://localhost:4200`.

## API Endpoints

### Courses API

- **Get all courses**:
    ```sh
    GET /api/courses
    ```

- **Get a specific course**:
    ```sh
    GET /api/courses/<id>
    ```

- **Create a new course**:
    ```sh
    POST /api/courses
    ```

- **Update a course**:
    ```sh
    PUT /api/courses/<id>
    ```

- **Delete a course**:
    ```sh
    DELETE /api/courses/<id>
    ```

## Directory Structure

adcore/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── routes.py
│ │ ├── utils.py
│ ├── venv/
│ ├── requirements.txt
│ └── run.py
└── frontend/
├── src/
│ ├── app/
│ │ ├── course-list/
│ │ ├── course-detail/
│ │ ├── course-form/
│ │ ├── services/
│ │ ├── app.component.html
│ │ ├── app.component.ts
│ │ ├── app.config.ts
│ │ ├── app.routes.ts
│ ├── assets/
│ ├── environments/
│ ├── main.ts
│ └── index.html
├── angular.json
├── package.json
├── tsconfig.json
└── tsconfig.app.json


## Usage

1. **Starting the Backend**:
    - Ensure MongoDB is running.
    - Navigate to the backend directory, activate the virtual environment, and run the Flask application.

2. **Starting the Frontend**:
    - Navigate to the frontend directory and run the Angular application.

3. **Access the Application**:
    - Open your browser and navigate to `http://localhost:4200/courses` to interact with the application.

## Troubleshooting

- **Backend issues**:
    - Ensure MongoDB is running and accessible.
    - Check the Flask application logs for any errors.

- **Frontend issues**:
    - Ensure the backend is running and accessible.
    - Check the Angular application logs and browser console for any errors.

## Additional Notes

- The application uses `ng-bootstrap` for UI components.
- Ensure CORS is correctly configured in Flask to allow requests from the Angular application.

---

Follow these steps to set up and run the application successfully. If you encounter any issues, refer to the troubleshooting section or check the logs for more details.

Test Results:

FLASK
GET Request
 ![image](https://github.com/user-attachments/assets/cd8f634a-880d-4d16-930f-9915b82ca2d3)


POST Request:
![image](https://github.com/user-attachments/assets/7ba4b2c5-6267-423c-83a1-809e81daa279)

 
UPDATE/PUT Request:
![image](https://github.com/user-attachments/assets/ea5b73e4-5c58-44ea-a540-ea8b5afda218)

 
DELETE Request:
![image](https://github.com/user-attachments/assets/0e567f70-a0f0-4a62-bef2-15d22ac9f944)

 
FRONTEND – ANGULAR:
COURSE VIEW:
 ![image](https://github.com/user-attachments/assets/e216fba1-36ea-4f37-9e14-e901f4f6635e)


FETCH/DELETE COURSE:
![image](https://github.com/user-attachments/assets/ec57f9c4-0776-48c6-aaa6-a3924debabc2)

 
EDIT Course
![image](https://github.com/user-attachments/assets/995d3ae9-c581-4e8b-a8d4-964ca68a9fbe)

 
ADD New Course
![image](https://github.com/user-attachments/assets/f2e81588-23b9-4a7a-a828-afc24071db4b)

