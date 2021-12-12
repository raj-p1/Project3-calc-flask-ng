from app.controllers.controller import ControllerBase
from flask import render_template

class OOPTermsController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oop_terms.html')
