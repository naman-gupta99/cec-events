# cec-events
CEC Events

## Requirements
1. Python >= 3.6

## Steps to Requirements
1. Create and activate virtual environment
```(bash)
python3 -m venv venv
source venv/bin/activate (Linux and MacOS)
venv\Scripts\activate (Windows)
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the server
```
FLASK_ENV=development
FLASK_APP=server.py flask run
```
