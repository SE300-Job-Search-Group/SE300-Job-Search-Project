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
location_list = ['United States']

## Loop Through Indeed Pages Until No More Jobs
for keyword in keyword_list:
    for location in location_list:
        for offset in range(0, 1010, 10):
            try:
                indeed_jobs_url = get_indeed_search_url(keyword, location, offset)
                
                ##bypass indeed blocking
                SCRAPEOPS_API_KEY = '1bcf4bb7-35b1-47e3-91b9-1053edd36bc7'

                def scrapeops_url(url):
                    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
                    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
                    return proxy_url

                ## Send URL To ScrapeOps Instead of Indeed 
                response = requests.get(scrapeops_url(indeed_jobs_url))
                
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


            except Exception as e:
                print('Error', e)    
            
print('done')
print(job_id_list)