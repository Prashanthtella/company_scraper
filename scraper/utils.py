import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def scrape_data(keyword):
    search_url = f"https://www.google.com/search?q={keyword}+site:linkedin.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(search_url, headers=headers)
    
    # Check if the response is OK
    if response.status_code != 200:
        print("Failed to retrieve data")
        return []
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check the soup content to ensure it's working
    print(soup.prettify())  # Look at what Google returns for troubleshooting

    companies = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if "linkedin.com/company" in href:
            company_name = link.text.strip()
            phone_number = extract_phone_number(soup.text)
            email = extract_email(soup.text)
            companies.append({
                "company_name": company_name,
                "phone_number": phone_number,
                "email": email,
                "keyword": keyword
            })

    # If no companies were found, return a message instead of an empty list
    if not companies:
        print("No results found. Google may have blocked scraping.")
    
    return companies

def extract_phone_number(text):
    phone_pattern = re.compile(r'\+?\d[\d -]{8,12}\d')
    phone_match = phone_pattern.search(text)
    return phone_match.group(0) if phone_match else "No phone number found"

def extract_email(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    email_match = email_pattern.search(text)
    return email_match.group(0) if email_match else "No email found"