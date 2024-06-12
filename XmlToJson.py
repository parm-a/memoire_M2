# coding: utf-8
from bs4 import BeautifulSoup as bs
import glob
import re
import json
import os

path_to_target = '/home/aaron/Documents/M2/memoire_M2/annexe_pngs/crops/annexe_pero_copy/'

output_name = 'annexe.jsonl'

list_files = []

for fichier in sorted(os.listdir(path_to_target)):
	if fichier.endswith('.xml'):
		path_fichier = os.path.join(path_to_target, fichier)
		list_files.append(path_fichier)


#créer un fichier jsonl : unité textuelle TR
jsonFile = open(output_name,'w',encoding='utf8')

myLstJson = list()

for file in list_files:
	print(file)
	fichier = open(file, 'r')

	bs_content = bs(fichier, features='xml')
	
	TR_id = ""
	
	for TR in bs_content.find_all('TextLine'):
		print("J'ai trouve un TR")

		# recuperer l'ID du TR
		TR_id = TR['id']
		# recuperer le contenu de la dernière balise unicode des TR
		myTxt = TR.find_all('Unicode')[-1].get_text()
		#print(myTxt)
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
