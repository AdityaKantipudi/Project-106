from os import supports_follow_symlinks
import plotly.express as px
import csv
import numpy as np

def plotfigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffe_in_ml=[]
    sleep_in_hours=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            coffe_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x":coffe_in_ml,"y":sleep_in_hours}

def find_co_relation(datasource):
     correlation=np.corrcoef(datasource["x"],datasource["y"])
     print("correleation between coffee in ml and sleep in hours is",correlation[0,1])

def setup():
     data_path="cups of coffee vs hours of sleep.csv"
     datasource=getDataSource(data_path)
     find_co_relation(datasource)
     plotfigure(data_path)

setup()
        








