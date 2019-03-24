# A Flask Multi-Purpose Media Collection Application

 This is an application that is built on the popular Flask framework for Python

 ![alt text](https://github.com/openec00/Flask-Multi-Purpose-Media-Collection-App/blob/master/Demo_2_Flask_Media_Collection_App_%202019-03-18%2000-11-52.png "App Demo")

### To Install (Linux Distro)

open a linux terminal

```
git clone https://github.com/openec00/Flask-Multi-Purpose-Media-Collection-App.git
```
```
cd flask-media-collection-app/
```
```
python3 -m venv flask_venv
```
```
source flask_venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=flask-media-collection-app.py (or create a .flaskenv file)
```
```
Create a database :
flask db init
```
```
Create an entries table in database:
flask db migrate -m "entries table"
```
```
Run initial migration for database version control:
flask db upgrade
```
```
Run application - NOTE FLASK_APP=flask-media-collection-app.py entry should be made in.flaskenv or export the variable in your local environment as seen in the steps above:

flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
