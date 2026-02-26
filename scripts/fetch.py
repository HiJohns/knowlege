import sys
import requests

def fetch_url(url):
    jina_url = f"https://r.jina.ai/{url}"
    try:
        response = requests.get(jina_url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching URL: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch.py <url>")
        sys.exit(1)
    print(fetch_url(sys.argv[1]))
