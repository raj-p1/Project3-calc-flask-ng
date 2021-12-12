"""Testing CSV Functions"""
import pandas
import os.path
from csvmanager.write import Write
from csvmanager.read import Read
import pandas as pd

def test_write_csv(value_1, value_2, result, operation):
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = 'csv_output.csv'
    path = 'tests/test_data'
    fullPath = path + '/' + filename
    name_dict = {
        'value1': [value_1],
        'value2': [value_2],
        'result': [result],
        'operation':[operation]

    }

    df = pd.DataFrame(name_dict)
    #Act

    Write.DataFrameToCSVFile(fullPath,df)
    #Assert
    assert os.path.exists(fullPath)

def test_read_csv():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = 'csv_output.csv'
    path = 'tests/test_data'
    fullPath = path + '/' + filename
    #Act
    df = Read.DataFrameFromCSVFile(fullPath)
    #Assert
    assert type(df) is pandas.DataFrame
    return df.values