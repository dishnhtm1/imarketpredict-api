import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def fetch_nikkei_headlines():
    print("🔎 Fetching Nikkei headlines...")

    url = "https://asia.nikkei.com/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Send request
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to fetch page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    # Extract headlines (we target <h3> or <span> tags based on Nikkei structure)
    headlines = []

    for tag in soup.find_all(["h3", "span"], limit=20):
        text = tag.get_text(strip=True)
        if text and len(text) > 20 and text not in headlines:
            headlines.append(text)

    if not headlines:
        print("⚠️ No headlines found.")
        return

    # Save to file
    os.makedirs("data_samples", exist_ok=True)
    filename = f"data_samples/nikkei_news_{datetime.today().strftime('%Y-%m-%d')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")

    print(f"✅ Saved {len(headlines)} headlines to: {filename}")

# Run the function directly
if __name__ == "__main__":
    fetch_nikkei_headlines()
