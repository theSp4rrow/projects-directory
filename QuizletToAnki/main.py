import requests
from bs4 import BeautifulSoup

# Replace with your Quizlet set URL
url = "https://quizlet.com/69578459/california-dmv-permit-practice-test-flash-cards/?funnelUUID=c6aca08c-0849-4ae5-b9d7-237432a7c009"

# Simulate a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
}

# Send the request
response = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

# Find terms and definitions
terms = soup.find_all("div", class_="SetPageTerm-content")

if not terms:
    print("No terms found. The page structure might have changed.")
else:
    for term in terms:
        front = term.find("span", attrs={"data-testid": "TermText"}).get_text()
        back = term.find("span", attrs={"data-testid": "DefinitionText"}).get_text()
        print(f"Term: {front}")
        print(f"Definition: {back}")
        print("-" * 30)
