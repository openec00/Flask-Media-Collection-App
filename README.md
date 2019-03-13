# A Flask Audio-Visual File Collection Application

 This is an application that is built on the popular Flask framework for Python

### To Install (Linux Distro)

open a linux terminal

```
git clone https://github.com/
```
```
cd av-collection-app/
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=av-collection-app.py
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
Run application - NOTE FLASK_APP=av-collection-app.py entry should be made in.flaskenv or export the variable in your local environment:
flask run
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
