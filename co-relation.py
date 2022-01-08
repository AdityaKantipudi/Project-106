import plotly.express as px
import csv
import numpy as np

def plotfigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(data_path):
    marks_in_percent=[]
    days_present=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks_in_percent.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x":marks_in_percent,"y":days_present}

def find_co_relation(datasource):
     correlation=np.corrcoef(datasource["x"],datasource["y"])
     print("correleation between marks in percent and days present is",correlation[0,1])

def setup():
     data_path="Student Marks vs Days Present.csv"
     datasource=getDataSource(data_path)
     find_co_relation(datasource)
     plotfigure(data_path)

setup()
        