import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from itertools import cycle, islice

data = pd.read_csv("datasets/updated_categories_employment_data.csv")

def job_postings(job_category, location):
    return data[(data['job_category'] == job_category) & (data['location_category'] == location)]

software_engineer_ny = job_postings('software engineer', 'new york city')
data_analyst_ny = job_postings('data analyst', 'new york city')
web_developer_ny = job_postings('web developer', 'new york city')
data_scientist_ny = job_postings('data scientist', 'new york city')
front_end_developer_ny = job_postings('front-end developer', 'new york city')
back_end_developer_ny = job_postings('back-end developer', 'new york city')
uiux_designer_ny = job_postings('UI/UX designer', 'new york city')


all_technologies = ['python', 'ruby', 'scala', 'java', 'javascript', 'html', 'css', 'aws', 'node js',
                    'c#', 'c++', 'git', 'github', 'sql', 'mysql', 'postgresql', 'oracle'
                   'linux', 'hadoop',  'scala', 'spark', 'nosql', 'rest apis', 'node.js', 
                   'mongodb', 'docker', 'kubernetes', 'terraform', 'teamcity', 'angular js', 'ides', 'bash'
                   'http', 'react', 'angular', 'vue.js', 'apache cassandra', 'cloud services', 'oop', 'funcitonal programming'
                   'bsa/aml', 'object-oriented programming', 'ssl certificates', 'version control system',
                   'microsoft excel', 'power bi', 'stata', 'sas', 'web intelligence', 'tableau', 'snowflake',
                   'redshift', 'looker', 'braze', 'adobe', 'r programming', 'microsoft office', 'airflow', 'databricks', 'etl', 
                   'machine learning', 'powerpoint', 'matlab', 'apache shark', 'perl', 'statistics', 'matplotlib', 'pandas',
                   'numpy', 'ggplot', 'bokeh', 'flask', 'django', 'd3.js', 'scikit-learn', 'tensorflow', 'pytorch', 'nlp',
                   'meteor', '.net', 'laravel', 'zend', 'yii', 'php', 'elixir', 'express.js', 'figma']

class Jobs:
    def __init__(self):
        self.tech = {}
        
    def append_tech(self, series):
        all_technologies = ['python', 'ruby', 'scala', 'java', 'javascript', 'html', 'css', 'aws', 'node js',
                    'c#', 'c++', 'git', 'github', 'sql', 'mysql', 'postgresql', 'oracle'
                   'linux', 'hadoop',  'scala', 'spark', 'nosql', 'rest apis', 'node.js', 
                   'mongodb', 'docker', 'kubernetes', 'terraform', 'teamcity', 'angular js', 'ides', 'bash'
                   'http', 'react', 'angular', 'vue.js', 'apache cassandra', 'cloud services', 'oop', 'funcitonal programming'
                   'bsa/aml', 'object-oriented programming', 'ssl certificates', 'version control system',
                   'microsoft excel', 'power bi', 'stata', 'sas', 'web intelligence', 'tableau', 'snowflake',
                   'redshift', 'looker', 'braze', 'adobe', 'r programming', 'microsoft office', 'airflow', 'databricks', 'etl', 
                   'machine learning', 'powerpoint', 'matlab', 'apache shark', 'perl', 'statistics', 'matplotlib', 'pandas',
                   'numpy', 'ggplot', 'bokeh', 'flask', 'django', 'd3.js', 'scikit-learn', 'tensorflow', 'pytorch', 'nlp',
                   'meteor', '.net', 'laravel', 'zend', 'yii', 'php', 'elixir', 'express.js', 'figma']
        
        #going through each individual string in the job description column
        for string in series.values:
            for technology in all_technologies:
                if technology in string:
                    self.tech[technology] = self.tech.get(technology, 0) + 1
#                     if tech not in self.tech.keys():
#                         self.tech[tech] = 1
#                     else:
#                         self.tech[tech] += 1

software_engineerny = Jobs()
software_engineerny.append_tech(software_engineer_ny['lowercase_description'])
software_engineerny.tech

data_analystny = Jobs()
data_analystny.append_tech(data_analyst_ny['lowercase_description'])
data_analystny.tech

data_scientistny = Jobs()
data_scientistny.append_tech(data_scientist_ny['lowercase_description'])
data_scientistny.tech

