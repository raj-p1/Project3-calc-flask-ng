from app.controllers.controller import ControllerBase
from flask import render_template

class OOPPrinciplesController(ControllerBase):
    @staticmethod
    def get():
        return render_template('oop_principles.html')
