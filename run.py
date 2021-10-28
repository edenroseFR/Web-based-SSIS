from ssis import create_app
from dotenv import load_dotenv

app = create_app()

load_dotenv('.env')

if __name__ == '__main__':
    app.run()
    