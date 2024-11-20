import pandas as pd

raw_file_path = "../openaq_data.csv"

processed_file_path = "../../processed_data.pkl"

print(f'Getting data file at: {raw_file_path}')
try:
    data = pd.read_csv(
        raw_file_path,
        sep=";",  
        header=0,  
        skipinitialspace=True,  
        encoding='utf8'  
    )
    print("Raw file read successfully.")
except Exception as e:
    print(f"Error reading the raw file: {e}")
    exit(1)

coord_data = data['Coordinates'].str.split(',', expand=True)
if coord_data.shape[1] == 2:
    data[['Latitude', 'Longitude']] = coord_data.astype(float)
else:
    print("Erreur : les coordonnées ne peuvent pas être séparées correctement. Veuillez vérifier le format.")
    exit(1)

molar_masses = {
    'O3': 48,     # Ozone
    'CO': 28,     # Monoxyde de carbone
    'NO2': 46,    # Dioxyde d'azote
    'SO2': 64,    # Dioxyde de soufre
    'PM10': None, # Particules (pas de conversion nécessaire)
    'PM2.5': None,# Particules fines ((pas de conversion nécessaire))
    'NO': 30,     # Monoxyde d'azote
    'NOX': 38     # Moyenne pondérée : (30 + 46) / 2
}

print("Conversion column 'Unit' to have the same mesure for compairison")

def convert_to_ugm3(row):
    """
    Convertit les unités de concentration en µg/m³ et met à jour l'unité correspondante.

    Args:
        row (pandas.Series): Une ligne du DataFrame contenant les colonnes `Unit`, `Pollutant`, et `Value`.

    Returns:
        tuple: La concentration convertie (ou inchangée) et l'unité mise à jour.
    """
    unit = row['Unit']
    pollutant = row['Pollutant']
    value = row['Value']
    
    # Récupération de la masse molaire du polluant
    molar_mass = molar_masses.get(pollutant, None)
    
    # Cas 1 : Unité déjà en µg/m³ 
    if unit == 'µg/m³':
        return value, 'µg/m³'
    
    # Cas 2 : Unité en ppm
    elif unit == 'ppm' and molar_mass:
        converted_value = value * (molar_mass / 24.45)  # Conversion ppm -> µg/m³
        return converted_value, 'µg/m³'

    # Cas 3 : Unité en ppb
    elif unit == 'ppb' and molar_mass:
        converted_value = value * (molar_mass / 24.45) / 1000  # Conversion ppb -> µg/m³
        return converted_value, 'µg/m³'

    # Cas 4 : Unité non supportée (on conserve la valeur d'origine)
    else:
        return value, unit 



data[['Value', 'Unit']] = data.apply(
    lambda row: pd.Series(convert_to_ugm3(row)), axis=1
)

# Sauvegarder les données traitées dans un fichier pickle
data.to_pickle(processed_file_path)
print(f"Données traitées sauvegardées dans {processed_file_path}")