import requests


def fetchQuote():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'yf34FMznrRRs47angYc+Vg==916c1cigyY226Mlm'})
    if response.status_code == requests.codes.ok:
        data = (response.json())
        return data[0]['quote']
    else:
        return 'No quote for you!'
