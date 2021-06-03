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

            search = GoogleSearch(params)
            #json data
            results = search.get_dict()
            jobs_results = results['jobs_results']

            #looping through 10 pages
            # job_results = []
            
            for x in range(10):                
                params['start'] = 10 * x
                search = GoogleSearch(params)
                results = search.get_dict()
                # if results['jobs_results'] is None:
                #     continue
                print(results)
                if 'job_results' not in results:
                    continue
                    print(params['q'])
                    print('if job_results is empty, then this should print')
                    print(results['search_metadata']["status"])
                else:
                    job_results += results['jobs_results']
                
    #list of dictionaries
    return job_results

def setup_db():
    # job_titles = ['software engineer', 'data analyst', 'web developer', 'data scientist', 'front-end developer', 'back-end developer', 'UI/UX designer']
    # cities = ['new york city', 'newark new jersey', 'los angeles california', 'atlanta georgia']
    job_titles = ['data analyst']
    cities = ['newark nj']
    data = pulling_data(job_titles, cities)
    db.drop_all()
    db.create_all()

    #adding data to database
    for dct in data:
        #making sure we don't include duplicates
        # exists = db.session.query(EmploymentData).filter_by(job_id=dct['job_id']).first()
        # if not exists:
        row = EmploymentData(title = dct['title'], company_name = dct['company_name'], location = dct['location'], via = dct['via'], description = dct['description'], schedule_type = dct['detected_extensions']['schedule_type'], job_id = dct['job_id'])
        db.session.add(row)
        db.session.commit()

if __name__ == '__main__':
    setup_db()