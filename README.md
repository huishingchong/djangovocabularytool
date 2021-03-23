# djangovocabularytool
This is a Chinese vocabulary tool website designated for making the creation of Chinese vocabulary sets easier. After entering a title for your vocabulary set, you can input Chinese vocabulary words and the english translation as well as phonetic writing will be automatically generated into a vocabulary table. There are  functionalities provided like staring/unstaring vocabulary words, editing the provided english translations to your liking, deleting vocabulary and vocabulary sets, etc. Lastly you can export your finished vocabulary set to pdf format for download.

<br>
To run web application on local host, first open a new terminal and if not in virtual environment (env), copy the code below into terminal:
source env/bin/activate

Once in virtual environment - you see (env) - then copy the code below into terminal and press enter:
python3 manage.py runserver

On your web browser, type in localhost:8000 and you should be able to see my web application.

<br>
Username and password you can use

Username: admin
Password: 123admin456
<br>

Packages installed:

pip install django-allauth

pip install pinyin_jyutping_sentence

pip install googletrans

pip install xhtml2pdf

pip install django-extensions

pip install pydotplus

pip install django-filters

pip install django_on_heroku
