import urllib
import urllib.request
import os.path
from pathlib import Path


def retrieve(if_not_exist, url_string):
    data_folder = 'data'
    path = Path(url_string)
    local_path = "../" + data_folder + "/" + path.name
    if os.path.isfile(local_path):
        print("File exist")
    else:
        print("File not exist")
        excel_file = urllib.request.urlretrieve(url_string, local_path)
    return local_path


if __name__ == '__main__':
    url = "http://www.econ.yale.edu/~shiller/data/chapt26.xlsx"
    retrieve(False, url)



# excel = pd.read_excel(excel_file)
# excel.head()

# xls = pd.ExcelFile(url)
# df = xls.parse('Data', skiprows=[0, 1, 3, 4, 5, 6, 7], skip_footer=5, index_col=0)
# df.to_csv(csv_file)


