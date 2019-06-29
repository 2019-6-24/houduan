_anthor_ = "twz"
import pandas as pd

def searchData(name):
    df = pd.read_csv("test1.csv" )
    df1=df[df['house']== name]
    print(df1)

    a = df1['acreage']
    b = df1['avg_price']
    c = df1['louceng']
    d = df1['price']
    e = [a, b, c, d, df1['house']]
    return e

searchData("三里民居")



