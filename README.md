Ceci est un dossier pour publier les scripts et données de mémoire de M2 d'Aaron Parmentelat, dans le cadre du master "Humanités Numériques" de l'Ecole des Chartes.

Ce mémoire s'intéresse à la propriété, copropriété et multi-propriété à Paris en 1898 et 1951. Il utilise pour ce faire des données d'annuaires de propriétaires de ces deux années. Ce travail a été effectué sous la direction de Carmen Brando, Frédérique Mélanie-Becquet et Gilles Postel-Vinay.

Notre objectif est de passer des numérisations des pages de l'annuaire de l'année 1951 à un tableau CSV contenant les informations rangées dans des colonnes "nom propriétaire", "adresse", etc. Nous souhaitons aussi associer chaque adresse à des coordonnées géographiques et un quartier parisien.

De plus du contexte supplémentaire sur les données est disponible dans le dossier `contexte_donnees`.


# Chaîne de traitement

## 0. Pré-traitement :
- Nous avons recouvert les publicités d'un rectangle uni avec **Gimp**
- Nous avons effectué un pré-traitement sur les images, pour les mettre en noir et blanc et augmenter le contraste et la luminosité, à l'aide des librairies bash **GhostScript** et **ImageMagick**. cf. `/notebooks_1951/0_commandes_pre_traitement.md` pour les commandes de pre-traitement utilisées.

<br>

## 1. Segmentation
Nous avons segmenté chaque image en trois images différentes correspondant aux trois colonnes. Pour ce faire, nous avons utilisé le **modèle segmentation YOLO-v8, par Ultralytics** fine-tuné pour nos données sur un jeu de 75 pages.

Le script se trouve à l'emplacement `/notebooks_1951/1_application_YOLO.ipynb`, et le modèle `/modeles_1951/1_YOLO/best.pt`. Il a été fine-tuné à partir du jeu d'entrainement `/donnees_entrainement_1951/donnees_anotees_roboflow_segmentation`.

Le script prend en input des pages entières (ici au format PNG) et a comme output les colonnes découpées (au format JPEG).

<br>

## 2. Reconnaissance de caractères
Nous avons procédé à la reconnaissance de caractères avec l'outil **PERO-OCR** (plus d'informations sur https://github.com/DCGM/pero-ocr). Le code se trouve dans le notebook `/notebooks_1951/2_PERO_OCR.ipynb`, et utilise des fonctions définies dans le fichier `/notebooks_1951/pipeline.py` ainsi que la configuration contenue dans le dossier `/modeles_1951/2_config_PERO`.

Le script prend en input les colonnes découpées (format JPEG) obtenues à l'étape précédente, et a comme output le texte extrait (aux formats : XML-ALTO, XML, TXT pour le texte, et PNG pour le détection des lignes)

<br>

## 3. Reconnaissance d'entités nommées

Nous convertissons dans un premier temps les fichiers XML en un fichier JSON-L (format JSON Lignes). Nous utilisons pour ce faire un script élaboré par Frédérique Mélanie-Becquet, se trouvant au chemin `/notebooks_1951/XmlToJson.py`. Notons qu'il est utile de copier uniquement les XML dans un nouveau dossier pour appliquer le script, afin ne pas prendre en compte les XML-ALTO et ne pas avoir l'information en double.


Ensuite, nous pouvons trier ce texte en associant à chaque élément une étiquette : nom de propriétaire, adresse, etc. Cette étape nous permettra de constituer cette information sous la forme d'un tableau, comme nous avons déjà pour l'année 1898.

Pour effectuer ce tri, nous utilisons la reconnaissance d'entités nommées (NER), qui permet à un algorithme d'intelligence artificielle d'"apprendre" quelles informations doivent être associées à quelles étiquettes à partir d'annotations. Nous avons donc procédé à l'annotation de 1160 lignes de l'annuaire avec l'outil **Prodigy**, et ensuite entrainé un modèle de NER grâce à **Spacy**. Ce modèle se trouve au chemin `modeles_1951/3_Prodigy/model-best`. Notons que nous avons entraîné plusieurs modèles et choisi le meilleur parmi eux.

Le notebook `/notebooks_1951/3_NER.ipynb` permet d'appliquer ce modèle de NER ligne par ligne, de séparer les différentes entrées de l'annuaire, de traduire les codes de voies en noms de voie explicite, et enfin d'appliquer le géocodeur de la Base Adresse Nationale (BAN) sur toutes les adresses. L'input est donc le contenu de l'annuaire au format JSON-L, et l'output est composé de deux tableaux CSV : un où une ligne du tableau correspond à un propriétaire, et un où une ligne du tableau correspond à un immeuble parisien.

<br>

## 4. Analyse

Ces données sont analysées *via* la production de statistiques et cartes interactives, contenues dans le dossier `cartes_et_figures`. De plus, le script pour leur production se trouve à `/notebooks_1951/4_analyses.ipynb`.

<br>

Notes :
1. Ces données n'ont pas été relues et comportent des erreurs.
2. Toutes ces étapes sont disponibles pour la page 3 de l'annuaire ordonné par nom de propriétaire, dans le dossier `exemple du traitement sur la page d-3`
3. Par contrainte d'espace de stockage, les étapes intermédiaires ne sont pas disponibles pour toutes les pages. Néanmoins elles sont disponibles pour un échantillon de 15 pages, dans le dossier `sample_1951`. Ce dossier contient les étapes suivantes :
- `pages_entieres_png` (données initiales)
- `crops_colonnes_jpg` (colonnes découpées par le modèle de segmentation fine-tuné à partir du modèle de YOLO-v8)
- `pero` et `pero_liste_annuaires` (texte extrait de ces colonnes par PERO-OCR ; notons que ces résultats sont contenus dans le dossier `pero` pour les pages de l'annuaire ordonnées par voie parisienne, et dans `pero_liste_annuaires` pour les pages de l'annuaire ordonnées par le nom du propriétaire)
- `contenu_echantillon.jsonl` (texte extrait des pages de l'annuaire par nom de propriétaires, dans le format JSON)
- `df_par_nom_complet_1951.csv` et `df_par_proprio_complet_1951.csv`, les deux tableaux CSV finaux, après l'application du modèle de NER.
