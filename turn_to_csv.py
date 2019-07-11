

filename = "C:\\Users\\Ryan Howe\\Documents\\Python\\Shower\\clean_shower.txt"

csvfile = "clean_shower.csv"
import pandas as pd
df = pd.read_fwf(filename)
df.to_csv(csvfile)