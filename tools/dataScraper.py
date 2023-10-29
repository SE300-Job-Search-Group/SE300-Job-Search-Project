import requests
from bs4 import BeautifulSoup
import sqlite3

def create_database():
    conn = sqlite3.connect('indeed_aerospace_jobs.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            company_reviews TEXT,
            job_title TEXT,
            job_description TEXT,
            job_salary_range TEXT,
            job_keywords TEXT,
            job_location TEXT
        )
    ''')

    conn.commit()
    conn.close()

def scrape_indeed_aerospace_jobs():
    base_url = "https://www.indeed.com"
    search_url = "/jobs?q=aerospace+engineering"

    conn = sqlite3.connect('indeed_aerospace_jobs.db')
    cursor = conn.cursor()

    while True:
        response = requests.get(base_url + search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for job in job_listings:
            company_name = job.find('span', class_='company').text.strip()
            company_reviews = job.find('span', class_='ratingsContent')
            job_title = job.find('a', class_='jobtitle').text.strip()
            job_description = job.find('div', class_='summary').text.strip()
            job_salary = job.find('span', class_='salaryText')
            job_keywords = job.find('div', class_='jobCardReqContainer')
            job_location = job.find('div', class_='location')

            if company_reviews:
                company_reviews = company_reviews.text.strip()
            else:
                company_reviews = "No reviews"

            if job_salary:
                job_salary = job_salary.text.strip()
            else:
                job_salary = "Salary not specified"

            if job_keywords:
                job_keywords = job_keywords.text.strip()
            else:
                job_keywords = "No keywords specified"

            if job_location:
                job_location = job_location.text.strip()
            else:
                job_location = "Location not specified"

            cursor.execute('''
                INSERT INTO jobs (company_name, company_reviews, job_title, job_description, job_salary_range, job_keywords, job_location)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (company_name, company_reviews, job_title, job_description, job_salary, job_keywords, job_location))

            conn.commit()

        next_page = soup.find('span', {'aria-label': 'Next'})
        if next_page:
            search_url = next_page.find_parent()['href']
        else:
            break

    conn.close()

if __name__ == "__main__":
    create_database()
    scrape_indeed_aerospace_jobs()
