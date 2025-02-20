# coding: utf-8
# import librairies
from bs4 import BeautifulSoup as bs
import glob
import re
import json
import os

# définition des path
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
path_to_target = os.path.join(parent_dir, 'sample_1951/pero_liste_annuaires')
output_path = os.path.join(parent_dir, "sample_1951/contenu_echantillon.jsonl")

# création d'une liste avec les noms de fichiers qui nous intéressent (xml)
list_files = []
for fichier in sorted(os.listdir(path_to_target)):
	if fichier.endswith('.out.xml'):
		path_fichier = os.path.join(path_to_target, fichier)
		list_files.append(path_fichier)

# initialisation du fichier JSON-L de sortie
jsonFile = open(output_path,'w',encoding='utf8')
myLstJson = list()

# Extraction du texte en itérant sur chaque XML, pour en extraire les informations et les rajouter dans le JSON-L
for file in list_files:
	# On ouvre le fichier XML et on le lit
	print(file)
	fichier = open(file, 'r')
	bs_content = bs(fichier, features='xml')
	TR_id = ""
	
	# Si on trouve un objet de type "TextLine" (appelé ensuite TR : Text Region)
	for TR in bs_content.find_all('TextLine'):
		print("Lecture de la TR")

		# On récupère l'ID de la TR
		TR_id = TR['id']
		# On récupèrer le contenu de la dernière balise unicode des TR
		myTxt = TR.find_all('Unicode')[-1].get_text()
		myTxt=re.sub(r'[\n\r]\s*',' ',myTxt)

		myTempDict = dict()
		myTempDict["text"] = myTxt
		myTempDict["meta"] = dict()
		myTempDict["meta"]["file_name"]=str(file)
		myTempDict["meta"]["TR_id"]=str(TR_id)
		
		# allow_nan = permet du jsonl (pas d'indentation)
		# ensure_ascii = gérer les accents
		jsonFile.write(json.dumps(myTempDict, allow_nan=True,ensure_ascii=True))
		jsonFile.write("\n")
