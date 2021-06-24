import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.read_csv("datasets/updated_categories_employment_data.csv")
df_schedule_type = data[~data['schedule_type'].isna()]
df_schedule_type['schedule_type'] = df_schedule_type['schedule_type'].replace('Full–time', 'Full-time')
pie_schedule_type = df_schedule_type.groupby('schedule_type', as_index=False).count()

def clean_data():
    df_schedule_type = data[~data['schedule_type'].isna()]
    df_schedule_type['schedule_type'] = df_schedule_type['schedule_type'].replace('Full–time', 'Full-time')
    schedule_type = df_schedule_type.groupby(['job_category', 'schedule_type'], as_index=False).count()
    return schedule_type

def app():
    st.title('Comprehensive View Across Our Cities')

    st.write("Tech Jobs In Our Cities")
    ax = data.groupby(["location_category"]).size()
    st.bar_chart(ax)


    schedule_type = clean_data()



   #plotting pie chart
    figure, axes = plt.subplots(figsize = (10,10))
    axes.pie(pie_schedule_type['title'], labels = pie_schedule_type['schedule_type'], explode = (0.6, 0, 0.6, 0.6),
        wedgeprops= {"edgecolor":"black",
                     'linewidth': 0.4,
                     'antialiased': True})
    axes.set(title ='The Overall Distribution of Schedule Types')
    axes.axis('equal')
    plt.legend() 
    st.pyplot(figure)

    #inserting a new row for software engineer
    new_row = ['software engineer', 'Part-time', 0,0,0,0,0,0,0,0,0]
    schedule_type = pd.DataFrame(np.insert(schedule_type.values, -5, new_row, axis=0), columns = ['job_category', 'schedule_type', 'title', 'company_name', 'location','via', 'location_category', 'description', 'job_id', 'lowercase_title','lowercase_description'])

    #creating bar graph for full time roles
    st.write('Distribution of Full-time Roles Per Job Title')
    fig, axes = plt.subplots(figsize=(20,10))
    x = schedule_type[schedule_type['schedule_type'] == 'Contractor']['job_category'] 
    y3 =  schedule_type[schedule_type['schedule_type'] == 'Full-time']['title']
    labels = schedule_type[schedule_type['schedule_type'] == 'Contractor']['job_category'] 

    m = np.arange(7)
    width = 0.35
    axes.bar(x,y3, label = 'Full-time', color = 'orangered')
    axes.set_xticks(m)
    axes.set_xticklabels(labels)
    plt.xlabel('Job titles', fontsize=20)
    plt.ylabel('Number of Job Postings', fontsize=20)
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize = 20)
    st.write(fig)

    #graphing for part-time, contractor, and internships
    fig, axes = plt.subplots(figsize=(20,10))
    x = schedule_type[schedule_type['schedule_type'] == 'Contractor']['job_category'] 
    y1 = schedule_type[schedule_type['schedule_type'] == 'Contractor']['title']
    y2 =  schedule_type[schedule_type['schedule_type'] == 'Internship']['title']
    y3 =  schedule_type[schedule_type['schedule_type'] == 'Part-time']['title']
    labels = schedule_type[schedule_type['schedule_type'] == 'Contractor']['job_category'] 

    m = np.arange(7)
    width = 0.35
    axes.bar(m-width, y1, label = 'Contractor', width = width, color = 'darkcyan', align='edge')
    axes.bar(m, y2, label = 'internship', width = width, color = 'palevioletred')
    axes.bar(m + width, y3, label = 'full-time', width = width, color = 'royalblue')
    axes.set_xticks(m)
    axes.set_xticklabels(labels)
    plt.xlabel('Job Titles', fontsize=20)
    plt.ylabel('Number of Job Postings', fontsize=20)
    plt.xticks(rotation=-45, ha="left", rotation_mode="anchor")
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize = 20)
    st.write('Distribution of Schedule Types Across Different Tech Roles')
    st.write(fig)


