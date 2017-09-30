# Dependencies
import pandas as pd
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML
import warnings
warnings.filterwarnings('ignore')

# Reading Data to Understand Structure
terror = pd.read_csv('../input/terrorism.csv',encoding='ISO-8859-1')
print( terror.head() )
