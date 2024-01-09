import pandas as pd
import numpy as np
file_path = 'world_alcohol.csv'
world= pd.read_csv(file_path)
print("Dimensions/Shape of the World Alcohol Consumption Dataset:")
print(world.shape)
print("\nColumn Names:")
print(world.columns)
