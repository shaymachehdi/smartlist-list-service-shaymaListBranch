
## Bienvenue dans le microservice List!  
Ce repository contient le code source de notre microservice list.  
En utilisant la version Python 3.6 pour l'application, et mysql 5.7 pour gérer la base de données.  
  
## Étapes à suivre  
  
 1. Ouvrez le dossier de repo.  
 2. Ouvrez le terminal dans ce dossier et lancez la commande :   
 ``` 
  $ sudo docker-compose up 
 ``` 
 3. Ouvrez un autre terminal et lancer la commande :   
 ```
  $ sudo docker ps
  ```  
  Prenez le CONTAINER ID de votre conteneur mysql:5.7  
 4. Puis lancez la commande suivante pour ouvrir l'invite de commande  de mysql :   
 ```
  $ sudo docker exec -it CONTAINER ID mysql -uroot -p
  ```  
 5. Entrez le mot de passe **root** qui est définit dans **docker-compose.yml**  
 6. Puis tapez la commande pour créer la base de données :  
 ``` 
  mysql> create database list_ms_db;
 ```  
 7. Une étape très importante est de garantir à notre utilisateur **root** tous les privilèges sur la base de données déjà créer en tapant les deux commandes suivantes :   
 ``` 
  mysql> use list_ms_db;
  mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'root' WITH GRANT OPTION; 
 ```
 8. Pour tester la bonne fonctionnement du serveur mysql dans le container docker, vous pouvez installer le client mysql-workbench :   
 ``` 
  $ sudo apt update 
  $ sudo apt install mysql-workbench 
 ```
 9. Ouvrez mysql-workbench et créer une nouvelle connexion avec les paramètres suivants :   
 <br/> `Hostname : localhost`  <br/> `Port : 32000`  <br/> `Username : root`<br/>`Password : root`  
  
On est terminé la configuration pour que le conteneur flask peut se connecter avec le conteneur MySQL. :smiley: :smiley: :smiley:  

 10. Maintenant il faut relancer le conteneur avec les deux commandes suivantes :   
 ``` 
  $ sudo docker-compose down
  $ sudo docker-compose up 
 ```
 Si tout vas bien, tant mieux, sinon n'hésitez pas à me contacter sur la plateforme. :open_mouth: :open_mouth: :open_mouth: