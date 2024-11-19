# Gaia_synthese, GAIA_planning

Cette application fait une synthèse du plan de formations issu de GAIA (GAIA - Accès gestionnaire (Orange))

GAIA_synthese : Extraction du plan de formation, du planning et des inscriptions
GAIA_planning : Version light qui ne fait que l'extraction du planning de formation
--------------------------------------------------------------
Une structure département a été mise en place avec une charte de nommage :

Libellé des dispositifs :  Nom_du_Bassin N°_circo Nom_dispo
Le N°_circo n'est pas obligatoire.
Ex : MONTLUCON 2 AUTRES DOMAINES ANIM PEDA - 6 H
pour la circonscription de Montluçon 2.

Libellé des Modules : Nom_module Nb_heure H
Exemple : PARCOURS MATERNELLE DES GESTES POUR ENSEIGNER 6H

--------------------------------------------------------------
Prérequis :
--------------------------------------------------------------
python 3.12 minimum 

Télécharger la dernière version 
https://www.python.org/downloads/

demander à la DSI son installation si vous n'avez pas les droits.

--------------------------------------------------------------
Configuration avant de commencer :
--------------------------------------------------------------

Ouvrir un fenêtre "invite de commande" en tapant  cmd dans la barre de recherche Windows

pour installer les dépendances, saisir :
pip install -r requirements.txt

Maintenant, vous pouvez utiliser GAIA_synthese_v1.0 en double cliquant dessus

----------------------------------------------------------------
Comment l'Utiliser
----------------------------------------------------------------

Ouvrir un session GAIA dans Firefox 
ATTENTION ne fonctionne qu'avec Firefox

Executer GAIA_synthese ou GAIA_planning en double cliquant sur le programme
La synthèse se trouve ensuite dans le dossier Output