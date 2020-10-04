import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_provincias():
    response = generate_request('https://apis.datos.gob.ar/georef/api/provincias')
    if response:
        provincias = response['provincias']
        return provincias


""" def get_departamentos(params={}):
    response = generate_request('https://apis.datos.gob.ar/georef/api/departamentos', params)
    if response:
        user = response.get('results')[0]
        return user.get('name').get('first')

    return ''"

def get_municipios(params={}):
    response = generate_request('https://apis.datos.gob.ar/georef/api/departamentos', params)
    if response:
        user = response.get('results')[0]
        return user.get('name').get('first')

    return ''" """