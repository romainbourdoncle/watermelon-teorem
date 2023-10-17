# théorème de la pastèque
Un visualiseur dynamique développé pour accompagner la résolution d'un problème mathématique faisant partie d'un projet pédagogique plus large. L'application utilise Matplotlib pour permettre une exploration dynamique de la constance de la surface dans un cercle divisé par des rayons partant d'un point intérieur mobile.

![app_screenshot](./docs/capture.png)

## Description
Cette application Python fait partie de l'initiative CSEN | GT3 visant à créer une base de données de problèmes mathématiques à destination des enseignants. C'est un outil pédagogique interactif pour explorer un problème de géométrie spécifique concernant la constance de la surface dans un cercle divisé par des lignes de coupes partant d'un point intérieur mobile. *Pour déplacer le point P, double-cliquez à l'endroit souhaité.*

Web app : [https://romainbourdoncle.github.io/watermelon-teorem/](https://romainbourdoncle.github.io/watermelon-teorem/)
_Ne prend actuellement pas en charge les appareils mobiles. Utiliser un ordinateur de bureau ou portable_

## Instructions pour exécuter l'application Python

### Pour les utilisateurs Windows
Si vous utilisez Windows, vous pouvez simplement télécharger puis exécuter le fichier .exe fourni pour lancer l'application.

[Télécharger l'application](https://github.com/romainbourdoncle/watermelon-teorem/releases/download/v1.0.0/tracer_cercle4.exe)

### Pour les utilisateurs macOS
Si vous utilisez macOS, vous devez exécuter le code via le terminal. Veuillez consulter le fichier nommé *tracer_cercle4* dans le dossier **src** pour le code source. Voici les étapes à suivre :
1. Ouvrez le terminal et naviguez vers le dossier contenant le script.
2. Installez les packages requis :
```
pip install matplotlib pip numpy
```
4. Executez the script:
```
python tracer_cercle4.py
```
**Contribuer**
Ce projet fait partie de l'initiative du CSEN | GT3. Les contributions sont les bienvenues, surtout à des fins éducatives. Pour les changements majeurs, veuillez d'abord ouvrir un problème pour discuter de ce que vous souhaitez changer.

**Licence**
Ce projet est sous licence CC BY-NC.
