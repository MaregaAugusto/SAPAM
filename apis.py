import requests

if __name__ == '__main__':
    url = 'https://apis.datos.gob.ar/georef/api/departamentos'
    args = {"campos":"nombre","max":1100,"provincia":"Santa Fe"}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        response_json = response.json()
        print(response_json['departamentos'])
