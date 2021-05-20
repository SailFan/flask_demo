# encoding: utf-8
# @Time    : 2021/5/19 11:39 下午
# @Author  : Sail
# @File    : manager.py
# @Software: PyCharm
from app import create_app



app = create_app()

if __name__ == "__main__":
    app.run("0.0.0.0",debug = True)