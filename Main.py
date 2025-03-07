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
        self.design()

    def Config_db(self):
        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        banco_de_dados = SQLAlchemy(app)

        # Terminar de programar o banco de dados

    def tela(self):
        self.setWindowTitle("BlackList")
        self.setFixedSize(900, 600)

        widget_central = QWidget()
        layout_principal = QVBoxLayout()

        self.mudar_frame = QStackedWidget()
        layout_principal.addWidget(self.mudar_frame)

        # ------------------------------------------
        self.frame_inicial = QFrame()
        frame_inicial_layout = QVBoxLayout()
        self.frame_inicial.setLayout(frame_inicial_layout)

        self.title_inicial = QLabel("Registrar")
        self.title_inicial.setMaximumSize(700, 50)
        self.title_inicial.setAlignment(Qt.AlignCenter)

        self.button_frame_resgistros = QPushButton("Ver Registros")
        self.button_frame_resgistros.setMaximumSize(700, 40)
        self.button_frame_resgistros.clicked.connect(self.mudar_frame_registros)

        self.frame_inserir = QFrame()
        frame_inserir_layout = QGridLayout()
        self.frame_inserir.setLayout(frame_inserir_layout)

        self.entrada_nome = QTextEdit()

        self.entrada_idade = QTextEdit()

        self.entrada_cidade = QTextEdit()

        self.entrada_estado = QComboBox()

        self.entrada_telefone = QTextEdit()

        self.entrada_email = QTextEdit()

        self.infos = QTextBlock()

        frame_inicial_layout.addWidget(self.title_inicial)
        frame_inicial_layout.addWidget(self.button_frame_resgistros)
        frame_inicial_layout.addWidget(self.frame_inserir)

        # -----------------------------------------
        self.frame_registros = QFrame()
        frame_registros_layout = QVBoxLayout()
        self.frame_registros.setLayout(frame_registros_layout)

        self.title_inicial2 = QLabel("Registros")
        self.title_inicial2.setMaximumSize(700, 50)
        self.title_inicial2.setAlignment(Qt.AlignCenter)

        self.button_frame_registrar = QPushButton("Registrar")
        self.button_frame_registrar.setMaximumSize(700, 40)
        self.button_frame_registrar.clicked.connect(self.mudar_frame_registrar)

        self.frame_buttons = QFrame()
        frame_buttons_layout = QVBoxLayout()
        self.frame_buttons.setLayout(frame_buttons_layout)

        self.button_safe = QPushButton("Categoria 1")
        self.button_safe.setMaximumSize(1000, 40)

        self.button_warning = QPushButton("Categoria 2")
        self.button_warning.setMaximumSize(1000, 40)

        self.button_Danger = QPushButton("Categoria 3")
        self.button_Danger.setMaximumSize(1000, 40)

        frame_buttons_layout.addWidget(self.button_safe)
        frame_buttons_layout.addWidget(self.button_warning)
        frame_buttons_layout.addWidget(self.button_Danger)

        frame_registros_layout.addWidget(self.title_inicial2)
        frame_registros_layout.addWidget(self.button_frame_registrar)
        frame_registros_layout.addWidget(self.frame_buttons)

        # -----------------------------------------
        self.mudar_frame.addWidget(self.frame_inicial)
        self.mudar_frame.addWidget(self.frame_registros)

        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def design(self):
        self.setStyleSheet("""
            background-color: black;
        """)

        self.title_inicial.setStyleSheet("""
            border: 1px solid white;
            color: white;
        """)

        self.title_inicial2.setStyleSheet("""
            border: 1px solid white;
            color: white;
        """)

        self.frame_inserir.setStyleSheet("""
            border: 1px solid white;
        """)

        self.frame_registros.setStyleSheet("""
            border: 1px solid white;
        """)

        self.button_frame_resgistros.setStyleSheet("""
            QPushButton {
                border: 1px solid white;
                color: white;
            }
            
            QPushButton:hover {
                background-color: white;
                color: black;
            }
        """)

        self.frame_buttons.setStyleSheet("""
            QPushButton {
                border: 1px solid white;
                color: white;
            }
            
            QFrame {
                border: none;
            }
        """)

        self.button_frame_registrar.setStyleSheet("""
            QPushButton {
                border: 1px solid white;
                color: white;
            }

            QPushButton:hover {
                background-color: white;
                color: black;
            }
        """)

    def mudar_frame_registros(self):
        self.mudar_frame.setCurrentWidget(self.frame_registros)

    def mudar_frame_registrar(self):
        self.mudar_frame.setCurrentWidget(self.frame_inicial)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sistema = Sistema()
    sistema.show()
    sys.exit(app.exec_())
