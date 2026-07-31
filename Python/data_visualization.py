import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos limpios
df = pd.read_csv('netflix_titles_cleaned.csv')

# Configurar el estilo visual general
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# --- GRAFICO 1: Top 10 Paises con mayor produccion ---
plt.figure(figsize=(10, 6))
# Limpiamos un poco los paises si hay multiples combinaciones
top_countries = df['country'].value_counts().head(10)
ax = sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title('Top 10 Paises con Mayor Produccion de Contenido en Netflix', fontsize=14, fontweight='bold')
plt.xlabel('Cantidad de Titulos')
plt.ylabel('Pais')
plt.tight_layout()
plt.savefig('../reports/figures/top_countries.png', dpi=300) # Lo guarda en tu carpeta de reportes
plt.show()

# --- GRAFICO 2: Evolucion de lanzamientos por año (Peliculas vs Series) ---
plt.figure(figsize=(12, 6))
df_filtered = df[df['release_year'] >= 2010] # Filtrar años recientes para mayor claridad
yearly_trend = df_filtered.groupby(['release_year', 'type']).size().unstack().fillna(0)

yearly_trend.plot(kind='line', marker='o', linewidth=2.5)
plt.title('Evolucion Historica de Lanzamientos (2010 en adelante)', fontsize=14, fontweight='bold')
plt.xlabel('Año de Lanzamiento')
plt.ylabel('Numero de Titulos')
plt.legend(title='Tipo de Contenido')
plt.tight_layout()
plt.savefig('../reports/figures/yearly_trend.png', dpi=300)
plt.show()