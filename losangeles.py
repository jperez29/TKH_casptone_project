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

software_engineer_LA = job_postings('software engineer', 'los angeles california')
data_analyst_LA = job_postings('data analyst', 'los angeles california')
web_developer_LA = job_postings('web developer', 'los angeles california')
data_scientist_LA = job_postings('data scientist', 'los angeles california')
front_end_developer_LA = job_postings('front-end developer', 'los angeles california')
back_end_developer_LA = job_postings('back-end developer', 'los angeles california')
uiux_designer_LA = job_postings('UI/UX designer', 'los angeles california')


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

#getting the dictionary of technologies for all roles

software_engineerlos_angeles = Jobs()
software_engineerlos_angeles.append_tech(software_engineer_LA['lowercase_description'])
software_engineerlos_angeles.tech

data_analystlos_angeles = Jobs()
data_analystlos_angeles.append_tech(data_analyst_LA['lowercase_description'])
data_analystlos_angeles.tech

data_scientistlos_angeles = Jobs()
data_scientistlos_angeles.append_tech(data_scientist_LA['lowercase_description'])
data_scientistlos_angeles.tech

web_developerlos_angeles = Jobs()
web_developerlos_angeles.append_tech(web_developer_LA['lowercase_description'])
web_developerlos_angeles.tech

frontend_developerlos_angeles = Jobs()
frontend_developerlos_angeles.append_tech(front_end_developer_LA['lowercase_description'])
frontend_developerlos_angeles.tech

backend_developerlos_angeles = Jobs()
backend_developerlos_angeles.append_tech(back_end_developer_LA['lowercase_description'])
backend_developerlos_angeles.tech

uiux_designerlos_angeles = Jobs()
uiux_designerlos_angeles.append_tech(uiux_designer_LA['lowercase_description'])
uiux_designerlos_angeles.tech

#converting all dictionaries to dataframes

tech_software_engineer_la = pd.DataFrame(list(software_engineerlos_angeles.tech.items()), columns=['technology', 'frequency'])
tech_data_analyst_la = pd.DataFrame(list(data_analystlos_angeles.tech.items()), columns=['technology', 'frequency'])
tech_data_scientist_la = pd.DataFrame(list(data_scientistlos_angeles.tech.items()), columns=['technology', 'frequency'])
tech_web_developer_la = pd.DataFrame(list(web_developerlos_angeles.tech.items()), columns=['technology', 'frequency'])
tech_frontend_developer_la = pd.DataFrame(list(frontend_developerlos_angeles.tech.items()), columns=['technology', 'frequency'])
tech_backend_developer_la = pd.DataFrame(list(backend_developerlos_angeles.tech.items()), columns=['technology', 'frequency'])
tech_uiux_developer_la = pd.DataFrame(list(uiux_designerlos_angeles.tech.items()), columns=['technology', 'frequency'])

#selecting the top 10 technologies per role from dataframe

top_tech_se_la = tech_software_engineer_la.sort_values(by='frequency', ascending=False).head(10)
top_tech_da_la = tech_data_analyst_la.sort_values(by='frequency', ascending=False).head(10)
top_tech_ds_la = tech_data_scientist_la.sort_values(by='frequency', ascending=False).head(10)
top_tech_wb_la = tech_web_developer_la.sort_values(by='frequency', ascending=False).head(10)
top_tech_frtdev_la = tech_frontend_developer_la.sort_values(by='frequency', ascending=False).head(10)
top_tech_backdev_la = tech_backend_developer_la.sort_values(by='frequency', ascending=False).head(10)
top_tech_uiux_la = tech_uiux_developer_la.sort_values(by='frequency', ascending=False).head(10)

def app():
    st.title('NEWARK')
    #---------graph for software engineer-----------------------------

    x = top_tech_se_la['technology']
    y = top_tech_se_la['frequency']
    # x = ['Scala', 'Java', 'Python', 'AWS', 'SQL', 'Git', 'React', 'JavaScript', 'Kubernetes', 'IDEs']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies Required by Employers For Software Engineers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for data analyst------------------------------

    x_da = top_tech_da_la['technology']
    y_da = top_tech_da_la['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_da,y_da, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Data Analyst in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for data scientist-----------------------------


    x_ds = top_tech_ds_la['technology']
    y_ds = top_tech_ds_la['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_ds,y_ds, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Data Scientist in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for web developer-----------------------------

    x_wdev = top_tech_wb_la['technology']
    y_wdev = top_tech_wb_la['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_wdev,y_wdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Web Developer in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for front end developer-----------------------------

    x_frtdev = top_tech_frtdev_la['technology']
    y_frtdev = top_tech_frtdev_la['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_frtdev,y_frtdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for front end developers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for backend developer-----------------------------

    x_backdev = top_tech_backdev_la['technology']
    y_backdev = top_tech_backdev_la['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_backdev,y_backdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for Back End developers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for uiux designer-----------------------------

    x_uiux = top_tech_uiux_la['technology']
    y_uiux = top_tech_uiux_la['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_uiux,y_uiux, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for UI/UX designers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)