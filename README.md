# Africrafts

Africrafts is built using Django.

## Installation

Create and activate virtual environment.

```bash
cd africrafts
python -m venv env

. venv/bin/activate || venv\Scripts\activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

Run migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Start server

```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
