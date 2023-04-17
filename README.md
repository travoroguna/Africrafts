## setup

install dependancies
```bash
python3 -m pip install -r requirements.txt
```

### Database

for local development set the database uri in `instance/configdev.toml`

config file can be passed to a run command as

```bash
gunicorn "app:create_app(config='config_deploy.toml')"
```


initialize the database
```bash
flask db init
```

generate initilal migration
```bash
flask db migrate -m "Initial migration."
```

apply changes
```bash
flask db upgrade
```

[flask migrate docs]("https://flask-migrate.readthedocs.io/en/latest/")

## running the app locally

creating a virtual environment is recomended

run the app
```bash
flask run
```