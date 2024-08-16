# Project Setup

```
python3 -m venv venv
source venv/bin/activate

-- Approach1
touch requirements.txt
Flask>=3.0.0
pip install -r requirements.txt
pip list

-- Approach2
pip install Flask
pip freeze > requirements.txt
pip list

```
