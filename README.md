# CRUD WEB APPLICATION (CCC181 Assignment)

![crudwebapp](https://github.com/edenroseFR/Web-based-SSIS/blob/main/readme_files/image.PNG)
## FEATURES
- Display data
- Add data
- Edit data
- Delete data
- Search data

## SETUP & INSTALLATION
1. Clone the repository to your local machine by running the following command on your command-line.
```bash
clone 'https://github.com/edenroseFR/Web-based-SSIS.git'
```
2. Install all the requirements.
```bash
pip install -r requirements.txt
```
3. Create a dotenv file.
```bash
type nul > .env
```
4. Open the .env file and write the following:
```python
DB_HOST=your_database_host
DB_NAME=ssisdb
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
SECRET_KEY=any_string_will_do

CLOUD_NAME = your_cloudinary_name
API_KEY = your_cloudinary_api_key
API_SECRET = your_cloudinary_api_secretkey
PHOTO_UPLOAD = cloud
```
5. Create a flaskenv file.
```bash
type nul > .flaskenv
```
6. Open the .flaskenv file and make sure it contains the following:
```python
FLASK_APP=ssis
FLASK_ENV=development
FLASK_RUN_PORT=8080
```
7. In your MySQL IDE, execute the script.sql file located in `WEB_BASED_SSIS/db_script`
8. To create your own login credential, run add_admin.py. Make sure you are inside `WEB_BASED_SSIS` directory before executing the following:
```bash
python add_admin.py
```
9. Make sure you see the **Admin added!** in your console, before moving to the next step.

## RUNNING THE APP
1. Activate the virtual environment
```bash
cd venv/Scripts/activate
```
2. Run
```bash
flask run
```
