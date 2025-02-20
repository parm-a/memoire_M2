Le document `annuaire_1951_index_proprietaires.csv` de ce dossier contient les données de l'Annuaire des propriétaires et des propriétés de Paris et du département de la Seine de l'année 1951, enrichies d'informations géographiques. Ces informations géographiques supplémentaires sont les coordonnées latitude-longitude des adresses (d'après la BAN), et les quartiers administratifs (chaque arrondissement comporte 4 quartiers).

Cet annuaire comporte, pour chaque personne possédant des immeubles à Paris : l'adresse de son domicile, et la liste des adresses des immeubles qu'elle possède. Cette personne peut être une personne physique (un particulier), ou une personne morale (une entreprise, un Etat, une municipalité, une organisation caritative, etc.). Les colonnes qui correspondent à l'immeuble parisien se terminent par le suffixe "_imm", et les colonnes correspondant aux domiciles des propriétaires ont le suffixe "_pers".

Ces données ont été extraites par des méthodes computationnelles et n'ont pas été relues à la main ; elles peuvent donc comporter des erreurs. Ce traitement informatique a été effectué par Aaron Parmentelat, dans le cadre du master "Humanités Numériques" de l'Ecole des Chartes, pour son mémoire encadré par Carmen Brando, Frédérique Mélanie et Gilles Postel-Vinay. Pour plus d'informations sur la chaîne de traitement informatique, aller voir https://github.com/parm-a/memoire_M2.

Pour chaque propriétaire, nous avons donc :
- son nom :
    - dans la colonne `nom_pers` si c'est un particulier
    - dans la colonne `org` si c'est une organisation 
- éventuellement prénom et civilité, dans les colonnes `prenom_pers` et `civilite_pers` respectivement, si il s'agit d'un particulier
- `index_total` est un index ou chaque propriétaire différent a un numéro différent. `__index_pers__` est exactement la même colonne

- l'adresse postale de son domicile, dans les colonnes `type_voie_pers` et `nom_voie_pers` (respectivement le numéro de l'immeuble dans la voie, le type de voie et le nom de la voie. Par exemple dans l'adresse `11 rue Michal`, `11` est le numéro de l'immeuble dans la voie, `rue` est le type de voie, et `Michal` est le nom de la voie)
- des informations complémentaires sur l'adresse de son domicile :
    - l'arrondissement dans `arr_pers` (si il s'agit adresse parisienne)
    - sa ville dans `ville_pers` (si il ne s'agit pas d'une adresse parisienne)
    - `loc_pers` contient une autre information, il peut s'agir de son département si ce n'est pas une adresse parisienne ; il peut s'agir de son pays si ce n'est pas une adresse en France
    - `part_pers` contient aussi des informations sur l'adresse de son domicile, en particulier sur son régime de propriété (essentiellement si il s'agit d'une copropriété ou d'une indivision, si c'est le cas)
- les coordonnées gégraphiques latitude-longitude de son domicile dans `lat_pers` et `lng_pers`, et c'est les mêmes informations sous forme de point geopandas dans les colonnes `coord_pers` et `geometry`. Ces coordonnées ont été associées à chaque adresse par le géocodeur de la BAN (cf. https://adresse.data.gouv.fr/base-adresse-nationale#4.4/46.9/1.7) et ne sont pas toujours exactes
- à partir de ces coordonnées géographiques, on associe un quartier administratif à chaque adresse, dans la colonne `quartier_pers`. Pour trouver ce quartier, on utilise les coordonnées de quartier disponibles sur le site d'Open Data Paris (cf. https://opendata.paris.fr/explore/dataset/quartier_paris/map/?disjunctive.c_ar&location=20,48.8932,2.36984&basemap=jawg.streets)
- de plus, nous avons des informations complémentaires du géocodeur sur l'adresse du domicile :
    - `result_type_pers` indique le niveau de précision de la réponse du géocodeur ; cela peut être une précision au niveau du numéro de la rue (`housenumber`), de la rue (`street`), ou de la municipalité (`municipality`)
    - `result_city_pers` indique la municipalité dans laquelle se trouve le point associé à l'adresse du domicile par le géocodeur

- `nveaux_codes` contient une liste des codes de tous les immeubles que cette personne possède. Les codes se présentent sous la forme "4592 : 3, 5" et signifie que pour la voie numéro 4592, cette personne possède les numéros 3 et 5. Le fichier `liste_rues_1951.csv` permet de décoder les numéros de voies, par exemple "4592" correspond à la place des Ternes
- `nb_codes` compte le nombre de codes différents. Par exemple, "4592 : 3, 5" compte pour un code
- `nb_imms` compte le nombre d'immeubles possédés par cette personne. Par exemple, "4592 : 3, 5" compte pour deux immeubles





