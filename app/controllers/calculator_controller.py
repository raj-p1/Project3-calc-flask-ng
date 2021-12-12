from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from tests.csv_test import test_write_csv, test_read_csv
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '':
            error = 'Please enter value 1 '
        elif request.form['value2'] == '':
            error = 'Please enter value 2'
        else:
            flash('This is your result')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            test_write_csv(value1, value2,result,operation)
            test_store = list(test_read_csv())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result, test_store=test_store)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')






