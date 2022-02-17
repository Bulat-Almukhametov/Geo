# Geo
 ## Prerequisites
Before first run:
 * Python 3 should be installed
 * Install Pillow package. In command line run:
 > pip install Pillow

 ## Run
 Put csv files to **data** folder. Open command line and go to root folder. Run in command line:
 > python app.py

Images per each csv will be created in **result** folder. Animation named **animation.gif** will be created in root folder.

### Notes
If delete csv files and run again with other data then **animation.gif** file will be rewritten. Images in **result** folder will be created with the name of csv file. They won't be rewritten if names of next files will be the same.