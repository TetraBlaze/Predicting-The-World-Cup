import pandas as pd

world_cup_data = pd.read_csv("worldcupdata.csv", encoding="latin-1") #Loading the data from the csv file. 

world_cup_data.info()