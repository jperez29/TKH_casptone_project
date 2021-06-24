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

software_engineer_atlanta = job_postings('software engineer', 'atlanta georgia')
data_analyst_atlanta = job_postings('data analyst', 'atlanta georgia')
web_developer_atlanta = job_postings('web developer', 'atlanta georgia')
data_scientist_atlanta = job_postings('data scientist', 'atlanta georgia')
front_end_developer_atlanta = job_postings('front-end developer', 'atlanta georgia')
back_end_developer_atlanta = job_postings('back-end developer', 'atlanta georgia')
uiux_designer_atlanta = job_postings('UI/UX designer', 'atlanta georgia')


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

software_engineeratlanta = Jobs()
software_engineeratlanta.append_tech(software_engineer_atlanta['lowercase_description'])
software_engineeratlanta.tech

data_analystatlanta = Jobs()
data_analystatlanta.append_tech(data_analyst_atlanta['lowercase_description'])
data_analystatlanta.tech

data_scientistatlanta = Jobs()
data_scientistatlanta.append_tech(data_scientist_atlanta['lowercase_description'])
data_scientistatlanta.tech

web_developeratlanta = Jobs()
web_developeratlanta.append_tech(web_developer_atlanta['lowercase_description'])
web_developeratlanta.tech

frontend_developeratlanta = Jobs()
frontend_developeratlanta.append_tech(front_end_developer_atlanta['lowercase_description'])
frontend_developeratlanta.tech

backend_developeratlanta = Jobs()
backend_developeratlanta.append_tech(back_end_developer_atlanta['lowercase_description'])
backend_developeratlanta.tech

uiux_designeratlanta = Jobs()
uiux_designeratlanta.append_tech(uiux_designer_atlanta['lowercase_description'])
uiux_designeratlanta.tech

#converting all dictionaries to dataframes

tech_software_engineer_atlanta = pd.DataFrame(list(software_engineeratlanta.tech.items()), columns=['technology', 'frequency'])
tech_data_analyst_atlanta = pd.DataFrame(list(data_analystatlanta.tech.items()), columns=['technology', 'frequency'])
tech_data_scientist_atlanta = pd.DataFrame(list(data_scientistatlanta.tech.items()), columns=['technology', 'frequency'])
tech_web_developer_atlanta = pd.DataFrame(list(web_developeratlanta.tech.items()), columns=['technology', 'frequency'])
tech_frontend_developer_atlanta = pd.DataFrame(list(frontend_developeratlanta.tech.items()), columns=['technology', 'frequency'])
tech_backend_developer_atlanta = pd.DataFrame(list(backend_developeratlanta.tech.items()), columns=['technology', 'frequency'])
tech_uiux_developer_atlanta = pd.DataFrame(list(uiux_designeratlanta.tech.items()), columns=['technology', 'frequency'])

#selecting the top 10 technologies per role

top_tech_se_atlanta = tech_software_engineer_atlanta.sort_values(by='frequency', ascending=False).head(10)
top_tech_da_atlanta = tech_data_analyst_atlanta.sort_values(by='frequency', ascending=False).head(10)
top_tech_ds_atlanta = tech_data_scientist_atlanta.sort_values(by='frequency', ascending=False).head(10)
top_tech_wb_atlanta = tech_web_developer_atlanta.sort_values(by='frequency', ascending=False).head(10)
top_tech_frtdev_atlanta = tech_frontend_developer_atlanta.sort_values(by='frequency', ascending=False).head(10)
top_tech_backdev_atlanta = tech_backend_developer_atlanta.sort_values(by='frequency', ascending=False).head(10)
top_tech_uiux_atlanta = tech_uiux_developer_atlanta.sort_values(by='frequency', ascending=False).head(10)

def app():
    st.title('ATLANTA')

    st.write("Atlanta, also referred to as “the Silicon Valley of the South,” is proving to be a leading city for start-ups and tech companies in a variety of industries. Below you will find some of the top tech jobs as well as their technologies and skills. Also, take a look at resources such as The Knowledge House and Built in Atlanta for further information about salaries, companies, job postings and opportunities to upskill.")
    st.write("")
    st.write("Tech Jobs in Atlanta")
    ax = data[data["location_category"] == "atlanta georgia" ].groupby("job_category").size()
    # ax.set_title("Atlanta Tech Jobs")
    st.bar_chart(ax)
    #---------graph for software engineer-----------------------------

    x = top_tech_se_atlanta['technology']
    y = top_tech_se_atlanta['frequency']
    # x = ['Scala', 'Java', 'Python', 'AWS', 'SQL', 'Git', 'React', 'JavaScript', 'Kubernetes', 'IDEs']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x,y, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write("The Top Technologies Required by Employers For Software Engineers in Atlanta, GA")
    st.write(fig)
    #---------graph for data analyst------------------------------

    x_da = top_tech_da_atlanta['technology']
    y_da = top_tech_da_atlanta['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_da,y_da, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write('The Top Technologies/Skills Required by Employers For Data Analyst in Atlanta, GA')
    st.write(fig)

    #---------graph for data scientist-----------------------------


    x_ds = top_tech_ds_atlanta['technology']
    y_ds = top_tech_ds_atlanta['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_ds,y_ds, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write('The Top Technologies/Skills Required by Employers For Data Scientist in Atlanta, GA')
    st.write(fig)

    #---------graph for web developer-----------------------------

    x_wdev = top_tech_wb_atlanta['technology']
    y_wdev = top_tech_wb_atlanta['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_wdev,y_wdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    st.write('The Top Technologies/Skills Required by Employers For Web Developer in Atlanta, GA')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for front end developer-----------------------------

    x_frtdev = top_tech_frtdev_atlanta['technology']
    y_frtdev = top_tech_frtdev_atlanta['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_frtdev,y_frtdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    st.write('The Top Technologies/Skills Required by Employers for front end developers in Atlanta, GA')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)

    #---------graph for backend developer-----------------------------

    x_backdev = top_tech_backdev_atlanta['technology']
    y_backdev = top_tech_backdev_atlanta['frequency']

    colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    # my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_backdev,y_backdev, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    st.write('The Top Technologies/Skills Required by Employers for Back End developers in Atlanta, GA')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
    #---------graph for uiux designer-----------------------------
    top_tech_uiux_atlanta 

    x_uiux = top_tech_uiux_atlanta['technology']
    y_uiux = top_tech_uiux_atlanta['frequency']

    # colors = cm.inferno_r(np.linspace(.5, .8, 5))
    # colors = ['lightcoral', 'b', 'cadetblue', 'turquoise','palegreen','indigo']
    my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(x)))

    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(x_uiux,y_uiux, color = colors)
    ax.set(xlabel='technology', ylabel = 'Frequency')
    st.write('The Top Technologies/Skills Required by Employers for UI/UX designers in Atlanta, GA')
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    st.write(fig)
   