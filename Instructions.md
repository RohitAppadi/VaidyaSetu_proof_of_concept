# Execution 
## To enure a smooth operation of my project in your system I will thouroughly guide you through on how to run and all the libraries you need to download 
1. Set up VSCode or any other compiler that is comfortable for your work type (I would recommend VSCode).
2. Download all the files in the repository mainly two important files that are the backbone and the structure of the prototype- **app.py** and **index.html** and **cmds.txt** and **requiremnts.txt**.
3. Create a separate folder on your Desktop and place **app.py** in the folder.
4. Create a sub folder named **template** and place the **index.html** in this folder.
5. Till now if everything is correct, in your VSCode select file>open folder>[Folder_Name}>Select folder
6. After opening your main folder not open **app.py** and open terminal.
7. Follow through the **cmds.txt** file provided to create a virtual space in your system and if every thing is working correctly after 2 steps your terminal folder address should start with **(venv)**
which is a Virtual Enviroinment all the Python libraries and dependencies we need, like Flask and the QR code generator, areonly installed in our project folder and don't
interfere with other projects on our computer. It keeps our project clean, organized,
and easily shareable with others on our team.
8. Continue following through the **cmds.txt** file and download **requiremnts.txt** which consists of all the libraries such as flask, pillow, QRcode and requests.
9. After downloading the required libraries you are ready to **run flask** which will connect your backend with your frontend and give you a http link to the webpage.
10. Ctlr+Click on the the link and you will be redirected to the page.
11. Check out the interface and add records according to the given questions, and don't forget the interactive map.
12. After adding the necessary details, Congratulaion- You have succesfully added a record and generated a QR code, when scanned you will be provided with you unique hashcode.
13. On the bottom you will find the interactive map and a pointer placed in the location with exact Time, and Day with the batch ID and the Herb name.
14. You can add more than one record and also if you face any difficulty with the **Geocode** be sure to input the address again without specifics or numbers such as sectors and pincodes.
15. If is issue still persists there might be a problem with with **Geocode API** since it is a third party free to use open source Interactive map and can have challenges loading.
16. After exploring the page go to the VSCode and click on the terminal and do Ctrl+C to stop the sever.
You have Succesfully added records, recieved a unique hashcode and even generated a QR code all while using basic python and HTML.
