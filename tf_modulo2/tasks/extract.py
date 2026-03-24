import requests

def extract():
    """
    extraer data de randomuser
    """
    URL = "https://restcountries.com/v3.1/region/America"
    response = requests.get(URL)
    
    extract_data = []
    if response.status_code == 200:
        extract_data = response.json()
    return extract_data