Repository pour publier mes code et données de mémoire de M2, dans le cadre du master "Humanités Numériques" de l'Ecole des Chartes


Mon mémoire s'intéresse à la propriété, copropriété et multi-propriété à Paris en 1898 et 1951. Il utilise pour ce faire des données d'annuaires de propriétaires de ces deux années. Ce travail a été effectué sous la direction de Carmen Brando, Frédérique Mélanie-Béquet et Gilles Postel-Vinay.

Notre objectif est de passer des numérisations des pages de l'annuaire à un tableau CSV contenant les informations rangées. Nous souhaitons aussi associer chaque adresse à des coordonnées géographiques et un quartier parisien.

# Chaîne de traitement

## 0. Pré-traitement :
- recouvrir les publicités d'un rectangle uni : **Gimp**
- mettre les images en noir et blanc et augmenter le contraste et la luminosité : librairies bash **GhostScript** et **ImageMagick**

cf. `0_commandes_pre_traitement.md`

<br>

## 1. Segmentation
Segmentation en trois images différentes correspondant aux trois colonnes. Utilisation de **modèle segemntation-v8 de YOLO, par Ultralytics** fine-tuné pour nos données

cf. le modèle `1_modele_YOLO_best.pt` et le notebook `1_application_YOLO.ipynb`

<br>

## 2. Reconnaissance de caractères
Nous avons procédé à l'HTR avec l'outil **PERO-OCR**

cf. le dossier `2_PERO_OCR`. Note : il manque le dossier config car il est trop lourd pour GitHub (400 MB)

<br>

## 3. Reconnaissance d'entités nommées
- convertion des XML en JSON-L avec le script de Frédérique Mélanie-Becquet `3_1_XmlToJson.py`
Nous avons procédé au NER avec l'outil **Prodigy**

cf. notebook `3_2_NER.ipynb` qui permet : d'appliquer le NER ligne par ligne (modèle de NER : `3_modele_prodigy`), de séparer les entrées, de traduire les codes de voies en noms de voie explicite, et d'appliquer le géocodeur du gouvernement. Input : JSON-L. Output : deux fichiers CSV, un premier où une ligne = un propriétaire et un deuxième où une ligne = un immeuble.

<br>

## 4. Analyse : production des cartes et statistiques sur ces données
cf. notebook ``

<br>

NB : Ces données n'ont pas été relues et comporte des erreurs.
