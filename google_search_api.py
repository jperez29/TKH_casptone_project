from serpapi import GoogleSearch
from app import db, EmploymentData

def pulling_data(job_titles, cities):
    job_results = []
    for job in job_titles:
        for city in cities:
            params = {
            "engine": "google_jobs",
            "q": f'{job} {city}',
            "hl": "en",
                'num': 100,
                'start': 10,
            "api_key": None,
            }


            #looping through 10 pages            
            for x in range(1):                
                params['start'] = 10 * x
                search = GoogleSearch(params)
                #json data
                results = search.get_dict()
            
    
                #loop and call validate response on each item of results['job_search']
                #pass each row to validate response
                #only return false with the columns we don't want
                #continue with the ones you want to keep
                
                #val is going to be either True of False, depending on what job_results_validation returns
                validate_response = jobs_results_validation(results)
                print(validate_response)
                #if jobs_results key is found in the json data, then this will return true and it'll enter the if statament. Otherwise continue with the for loop to get more pages
                if validate_response:
                    job_postings = results['jobs_results']
                    print(type(job_postings))
                    #we're getting 10 pages per loop in a list, so we're looping through each job posting to check that the columns we want are there
                    for job_post in job_postings:
                        response = columns_validation(job_post)
                        if response:
                            print(job_post)
                            job_results.append(job_post)
                        else:
                            print('response was false')
                else:
                    continue
                        
    #list of dictionaries
    print(len(job_results))
    return job_results

def jobs_results_validation(results):
    print('does validate response work?')
    if 'jobs_results' not in results:
        print(params['q'])
        print('if job_results is not found in the json data, then this should print')
        # print(results['search_metadata']["status"])
        return False
    return True
    # print(results['jobs_results'])

def columns_validation(job_post):
    lst = ['title', 'location', 'job_id']
    #prioritize: title, location, job_id --> if rows don't have these, then we don't want them
    #if these are empty, return false

    for column in lst:
        if column not in job_post:
            # print(results['jobs_results']['title'])
            print('is columns_validation returning false?')
            return False
    #if this returns false then the job posting will not be added to the list, even if the above columns are found in job posting
    if 'schedule_type' not in job_post['detected_extensions']:
            print('schedule type')
            return False
    return True

def setup_db():
    job_titles = ['software engineer', 'data analyst', 'web developer', 'data scientist', 'front-end developer', 'back-end developer', 'UI/UX designer']
    cities = ['new york city', 'newark new jersey', 'los angeles california', 'atlanta georgia']
    # job_titles = ['data analyst']
    # cities = ['newark nj']
    data = pulling_data(job_titles, cities)
    db.drop_all()
    db.create_all()

    #adding data to database
    for dct in data:
        #making sure we don't include duplicates
        #job_id is the primary key
        exists = db.session.query(EmploymentData).filter_by(job_id=dct['job_id']).first()
        if not exists:
            row = EmploymentData(title = dct['title'], company_name = dct['company_name'], location = dct['location'], via = dct['via'], description = dct['description'], schedule_type = dct['detected_extensions']['schedule_type'], job_id = dct['job_id'])
            print(row)
            db.session.add(row)
            db.session.commit()

if __name__ == '__main__':
    setup_db()