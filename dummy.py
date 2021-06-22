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
    st.title('Dummy page')
    schedule_type = clean_data()
    fig, axes = plt.subplots(figsize=(20,5))
    x = schedule_type[schedule_type['schedule_type'] == 'Contractor']['job_category'] 
    y1 = schedule_type[schedule_type['schedule_type'] == 'Contractor']['title']
    y2 =  schedule_type[schedule_type['schedule_type'] == 'Internship']['title']
    labels = schedule_type[schedule_type['schedule_type'] == 'Contractor']['job_category'] 

    m = np.arange(7)
    width = 0.35
    axes.bar(m - width/2,y1, label = 'Contractor', width = width, color = 'blue')
    axes.bar(m + width/2, y2, label = 'internship', width = width, color = 'red')
    # labels = axes.get_xticklabels()
    axes.set_xticks(m)
    axes.set_xticklabels(labels)
    axes.set(xlabel='Job titles', label='frequency',\
        title="Distribution of Schedule Types Across Different Tech Roles")
    plt.legend()
    plt.show()

    st.write(fig)

   #plotting pie chart
    figure, axes = plt.subplots(figsize = (10,10))
    axes.pie(pie_schedule_type['title'], labels = pie_schedule_type['schedule_type'], explode = (0.6, 0, 0.6, 0.6),
        wedgeprops= {"edgecolor":"black",
                     'linewidth': 0.4,
                     'antialiased': True})
    axes.set(title ='The Overall distribution of schedule types')
    axes.axis('equal')
    plt.legend() 
    st.write(figure)


#
    ax = data[data["location_category"] == "atlanta georgia" ].groupby("job_category").size()
    # ax.set_title("Atlanta Tech Jobs")
    st.bar_chart(ax)