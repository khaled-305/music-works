# Admin Login Details
- Username: admin
- Password: swordfish

# Part 1
- To execute the app:

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

# convert the csv file to json
python3 makejson.py

# load the converted json file to the database with django command
python3 manage.py loaddata makejson.json

# Questions
1) 
2) The process of automating metadata upload from providers can be achieved by 
   creating a form on the music application and allowing the providers to make 
   the upload on their own. This form will have all the necessary fields expected from the metadata, and validations to make sure only appropriate characters and keywords are entered. This will help save time and resources. 

# Part 2
- To execute the app:

python manage.py runserver

from your web browser, go to: http://127.0.0.1:8000/music/<iswc>/

replace <iswc> with the iswc code you want to get metadata for.