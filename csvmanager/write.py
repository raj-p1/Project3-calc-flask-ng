import os

class Write:
    @staticmethod
    def DataFrameToCSVFile(filename, df):
        return df.to_csv(os.path.abspath(filename), mode='a', float_format='%.2f', index=False, header=False)
