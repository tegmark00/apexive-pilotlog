## How to set up

1. Clone this repository:
```bahs
git clone https://github.com/tegmark00/apexive-pilotlog.git
```
2. Change directory to the project root:
```bash
cd apexive-pilotlog
```
3. If you are using poetry, install the dependencies:
```bash
poetry install --no-root
```
```bash
poetry shell
```
4. Otherwise you can use virtual environment:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

## How to run
 - Run migrations (it is SQLite database, so you don't need to set up a database):
```bash
python manage.py migrate
```
 - Run the server:
```bash
python manage.py runserver
```
 - Open your browser and go to http://127.0.0.1:8000/

## How to import data

### Using UI
Go to http://127.0.0.1:8000/ and use form to upload a JSON file with data.

Example file: `import - pilotlog_mcc.json`; 

### Using command
Use management command to import data from a file:
```bash
python manage.py import_pilotlog_json <path_to_file>
```
Example:
```bash
python manage.py import_pilotlog_json "import - pilotlog_mcc.json"
```

### Using API
Check this endpoint http://127.0.0.1:8000/api/import/

## How to export data

### Using UI
Go to http://127.0.0.1:8000/ and press download button.

### Using Link
Go to http://127.0.0.1:8000/export/.

### Using command
Use management command to export data to a file:
```bash
python manage.py export_logbook_csv
```