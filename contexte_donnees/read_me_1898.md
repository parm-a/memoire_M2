Le document `annuaire_1898_avec_quartiers.csv` de ce dossier contient les données de l'Annuaire des propriétaires et des propriétés de Paris et du département de la Seine de l'année 1898, enrichies d'informations géographiques. Ces informations géographiques supplémentaires sont les quartiers administratifs (chauque arrondissement comporte 4 quartiers).

Cet annuaire comporte pour chaque immeuble parisien, le nom de son propriétaire, et l'adresse du domicile de ce dernier.

Pour les adresses des immeubles parisiens, il existe deux cas : soit l'immeuble se trouve sur une voie qui ne traverse qu'un seul quartier ; soit il se trouve dans une rue qui traverse plusieurs quartiers.
- dans le premier cas, qui correspond à 65% des adresses, on obtient directement l'information du quartier de l'immeuble à partir de l'information du quartier de la voie. Par exemple, la "rue Michal" dans le 13e arrondissement, et se trouve uniquement dans le quartier numéro 51, appelé "Maison blanche" ; on en déduit facilement que toutes les adresses de cette rue se trouvent dans ce quartier.
- dans le second cas, donc pour les 35% restants, on ne peut pas obtenir le quartier de la voie directement car la voie traverse plusieurs quartiers. Pour trouver le quartier de ces adresses, on va leur associer des coordonnées géographiques latitude-longitude, puis constater dans quel quartier ces coordonnées se trouvent. On utilise un géocodeur, qui permet d'associer des coordonnées géographiques à une adresse ; on utilise le géocodeur du gouvernement. Ensuite, on utilise les coordonnées des quartiers parisiens disponibles sur le site Open Data Paris, pour associer un quartier à chaque adresse.

Pour les adresses des domiciles, on n'a pas d'information de quartier facilement disponible ; on applique donc le géocodeur à 100% des adresses, et on procède à la même méthode pour déterminer leur quartier.

Les colonnes qui correspondent à l'immeuble parisien se terminent par le suffixe "_imm", et les colonnes correspondant aux domiciles des propriétaires ont le suffixe "_pers".

Ces données sont donc enrichies des quartiers de l'immeuble, et du domicile du propriétaire. Cependant, ces informations géographiques n'ont pas été vérifiées à la main, et sont donc passibles d'erreurs.

Ces traitements informatiques pour obtenir ces données géographiques complémentaires ont été effectués par Aaron Parmentelat, dans le cadre du master "Humanités Numériques" de l'Ecole des Chartes, pour son mémoire encadré par Carmen Brando, Frédérique Mélanie et Gilles Postel-Vinay. Pour plus d'informations, aller voir https://github.com/parm-a/memoire et https://github.com/parm-a/memoire_M2.

Note : certains immeubles sont comptés plusieurs fois, car ils se situent au coin de 2 voies et disposent de deux adresses postales. Pour supprimer ces doublons, il suffit d'enlever les "0.1" dans la colonne "Entree=0.1_Parisien=1.0_Nonparisien=0.0".
