# python
python -m venv .venv
python -m pip install --upgrade pip
.venv\Scripts\deactivate (deactivate)
.venv\Scripts\activate (activate)
pip freeze > requirements.txt
pip install -r requirements.txt