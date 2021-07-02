import streamlit as st
from PIL import Image

def app():
    st.title('Meet the team')

    col1, col2, col3 = st.beta_columns(3)

    Janet = Image.open('janet_perez.jpg')
    col1.header("Janet Perez")
    col1.image(Janet, caption ="Janet Perez is passionately pursuing a career at the intersection of data science, technology, and mathematics. She obtained her Bachelor's in math and biology from Binghamton University and worked as a math tutor upon graduating from college. Currently, she’s a data science fellow at The Knowledge House, a nonprofit organization focused on training people to pursue careers in the tech sector.  Janet finds the power of technology fascinating in being able to help us find patterns and insights in data that would be hard to find without the use of computers. Janet is committed to combining her technical skills with her background in math and biology to join a company that derives data-driven decisions, makes a lasting impact in people’s lives, fosters growth-mindsets, and values community perspectives in its research.", use_column_width=True)

    Elston = Image.open('IMG_2905 (1).jpg')
    col2.header("Elston Bell Jr.")
    col2.image(Elston, caption ="Elston Bell, Jr. is a multi-disciplinary storyteller based in NYC, who seeks to create and capture the complete stories of others through words, data, and visuals. Since graduating from UCLA in 2019 with a Bachelor of Science in Human Biology & Society, Elston has been working on various projects to develop and refine both his technical and creative skills. With the tagline “connect x code x create,” he hopes to integrate his diverse passions into a complementary style to produce content for social change. These passions include co-hosting the Speaking Our Language podcast, being a Data Science Fellow, and being the founder of Black Boys Lit.", use_column_width=True)

    Chioma = Image.open("chiomadunkley_headshot.jpg")
    col3.header("Chioma Dunkley")
    col3.image(Chioma, caption ="Chioma is a Data Science Fellow, Content Contributor, and Customer Success intern. She aspires to help people harness data to improve lives and experiences. She hopes to be able to articulate what she’s learning in the tech field to everyday people in everyday terms. Ultimately she wants to be intentional in truly making tech accessible and inclusive to those from underrepresented and nontraditional backgrounds.She wants people, and especially Black people, regardless of their background to know that tech is an option for them and a space where they can learn no matter their age or stage in their lives.", use_column_width=True)