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
            for x in range(50):                
                params['start'] = 10 * x
                search = GoogleSearch(params)
                #json data
                results = search.get_dict()
                
                #val is going to be either True of False, depending on what job_results_validation returns
                validate_response = jobs_results_validation(results)
                print(validate_response)
                #if jobs_results key is found in the json data, then this will return true and it'll enter the if statament. Otherwise continue with the for loop to get more pages
                if validate_response:
                    job_postings = results['jobs_results']
                    #we're getting 10 pages per loop in a list, so we're looping through each job posting to check that the columns we want are there
                    for job_post in job_postings:
                        response = columns_validation(job_post)
                        if response:
                            job_post['job_category'] = job
                            job_post['location_category'] = city
                            print(job_post)
                            job_results.append(job_post)
                        else:
                            print('response was false')
                else:
                    print(f'No job posting found for {job} in {city}')
               
                        
    #list of dictionaries
    print(len(job_results))
    return job_results

def jobs_results_validation(results):
    if 'jobs_results' not in results:
        # print('if job_results is not found in the json data, then this should print')
        return False
    return True

def columns_validation(job_post):
    lst = ['title', 'location', 'job_id']
    #prioritize: title, location, job_id --> if rows don't have these, then we don't want them
    #if these are empty, return false

    for column in lst:
        if column not in job_post:
            print('is columns_validation returning false?')
            return False
    return True

def setup_db():
    job_titles = ['front-end developer', 'back-end developer', 'UI/UX designer']
    cities = ['new york city', 'newark new jersey', 'los angeles california', 'atlanta georgia']
    # job_titles = ['software engineer']
    # cities = ['new york city']
    data = pulling_data(job_titles, cities)
    
    db.create_all()

    #adding data to database
    for dct in data:
        #making sure we don't include duplicates
        #job_id is the primary key
        exists = db.session.query(EmploymentData).filter_by(job_id=dct['job_id']).first()
        if not exists:
            row = EmploymentData(title = dct['title'], company_name = dct['company_name'], location = dct['location'], via = dct['via'], job_category= dct['job_category'], location_category = dct['location_category'], description = dct['description'], schedule_type = dct['detected_extensions'].get('schedule_type', None), job_id = dct['job_id'])
            print(row)
            db.session.add(row)
            db.session.commit()

if __name__ == '__main__':
    setup_db()