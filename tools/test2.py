##Cancel the run asap so we don't use up the API key
import re
import json
import requests
import sqlite3  # Use SQLite for simplicity
from urllib.parse import urlencode

# Initialize a SQLite database connection
conn = sqlite3.connect('job_data.db')
cursor = conn.cursor()

# Create a table to store job data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        job_id TEXT PRIMARY KEY,
        keyword TEXT,
        location TEXT
    )
''')

def save_job_to_database(job_id, keyword, location):
    cursor.execute('INSERT INTO jobs (job_id, keyword, location) VALUES (?, ?, ?)', (job_id, keyword, location))
    conn.commit()

def get_indeed_search_url(keyword, location, offset=0):
    parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
    return "https://www.indeed.com/jobs?" + urlencode(parameters)

headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

job_id_list = []

# Job Search Parameters
keyword_list = ['aerospace']
location_list = ['anywhere']

# Loop Through Indeed Pages Until No More Jobs
for keyword in keyword_list:
    for location in location_list:
        for offset in range(0, 1010, 10):
            try:
                indeed_jobs_url = get_indeed_search_url(keyword, location, offset)

                # Send URL To ScrapeOps Instead of Indeed
                response = requests.get(
                    url='https://proxy.scrapeops.io/v1/',
                    params={
                        'api_key': '368ff5f6-f062-4cc3-b874-d08d6a7a1ff3',
                        'url': indeed_jobs_url,
                    },
                )
                ##bypass indeed blocking
                if response.status_code == 200:
                    script_tag = re.search(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', response.text)
                    
                    if script_tag is not None:
                        json_blob = json.loads(script_tag.group(1))
        
                        # Extract jobs data
                        jobs_list =json_blob['metaData']['mosaicProviderJobCardsModel']['results']      
                        
                        for job in jobs_list:
                            if job.get('jobkey') is not None:
                                job_id_list.append(job.get('jobkey'))
                                print("Appended job key:", job.get('jobkey'))

                                ## If response contains less than 10 jobs then stop pagination
                                if len(jobs_list) < 10:
                                    print('3')
                                    break
                                
                                # Insert job data into the database
                                save_job_to_database(job_id_list, keyword, location)
                        if len(jobs_list) < 10:
                            break

            except Exception as e:
                print('Error', e)

print(job_id_list)

# Close the database connection
conn.close()
