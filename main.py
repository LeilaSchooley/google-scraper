import requests
import pandas as pd
import configparser
import os
import uuid

from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

config = configparser.ConfigParser()

config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path)
SCRAPER_API_KEY = config.get("DEFAULT", "SCRAPER_API_KEY")
# Replace 'APIKEY' with your actual API key from ScraperAPI


def fetch_google_results(query, pages=1, country_code='us', tld='com'):
    """
    Fetch Google search results for a given query and number of pages.

    Args:
        query (str): The search query.
        pages (int): Number of pages to scrape (10 results per page).
        country_code (str): Country code for geotargeting.
        tld (str): Top-level domain for Google.

    Returns:
        list: A list of dictionaries with the scraped results.
    """
    all_results = []
    print(f"Scraping query: {query}")
    
    for page in range(pages):
        start = page * 10
        print(f"Fetching page {page + 1}...")
        payload = {
            'api_key': SCRAPER_API_KEY,
            'query': query,
            'country_code': country_code,
            'tld': tld,
            'start': start,
            'output': 'json'
        }
        response = requests.get('https://api.scraperapi.com/structured/google/search', params=payload)

        if response.status_code == 200:
            data = response.json()
            if 'organic_results' in data:
                all_results.extend(data['organic_results'])
            else:
                print(f"No organic results found on page {page + 1}.")
        else:
            print(f"Error fetching page {page + 1}: {response.status_code} - {response.text}")

    return all_results

def process_results(results):
    """
    Process the raw results from the Google SERP API into a pandas DataFrame.

    Args:
        results (list): The raw results from the API.

    Returns:
        pd.DataFrame: A DataFrame with structured data.
    """
    processed_data = []
    
    for result in results:
        processed_data.append({
            'position': result.get('position'),
            'title': result.get('title'),
            'snippet': result.get('snippet'),
            'link': result.get('link'),
            'displayed_link': result.get('displayed_link'),
        })
    
    print(f"Processed {len(processed_data)} results.")
    return pd.DataFrame(processed_data)

def save_to_csv(dataframe, filename="results.csv"):
    """
    Save the DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        filename (str): The name of the output CSV file.
    """
    dataframe.to_csv(filename, index=False)
    print(f"Results saved to {filename}.")

def main():
    # User inputs
    query = input("Enter the search keyword: ").strip()
    pages = int(input("Enter the number of pages to scrape: ").strip())
    
    # Fetch and process results
    results = fetch_google_results(query, pages=pages)
    if results:
        df = process_results(results)
        df.columns = [col.lower() for col in df.columns]  # Convert column names to lowercase
        print(df.head())  # Display the first few rows
        save_to_csv(df, f"{query.replace(' ', '_')}_results.csv")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
