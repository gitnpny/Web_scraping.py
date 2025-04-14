import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import schedule
import time
from datetime import datetime


logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_jobs():
    url = 'https://vacancymail.co.zw/jobs/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the webpage: {e}")
        return None


def extract_job_data(soup):
    job_list = []
    try:
        job_posts = soup.find_all('div', class_='job-listing-details', limit=10)
        for job in job_posts:
            try:
                title_tag = job.find('h3', class_='job-listing-title')
                company_tag = job.find('h4', class_='job-listing-company')
                desc_tag = job.find('p', class_='job-listing-text')

                title = title_tag.text.strip() if title_tag else 'Not specified'
                company = company_tag.text.strip() if company_tag else 'Not specified'
                description = desc_tag.text.strip() if desc_tag else 'Not specified'

                job_list.append({
                    'Job Title': title,
                    'Company': company,
                    'Location': 'Not specified', 
                    'Expiry Date': pd.NaT,        
                    'Job Description': description
                })
            except Exception as e:
                logging.warning(f"Error parsing a job listing: {e}")
                continue
    except Exception as e:
        logging.error(f"Error extracting job data: {e}")
    return job_list


def save_to_csv(job_list):
    df = pd.DataFrame(job_list)
    df.to_csv('scraped_data.csv', index=False)
    logging.info(f"Data saved to scraped_data.csv with {len(df)} entries")


def save_to_html(job_list):
    df = pd.DataFrame(job_list)
    html_file = 'scraped_jobs.html'
    df.to_html(html_file, index=False, escape=False)
    logging.info(f"Data saved to {html_file}")

def scrape_jobs():
    logging.info("Scraping started")
    soup = fetch_jobs()
    if soup:
        job_list = extract_job_data(soup)
        if job_list:
            save_to_csv(job_list)
            save_to_html(job_list)  
        else:
            logging.warning("No job data found")
    else:
        logging.warning("Failed to retrieve the webpage")
    logging.info("Scraping completed")


def schedule_scraping():
    schedule.every().day.at("00:00").do(scrape_jobs)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    
    scrape_jobs()

    
    schedule_scraping()