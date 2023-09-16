import requests
from bs4 import BeautifulSoup

def scrape_google_maps(search_query):
    url = f"https://www.google.com/maps/search/{search_query}"
    headers = {
        "User-Agent": "Chrome/116.0.5845.188 (Windows 11 Pro; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find and extract relevant information
    results = []
    for item in soup.select('.section-result'):
        name = item.select_one('.section-result-title span').text.strip()
        address = item.select_one('.section-result-location').text.strip()
        rating = item.select_one('.cards-rating-score span').text.strip()
        lat = item.get('data-lat')
        lng = item.get('data-lng')
        
        result = {
            'name': name,
            'address': address,
            'rating': rating,
            'latitude': lat,
            'longitude': lng
        }
        results.append(result)
    
    return results

# Example usage
search_query = "restaurants in New York"
results = scrape_google_maps(search_query)
for result in results:
    print(result)