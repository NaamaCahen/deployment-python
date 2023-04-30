db_info = {'host': 'dpg-ch7989jhp8u9bo5tl7ug-a.frankfurt-postgres.render.com',
           'database': 'books_bodt',
           'psw': 'lTsUS23L9EYzFV3WKp7LV0PLhtjOrD81',
           'user': 'naama',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
