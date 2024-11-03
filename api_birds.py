# -*- coding: utf-8 -*-
"""api-birds.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eWMabw7yTGNd4JST-HPQTbC35VVzluVS
"""

import os
import json
import zipfile

from kaggle import KaggleApi

try:
    # Inicializando a API do Kaggle
    api = KaggleApi()
    api.authenticate()

    # Baixando o conjunto de dados
    api.dataset_download_files('rahmasleam/bird-speciees-dataset', path='.', unzip=False)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

zip_file = 'bird-speciees-dataset.zip'

# Verifica se o arquivo existe
if os.path.exists(zip_file):
    # Descompacta o arquivo
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('.')
else:
    print(f"O arquivo {zip_file} não foi encontrado.")

basepath = "Bird Speciees Dataset"

american_goldfinch = "AMERICAN GOLDFINCH"
barn_owl = "BARN OWL"
carmine_bee_eater = "CARMINE BEE-EATER"
downy_woodpecker = "DOWNY WOODPECKER"
emperor_penguin = "EMPEROR PENGUIN"
flamingo = "FLAMINGO"

# Nomes das pastas das espécies
species_folders = [
    american_goldfinch,
    barn_owl,
    carmine_bee_eater,
    downy_woodpecker,
    emperor_penguin,
    flamingo
]

# Criar um dicionário para armazenar os caminhos das imagens
species_images = {}

for species in species_folders:
    species_path = os.path.join(basepath, species)
    # Listar todos os arquivos de imagem na pasta da espécie
    image_files = os.listdir(species_path)

    # Criar uma lista de caminhos completos para cada imagem
    image_paths = [os.path.join(species_path, img) for img in image_files if img.endswith(('.png', '.jpg', '.jpeg'))]

    # Adicionar ao dicionário
    species_images[species] = image_paths

# Salvar o dicionário como um arquivo JSON
json_file_path = 'species_images.json'
with open(json_file_path, 'w') as json_file:
    json.dump(species_images, json_file)

print(f'JSON file saved to {json_file_path}')