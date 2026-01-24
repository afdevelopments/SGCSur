# SGCSur (Sistema de Gestión de Convenios CUSur)

**SGCSur** is a web-based Convention Management System developed for the *Centro Universitario del Sur* (CUSur) of the University of Guadalajara. Its primary purpose is to digitize and streamline the management of agreements (convenios) between the university and various external entities (companies, institutions).

## Description

The system allows administrators to register and track:

*   **Companies**: Agencies or businesses partnering with the University.
*   **Programs (Carreras)**: Academic programs offered by the campus.
*   **Contacts**: Key personnel within partnering companies.
*   **Agreements (Convenios)**: Legal agreements with start/expiration dates and status tracking.
*   **Reports**: Statistical insights into the agreements.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

*   Python 3.x
*   `pip` (Python Package Installer)
*   `virtualenv` (optional but recommended)

### Setup Instructions

1.  **Clone the repository**
    ```bash
    git clone <repository_url>
    cd SGCSur
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database**
    Run the migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

5.  **Create an Admin User**
    You'll need a superuser to access the admin panel and manage the system:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**
    Start the development server:
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

Once logged in, you can navigate through the following modules:

*   **Dashboard**: Provides a quick overview of active, expiring, and expired agreements.
*   **Companies**: Register and manage external entities (private, public, or social sectors).
*   **Agreements**: Link a **Program** with a **Company** for a specific duration. The system automatically calculates status based on validity dates.
*   **Reports**: Filter agreements by company, program, date, or sector, and export the results to Excel.

## Roadmap

*   [ ] **Security**: Externalize `SECRET_KEY` and database credentials to environment variables.
*   [ ] **Containerization**: Add Docker support for easier deployment.
*   [ ] **Testing**: Implement unit and integration tests for key workflows.
*   [x] **Reports**: Add "Sector" filter and "Include Contacts" option.
*   [x] **Dashboard**: Enhanced visual indicators for expiring agreements.

## Contributing

Contributions are welcome! If you'd like to improve the project, please following these steps:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

This project is developed for the **Centro Universitario del Sur (CUSur)** - University of Guadalajara.

## Project Status

Active development and maintenance.
