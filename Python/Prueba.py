import pandas as pd
table = pd.read_csv(filepath_or_buffer=r"C:\Users\ERIK\Documents\Documentos\Projects\vgsales.csv") 
#name = pd.DataFrame(index=table, columns=["Name"]) # Create new column

print(table.loc[0])
print(table.shape)
print(table.columns)
print(table.tail()) 
