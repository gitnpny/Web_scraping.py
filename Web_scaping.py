#import requests
#from bs4 import BeautifulSoup
#import pandas as pd
#import logging
#import schedule
#import time
#import os
#
## Setup logging
#logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
#def scrape_jobs():
#    start_time = time.time()
#    logging.info("Starting job scraping...")
#
#    url = "https://vacancymail.co.zw/jobs/"
#
#    try:
#        # Use requests to fetch the page content
#        logging.debug("Sending request to the URL...")
#        response = requests.get(url, timeout=10)
#        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
#        logging.debug("Page loaded successfully.")
#        soup = BeautifulSoup(response.text, 'html.parser')
#
#        logging.debug(f"Page content loaded. Extracting job data...")
#
#        jobs_data = []
#        job_cards = soup.select('div.card')[:10]  # Get the 10 most recent jobs
#
#        logging.debug(f"Number of job cards found: {len(job_cards)}")
#
#        for card in job_cards:
#            try:
#                title = card.select_one('a.card-title').text.strip()
#                company = card.select_one('span.company').text.strip() if card.select_one('span.company') else 'N/A'
#                location = card.select_one('span.location').text.strip() if card.select_one('span.location') else 'N/A'
#                expiry = card.select_one('span.expiry-date').text.strip() if card.select_one('span.expiry-date') else 'N/A'
#                description = card.select_one('div.card-text').text.strip() if card.select_one('div.card-text') else 'N/A'
#                link = card.select_one('a.card-title')['href'] if card.select_one('a.card-title') else 'N/A'
#                posted_date = card.select_one('span.posted-date').text.strip() if card.select_one('span.posted-date') else 'N/A'
#
#                jobs_data.append({
#                    "Job Title": title,
#                    "Company": company,
#                    "Location": location,
#                    "Expiry Date": expiry,
#                    "Job Description": description,
#                    "Job Link": link,
#                    "Posted Date": posted_date
#                })
#            except Exception as e:
#                logging.warning(f"Failed to parse a job card: {e}")
#
#        # Create a DataFrame with the job data
#        df = pd.DataFrame(jobs_data)
#
#        # Save the data to an Excel file
#        file_path = r'c:\Users\uncommonStudent\Desktop\scraped_jobs.xlsx'
#        df.to_excel(file_path, index=False, engine='openpyxl')  # Save as Excel file
#        logging.info(f"Job scraping completed in {time.time() - start_time:.2f} seconds. Data saved to {file_path}.")
#    except requests.exceptions.RequestException as e:
#        logging.error(f"HTTP Request failed: {e}")
#    except Exception as e:
#        logging.error(f"Unexpected error: {e}")
#
## Schedule to run every 1 minute
#schedule.every(1).minutes.do(scrape_jobs)
#logging.info("Scheduled job executed.")
#
#def run_scheduler():
#    logging.info("Scheduler started.")
#    try:
#        while True:
#            schedule.run_pending()
#            time.sleep(1)  # Reduced sleep time for quicker response
#    except KeyboardInterrupt:
#        logging.info("Scheduler stopped by user.")
#
## Enable scheduling
#run_scheduler()