Repository pour publier mes code et données de mémoire de M2, dans le cadre du master "Humanités Numériques" de l'Ecole des Chartes


Mon mémoire s'intéresse à la propriété, copropriété et multi-propriété à Paris en 1898 et 1951. Il utilise pour ce faire des données d'annuaires de propriétaires de ces deux années. Ce travail a été effectué sous la direction de Carmen Brando, Frédérique Mélanie-Béquet et Gilles Postel-Vinay.

Notre objectif est de passer des numérisations des pages de l'annuaire à un tableau CSV contenant les informations rangées. Nous souhaitons aussi associer chaque adresse à des coordonnées géographiques et un quartier parisien.

# Chaîne de traitement

## Pré-traitement :
- recouvrir les publicités d'un rectangle uni : **Gimp**
- mettre les images en noir et blanc et augmenter le contraste et la luminosité : librairies bash **GhostScript** et **ImageMagick**
cf. 


- segmentation en trois images différentes correspondant aux trois colonnes : **modèle segemntation-v8 de YOLO, par Ultralytics** (cf. )
- 
