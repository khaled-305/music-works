
docker-compose build
docker-compose up
python manage.py makemigrations
python manage.py migrate

python manage.py runserver

## ----------------- ##

# Part 1
- To execute the app:

from the root directory, open 'makejson.py', and change 'csv_path' and 'json_path' variables to the absolute path of the CSV file and Json file respectively on your computer.

'makejson.py' converts the given CSV file to a Json file format so it can be loaded to the database.

# convert the csv file to json
python3 makejson.py

# load the converted json file to the database with django command
python3 manage.py loaddata makejson.json

# Questions
1) 
2) The process of automating metadata upload from providers can be achieved by 
   creating a form on the music application and allowing the providers to make 
   the upload on their own. This form will have all the necessary fields expected from the metadata, and validations to make sure only appropriate characters and keywords are entered. This will help save time and resources. 

## ----------------------- ##

# Part 2
- To execute the app:

python manage.py runserver

from your web browser, go to: http://127.0.0.1:8000/music/<iswc>/

replace <iswc> with the iswc code you want to get metadata for.

# Question
1) No, the solution would not have a similar response time.
2) i. Since the data does not change frequently, i would save the request  
reaponse in a temporary cache instead of having the code to re-run all SQL queries
for every new request.
   ii. Impliment threading. In python, this can be done by using async functions that run on multiple threads
so that tasks which take up a lot of time would run concurrently without compromising the entire view.

# To run Test Case for the API response: 
- python manage.py test