web_developerny = Jobs()
web_developerny.append_tech(web_developer_ny['lowercase_description'])
web_developerny.tech

frontend_developerny = Jobs()
frontend_developerny.append_tech(front_end_developer_ny['lowercase_description'])
frontend_developerny.tech

backend_developerny = Jobs()
backend_developerny.append_tech(back_end_developer_ny['lowercase_description'])
backend_developerny.tech

uiux_designerny = Jobs()
uiux_designerny.append_tech(uiux_designer_ny['lowercase_description'])
uiux_designerny.tech

tech_software_engineer_ny = pd.DataFrame(list(software_engineerny.tech.items()), columns=['technology', 'frequency'])
tech_data_analyst_ny = pd.DataFrame(list(data_analystny.tech.items()), columns=['technology', 'frequency'])
tech_data_scientist_ny = pd.DataFrame(list(data_scientistny.tech.items()), columns=['technology', 'frequency'])
tech_web_developer_ny = pd.DataFrame(list(web_developerny.tech.items()), columns=['technology', 'frequency'])
tech_frontend_developer_ny = pd.DataFrame(list(frontend_developerny.tech.items()), columns=['technology', 'frequency'])
tech_backend_developer_ny = pd.DataFrame(list(backend_developerny.tech.items()), columns=['technology', 'frequency'])
tech_uiux_developer_ny = pd.DataFrame(list(uiux_designerny.tech.items()), columns=['technology', 'frequency'])

top_technologies_se = tech_software_engineer_ny.sort_values(by='frequency', ascending=False).head(10)
top_technologies_da = tech_data_analyst_ny.sort_values(by='frequency', ascending=False).head(10)
top_technologies_ds = tech_data_scientist_ny.sort_values(by='frequency', ascending=False).head(10)
top_technologies_wb = tech_web_developer_ny.sort_values(by='frequency', ascending=False).head(10)
top_technologies_frtd = tech_frontend_developer_ny.sort_values(by='frequency', ascending=False).head(10)
top_technologies_backd = tech_backend_developer_ny.sort_values(by='frequency', ascending=False).head(10)
top_technologies_uiux = tech_uiux_developer_ny.sort_values(by='frequency', ascending=False).head(10)



def app():
    st.title('NEW YORK CITY')

    st.write("Tools for Software Engineer Roles in NY")

        # x = top_technologies_SE['technology']
    y = top_technologies_se['frequency']
    x = ['Scala', 'Java', 'Python', 'AWS', 'SQL', 'Git', 'React', 'JavaScript', 'Kubernetes', 'IDEs']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies Required by Employers For Software Engineers in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()

    st.write(fig)

#Tools for Data Analyst in NYC
    st.write("Tools for Data Analyst Roles in NY")
    x = top_technologies_da['technology']
    y = top_technologies_da['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Data Analyst in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()
    st.write(fig)


#Tools For Data Scientist 
    st.write("Tools for Data Scientist Roles in NY")

    x = top_technologies_ds['technology']
    y = top_technologies_ds['frequency']

    colors = cm.inferno_r(np.linspace(.2, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Data Scientists in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()
    st.write(fig)


#Tools For Web Developers
    st.write("Tools for Web Developers in NY")

    x = top_technologies_wb['technology']
    y = top_technologies_wb['frequency']

    colors = cm.inferno_r(np.linspace(.167, .8, 10))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Web Developers in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()
    st.write(fig)


#Tools For Front-end Developers
    st.write("Tools for Front-end Developers in NY")
    x = top_technologies_frtd['technology']
    y = top_technologies_frtd['frequency']

    # colors = cm.inferno_r(np.linspace(.167, .8, 10))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for Front End Developers in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()
    st.write(fig)



#Tools For Back-end Developers
    st.write("Tools for Back-endDevelopers in NY")

    x = top_technologies_backd['technology']
    y = top_technologies_backd['frequency']

    # colors = cm.inferno_r(np.linspace(.167, .8, 10))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for Back End Developers in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()
    st.write(fig)



#Tools For UI/UX Developers
    st.write("Tools for UI/UX Developers in NY")
    x = top_technologies_uiux['technology']
    y = top_technologies_uiux['frequency']

    # colors = cm.inferno_r(np.linspace(.167, .8, 10))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for UI/UX Developers in NY')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")

    plt.show()
    st.write(fig)