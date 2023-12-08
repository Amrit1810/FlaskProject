# Python Project (Flask)

### OBJECTIVE:
- Creating a Simple Website to show data after pulling it from the db

### Project:
- In this project, We made a website where user can login, registar, reset password and see his/her profile. We are not creating Session but the login will still work with credentials only as it is a simple project.

### Data
- In this project, we are not getting data via web scraping or API. We created random user data by our own using Python and pushed the data (200 Record) into the db.


## Files:
- **`app.py`** This Python script initializes a Flask web application, incorporating a blueprint named views to handle routes. It utilizes the Flask framework to create a web server and runs the application with debugging enabled on port 5000 when executed directly.
- **`views.py`** This Python script define Flask routes using a Blueprint named views for login, registration, profile, and password reset, with sample user data. The profile route renders a template with details for a user who logged in.
- **`SampleDataGeneration.py`** This Python script generates a sample dataset of user profiles with random information, including names, genders, LinkedIn profiles, designations, countries, and more. The generated data is structured as a list of dictionaries, with each dictionary representing a user profile. The dataset creation is based on a mix of predefined male and female names, industrial designations, and other attributes.
- **`database.py`** This Python script defines functions for interacting with an SQLite database named `websitedata.db.` The sample_data_fill function creates a table named `users` and fills it with sample user data generated using `SampleDataGeneration.py.` The data_fill function inserts user data into the `users` table, while the data_fetch function retrieves user data based on email and password. The existence_check function checks if a user with a given email already exists in the database.
- **`websitedata.db`** Database - User Information Stored in table named `user`
- **`Requirements.txt`** All the packages/libraries needed to run this project.
- **`templates`**
    - **`about.html`**  HTML page for Data Briefing.
    - **`login.html`** HTML page for log in.
    - **`passreset.html`** HTML page for Reseting the password.
    - **`profile.html`** HTML page for User Profile.
    - **`reg.html`**  HTML page for Registration of a new user.
- **`static`**
    - **`about.html`** Stylesheet defining the visual presentation for `about.html` webpage in the project.
    - **`login.css`** Stylesheet defining the visual presentation for `login.html` webpage in the project.
    - **`passreset.css`** Stylesheet defining the visual presentation for `passreset.html` webpage in the project.
    - **`profile.css`** Stylesheet defining the visual presentation for `profile.html` webpage in the project.
    - **`reg.css`**  Stylesheet defining the visual presentation for `reg.html` webpage in the project.

# Testing Credentials
- **`email:`** alexander_smith30@outlook.com
- **`password:`** alexander_smith30