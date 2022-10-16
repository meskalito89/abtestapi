from flask import Flask
from sqlalchemy import create_engine, select

engine = create_engine("sqlite:///database.sqlite")
print(engine)


# app = Flask(__name__)

# @app.route('/')
# def main():
#     with engine.connect() as con:
#         data = select(con['EmployeeName'])
#     return '<h1>some text</h1>'



