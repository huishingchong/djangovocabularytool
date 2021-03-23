# djangovocabularytool
This is a Chinese vocabulary tool website designated for making the creation of Chinese vocabulary sets easier. After entering a title for your vocabulary set, you can input Chinese vocabulary words and the english translation as well as phonetic writing will be automatically generated into a vocabulary table. There are  functionalities provided like staring/unstaring vocabulary words, editing the provided english translations to your liking, deleting vocabulary and vocabulary sets, etc. Lastly you can export your finished vocabulary set to pdf format for download.
<br>
<br>
To run web application on local host, first open a new terminal and make sure you are in the correct directory of the vocabularytool. Copy the code below into terminal to activate the virtual environment:
<br>
source env/bin/activate
<br>
You may need to create a new virtual environment before activating it by downloading pip and installing virtualenv.
<br>
python3 -m pip install --user --upgrade pip
<br>
python3 -m venv env
<br>
Go to https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ for  documentation on virtual environments.
<br><br>
Once in virtual environment - you know if you see (env) - then copy the code below into terminal and press enter:
<br>
python3 manage.py runserver
<br>
On your web browser, type localhost:8000 into the address bar and press 'enter'. You should be able to see the web application now.
<br><br>
Existing account you can use: <br>
Username: admin
<br>
Password: 123admin456
<br>
<br>
Packages installed:
<br>
pip install django-allauth

pip install pinyin_jyutping_sentence

pip install googletrans

pip install xhtml2pdf

pip install django-extensions

pip install pydotplus

pip install django-filters

pip install django_on_heroku
