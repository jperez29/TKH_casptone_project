from serpapi import GoogleSearch
from app import db, EmploymentData

def pulling_data():
    params = {
    "engine": "google_jobs",
    "q": "software engineer new york",
    "hl": "en",
        'num': 100,
        'start': 10,
    "api_key": None
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results['jobs_results']

    job_results = []
    for x in range(10):
        params['start'] = 10 * x
        search = GoogleSearch(params)
        results = search.get_dict()
        job_results += results['jobs_results']
    #list of dictionaries
    return job_results

def setup_db():
    data = pulling_data()
    db.drop_all()
    db.create_all()

    #adding data to database
    for dct in data:
        exists = db.session.query(EmploymentData).filter_by(job_id=dct['job_id']).first()
        if not exists:
            row = EmploymentData(title = dct['title'], company_name = dct['company_name'], location = dct['location'], via = dct['via'], description = dct['description'], schedule_type = dct['detected_extensions']['schedule_type'], job_id = dct['job_id'])
            db.session.add(row)
            db.session.commit()

if __name__ == '__main__':
    setup_db()