import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    dfObj = pd.read_csv(csv_file_path, header = None)
    rowList = [list(row) for row in dfObj.values]
    return rowList