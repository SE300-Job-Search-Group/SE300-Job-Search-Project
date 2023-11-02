import re
import json
import requests
from urllib.parse import urlencode

def get_indeed_search_url(keyword, location, offset=0):
    parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
    return "https://www.indeed.com/jobs?" + urlencode(parameters)


headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

job_id_list = []

## Job Search Parameters
keyword_list = ['aerospace']
location_list = ['anywhere']

## Loop Through Indeed Pages Until No More Jobs
for keyword in keyword_list:
    for location in location_list:
        for offset in range(0, 1010, 10):
            try:
                indeed_jobs_url = get_indeed_search_url(keyword, location, offset)
                
                ##bypass indeed blocking
                SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

                def scrapeops_url(url):
                    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
                    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
                    return proxy_url


                indeed_search_url = 'https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Dsoftware%20engineer%26l%3DSan%20Francisco%26start%3D0%26filter%3D0'

                ## Send URL To ScrapeOps Instead of Indeed 
                response = requests.get(
                url='https://proxy.scrapeops.io/v1/',
                params={
                    'api_key': '368ff5f6-f062-4cc3-b874-d08d6a7a1ff3',
                    'url': indeed_jobs_url, 
                },
                )
                
                
                if response.status_code == 200:
                    script_tag = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', html)
                    if script_tag is not None:
                        json_blob = json.loads(script_tag[0])
                        jobs_list = json_blob["metaData"]["mosaicProviderJobCardsModel"]

                        for index, job in enumerate(jobs_list):
                            if job.get('jobkey') is not None:
                                job_id_list.append(job.get('jobkey'))
                        ## If response contains less than 10 jobs then stop pagination
                        if len(jobs_list) < 10:
                            break
                    
            except Exception as e:
                print('Error', e)

print(job_id_list)