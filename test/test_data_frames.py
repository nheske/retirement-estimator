import unittest
import util.download as download
import pandas as pd


class DownloadTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_shiller(self):
        shiller_excel_url = "http://www.econ.yale.edu/~shiller/data/chapt26.xlsx"
        excel_file_path = download.retrieve(False, shiller_excel_url)
        df = pd.read_excel(excel_file_path, engine='openpyxl', sheet_name='Data', skiprows=7, usecols = "A:U") #xlrd removed support for xlsx  https://stackoverflow.com/questions/65250207/pandas-cannot-open-an-excel-xlsx-file
        print(df.head())


if __name__ == '__main__':
    unittest.main()
