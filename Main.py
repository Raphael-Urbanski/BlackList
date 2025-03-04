import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


class Sistema(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tela()

    def Config_db(self):
        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        banco_de_dados = SQLAlchemy(app)

        # Terminar de programar o banco de dados

    def tela(self):
        self.setWindowTitle("BlackList")
        self.setFixedSize(500, 500)
