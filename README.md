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
DB_NAME=your_database_name
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
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

## RUNNING THE APP
```bash
flask run
```
