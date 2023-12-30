import requests


def fetchQuote():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        data = (response.json())
        return data[0]['quote']
    else:
        return 'No quote for you!'
