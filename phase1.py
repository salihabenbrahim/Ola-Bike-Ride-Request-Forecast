import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt

## Chargement et aperçu des données

# Charger les données
file_path = "C:/Users/salih/OneDrive/Documents/DATA SCIENCE/bike-sharing-demand/train.csv"
data = pd.read_csv(file_path)

# Afficher les premières lignes
#print(data.head())

# Vérifier les infos générales
#print(data.info())

# Vérifier les valeurs manquantes
#print(data.isnull().sum())


##Nettoyage et transformation des données

#Convertir la colonne datetime en type datetime
data["datetime"] = pd.to_datetime(data["datetime"])

#Extraire des informations utiles (année, mois, jour, heure, jour de la semaine)
data["year"] = data["datetime"].dt.year
data["month"] = data["datetime"].dt.month
data["day"] = data["datetime"].dt.day
data["hour"] = data["datetime"].dt.hour
data["weekday"] = data["datetime"].dt.weekday

#Vérifier et traiter les valeurs aberrantes
plt.figure(figsize=(10, 5))
sns.boxplot(data["count"])
plt.show()

#Supprimer les outliers avec la méthode IQR
Q1 = data["count"].quantile(0.25)  # Premier quartile
Q3 = data["count"].quantile(0.75)  # Troisième quartile
IQR = Q3 - Q1  # Intervalle interquartile

# Seuils pour définir les outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrer les données en supprimant les valeurs aberrantes
data = data[(data["count"] >= lower_bound) & (data["count"] <= upper_bound)]

##Visualisation des données

#Distribution de la variable cible (count)
sns.histplot(data["count"], bins=30, kde=True)
plt.show()

#Relation entre les heures et la demande de courses
plt.figure(figsize=(12, 6))
sns.boxplot(x="hour", y="count", data=data)
plt.title("Nombre de courses en fonction de l'heure")
plt.show()

#Effet de la météo sur la demande
sns.barplot(x="weather", y="count", data=data)
plt.show()


##Gestion des données catégorielles

data = pd.get_dummies(data, columns=["season", "weather"], drop_first=True)


plt.figure(figsize=(10, 5))
sns.boxplot(data["count"])
plt.show()
