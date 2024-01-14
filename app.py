import os
import openai
import streamlit as st

# Retrieve the OpenAI API key from the environment variables
openai_api_key = st.secrets['OPENAI_API_KEY']

# Set the OpenAI API key
#openai.api_key = openai_api_key

# Create an OpenAI client with the API key
#client = openai.OpenAI(api_key=openai_api_key)

# Set the title of the Streamlit application
st.title('Creative Writing Generator')

# Add a dropdown menu for the user to select the type of creative writing
creative_type = st.selectbox(
   'Choose the type of creative writing:',
   ('Sonnet', 'Haiku', 'Limerick', 'Rap Song', "Children's Story", 'Horror Story', 'Comedy'))

# Prompt the user to enter a subject or theme
user_input = st.text_input("Enter a theme or subject: ")

# Check if the 'Generate' button is clicked
if st.button('Generate'):
   # Display a loading spinner while the content is being generated
   with st.spinner('Generating your content...'):
       # Determine the system message based on the selected type
       if creative_type in ['Sonnet', 'Haiku', 'Limerick']:
           system_message = f"You are a poet and you write {creative_type}"
       elif creative_type == 'Rap Song':
           system_message = "You are a rapper crafting a new rap song"
       elif creative_type == "Children's Story":
           system_message = "You are an author writing a children's story"
       elif creative_type == 'Horror Story':
           system_message = "You are an author crafting a horror story"
       else: # Comedy
           system_message = "You are a writer creating a comedic piece"

       # Generate the response from OpenAI
       response = openai.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[
               {
                   "role": "system",
                   "content": system_message
               },
               {
                   "role": "user",
                   "content": user_input
               },
           ],
           temperature=1,
           max_tokens=256,
           top_p=1,
           frequency_penalty=0,
           presence_penalty=0
       )

       # Extract and display the content
       message_content = response.choices[0].message.content
       st.text_area("Generated Content: ", value=message_content, height=200)
