import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from itertools import cycle, islice

data = pd.read_csv("datasets/updated_categories_employment_data.csv")


plt.show()

def job_postings(job_category, location):
    return data[(data['job_category'] == job_category) & (data['location_category'] == location)]

software_engineer_newark = job_postings('software engineer', 'newark new jersey')
data_analyst_newark = job_postings('data analyst', 'newark new jersey')
web_developer_newark = job_postings('web developer', 'newark new jersey')
data_scientist_newark = job_postings('data scientist', 'newark new jersey')
front_end_developer_newark = job_postings('front-end developer', 'newark new jersey')
back_end_developer_newark = job_postings('back-end developer', 'newark new jersey')
uiux_designer_newark = job_postings('UI/UX designer', 'newark new jersey')


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

software_engineernewark = Jobs()
software_engineernewark.append_tech(software_engineer_newark['lowercase_description'])
software_engineernewark.tech

data_analystnewark = Jobs()
data_analystnewark.append_tech(data_analyst_newark['lowercase_description'])
data_analystnewark.tech

data_scientistnewark = Jobs()
data_scientistnewark.append_tech(data_scientist_newark['lowercase_description'])
data_scientistnewark.tech

web_developernewark = Jobs()
web_developernewark.append_tech(web_developer_newark['lowercase_description'])
web_developernewark.tech

frontend_developernewark = Jobs()
frontend_developernewark.append_tech(front_end_developer_newark['lowercase_description'])
frontend_developernewark.tech

backend_developernewark = Jobs()
backend_developernewark.append_tech(back_end_developer_newark['lowercase_description'])
backend_developernewark.tech

uiux_designernewark = Jobs()
uiux_designernewark.append_tech(uiux_designer_newark['lowercase_description'])
uiux_designernewark.tech

#converting all dictionaries to dataframes

tech_software_engineer_newark = pd.DataFrame(list(software_engineernewark.tech.items()), columns=['technology', 'frequency'])
tech_data_analyst_newark = pd.DataFrame(list(data_analystnewark.tech.items()), columns=['technology', 'frequency'])
tech_data_scientist_newark = pd.DataFrame(list(data_scientistnewark.tech.items()), columns=['technology', 'frequency'])
tech_web_developer_newark = pd.DataFrame(list(web_developernewark.tech.items()), columns=['technology', 'frequency'])
tech_frontend_developer_newark = pd.DataFrame(list(frontend_developernewark.tech.items()), columns=['technology', 'frequency'])
tech_backend_developer_newark = pd.DataFrame(list(backend_developernewark.tech.items()), columns=['technology', 'frequency'])
tech_uiux_developer_newark = pd.DataFrame(list(uiux_designernewark.tech.items()), columns=['technology', 'frequency'])

#selecting the top 10 technologies per role

top_tech_se_newark = tech_software_engineer_newark.sort_values(by='frequency', ascending=False).head(10)
top_tech_da_newark = tech_data_analyst_newark.sort_values(by='frequency', ascending=False).head(10)
top_tech_ds_newark = tech_data_scientist_newark.sort_values(by='frequency', ascending=False).head(10)
top_tech_wb_newark = tech_web_developer_newark.sort_values(by='frequency', ascending=False).head(10)
top_tech_frtdev_newark = tech_frontend_developer_newark.sort_values(by='frequency', ascending=False).head(10)
top_tech_backdev_newark = tech_backend_developer_newark.sort_values(by='frequency', ascending=False).head(10)
top_tech_uiux_newark = tech_uiux_developer_newark.sort_values(by='frequency', ascending=False).head(10)

def app():
    st.title('NEWARK')
    #---------graph for software engineer-----------------------------

    x = top_tech_se_newark['technology']
    y = top_tech_se_newark['frequency']
    # x = ['Scala', 'Java', 'Python', 'AWS', 'SQL', 'Git', 'React', 'JavaScript', 'Kubernetes', 'IDEs']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies Required by Employers For Software Engineers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for data analyst------------------------------

    x_da = top_tech_da_newark['technology']
    y_da = top_tech_da_newark['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_da,y_da, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Data Analyst in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for data scientist-----------------------------


    x_ds = top_tech_ds_newark['technology']
    y_ds = top_tech_ds_newark['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_ds,y_ds, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Data Scientist in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for web developer-----------------------------

    x_wdev = top_tech_wb_newark['technology']
    y_wdev = top_tech_wb_newark['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_wdev,y_wdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers For Web Developer in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for front end developer-----------------------------

    x_frtdev = top_tech_frtdev_newark['technology']
    y_frtdev = top_tech_frtdev_newark['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_frtdev,y_frtdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for front end developers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for backend developer-----------------------------

    x_backdev = top_tech_backdev_newark['technology']
    y_backdev = top_tech_backdev_newark['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_backdev,y_backdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for Back End developers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for uiux designer-----------------------------
    top_tech_uiux_newark 

    x_uiux = top_tech_uiux_newark['technology']
    y_uiux = top_tech_uiux_newark['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_uiux,y_uiux, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency', title ='The Top Technologies/Skills Required by Employers for UI/UX designers in Newark, NJ')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)