# Dependencies
import pandas as pd
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML
import warnings
warnings.filterwarnings('ignore')

def checkColumns(data):
    print(data.columns.values)

def checkContent(data):
    print(terror.head())
    
def getRowById(data,id):
    return (data.loc[data['eventid'] == id])

def getFieldEqualsValue(data,field):
    return ( data.loc[data[field].isnull() == False]['eventid'] )

def getRowLength(data):
    return len(data.columns)

def getRowCount(data):
    return len(data.index)
    
# Reading Data to Understand Structure
terror = pd.read_csv('../input/terrorism.csv',encoding='ISO-8859-1')
print( getRowCount(terror) )