# Web_scraping.py
1. Import Statements
requests: Used to send HTTP requests to fetch the webpage content.
BeautifulSoup: Used to parse and extract data from the HTML content of the webpage.
pandas: Used to structure the scraped data into a DataFrame and save it as a CSV or HTML file.
logging: Used to log information, warnings, and errors during the execution of the script.
schedule: Used to schedule the scraping task to run at specific times.
time: Used to pause the script while waiting for the next scheduled task.
datetime: Provides date and time functionality (not directly used in the code but imported for potential use).
2. Logging Setup
Configures the logging system to:
Save logs to a file named scraper.log.
Log messages with a timestamp, log level (INFO, WARNING, ERROR), and the message content.
Helps track the script's execution and debug issues.
3. fetch_jobs() Function
Purpose: Fetches the HTML content of the job listing webpage.
Steps:
Sends an HTTP GET request to the URL (https://vacancymail.co.zw/jobs/) with custom headers to mimic a browser.
Checks for HTTP errors using response.raise_for_status().
Parses the HTML content using BeautifulSoup and returns the parsed object (soup).
Logs an error and returns None if the request fails.
4. extract_job_data() Function
Purpose: Extracts job details from the parsed HTML content.
Steps:
Finds all job postings (div elements with class job-listing-details) and limits the results to 10.
For each job posting:
Extracts the job title, company name, and description.
Adds the extracted data to a list of dictionaries (job_list).
Logs warnings for any errors encountered while parsing individual job postings.
Returns the list of job data.
5. save_to_csv() Function
Purpose: Saves the scraped job data to a CSV file.
Steps:
Converts the job data (job_list) into a pandas DataFrame.
Saves the DataFrame to a file named scraped_data.csv.
Logs the number of entries saved.
6. save_to_html() Function
Purpose: Saves the scraped job data to an HTML file.
Steps:
Converts the job data (job_list) into a pandas DataFrame.
Saves the DataFrame as an HTML file named scraped_jobs.html.
Logs the file name.
7. scrape_jobs() Function
Purpose: Orchestrates the entire scraping process.
Steps:
Logs the start of the scraping process.
Fetches the webpage content using fetch_jobs().
Extracts job data using extract_job_data().
Saves the data to both CSV and HTML files using save_to_csv() and save_to_html().
Logs warnings if no data is found or if the webpage cannot be retrieved.
Logs the completion of the scraping process.
8. schedule_scraping() Function
Purpose: Schedules the scrape_jobs() function to run daily at midnight.
Steps:
Uses the schedule library to schedule the scrape_jobs() function at 00:00 every day.
Continuously checks for pending tasks and executes them.
9. Main Execution Block
Purpose: Executes the script.
Steps:
Runs the scrape_jobs() function immediately for testing.
Starts the scheduler to run the scraping task daily at midnight.
Summary of Outputs
CSV File:
The scraped job data is saved in scraped_data.csv.
HTML File:
The scraped job data is saved in scraped_jobs.html.
Logs:
Execution details, warnings, and errors are logged in scraper.log.
Let me know if you need further clarification!

Similar code found with 1 license type - View matches