import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

table = pd.read_csv(filepath_or_buffer=r"C:\Users\ERIK\Documents\Documentos\Projects\vgsales.csv")

#What were the top 5 most sold games?
top_sales = table[['Name', 'Global_Sales']].nlargest(5, 'Global_Sales')
top_sales.plot.bar(title='Top 5 most sold games', xlabel='Name', ylabel='Global Sales (millions)')
plt.show()


#In what year did Wii sell the most?

sales_year = table[['Platform', 'Year', 'Global_Sales']]
sales_year['Year']  = sales_year['Year'].convert_dtypes()
num_wii = sales_year['Platform']=='Wii' 
wii_sales = sales_year[num_wii][['Year', 'Global_Sales']]
per_year = wii_sales.groupby('Year')['Global_Sales'].sum()
per_year.plot.bar(title='Wii Global Sales per Year', xlabel='Year', ylabel='Global Sales (millions)')
plt.show()

#North-American and European sales move together; most titles sell little in both
sns.scatterplot(data=table, x='EU_Sales', y='NA_Sales')
plt.show()

#Which genre has the most titles?

table['Genre'].value_counts().plot.bar(title='#Titles per Genre', xlabel='Genres', ylabel='#Titles')
plt.show()
