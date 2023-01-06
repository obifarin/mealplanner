import streamlit as st
import openai

# Backend 

openai.api_key = "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"

def mealplan(userPrompt):
    """Returns a generated an meal plan using GPT3 with a certain prompt"""
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= userPrompt,
        temperature=0.71,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response.get("choices")[0]['text']


 # Frontend  

with st.sidebar:
    st.title("Meal Planner :coconut:")
    st.info("App by Olatomiwa Bifarin :male-technologist:")
    choice = st.radio("Navigation", ["Introduction", "Meal Plan", "Grocery List", "Recipe App"])

# Frontend Panel 1
if choice == 'Introduction': 

    st.title("Autogenerate Meal Plans :shallow_pan_of_food:, Grocery Lists :memo:, Recipes :cucumber:")
    st.info("""Navigate to different sections via the side bar""")
    st.info("""NOTE: The generative model will not perform well on meals that are not well represented on the web, such as African dishes. The AI model used is GPT-3 model, trained on all information on the web. Furthermore, the model can occassionally give errorneous output""")
    st.image("meal-plan.png", caption='Olatomiwa X DALLE-2') #, width=500

# Frontend Panel 2
if choice == 'Meal Plan': 

    st.markdown("## Generate Meal Plan :shallow_pan_of_food:")

    with st.form(key="form"):
        prompt = st.text_input("Name of the diet")
        st.info(f"Only include the keyword. For example: Keto, Elemental, Carnivore, Jain, Atkins.")
        st.write("Don't know where to start? Click here for list of [diet](https://en.wikipedia.org/wiki/List_of_diets)")

        submit_button = st.form_submit_button(label='Generate Meal plan')

        boilerPrompt = ("Give me a detailed meal plan for a week for %s diet starting with the heading Day 1, Day 2, and so on. Be sure to include snacks." %prompt)

        if submit_button:
            with st.spinner("Generating Meal plan..."):
                output = mealplan(boilerPrompt)
            st.markdown("### Meal plan Output:")
            st.markdown("#### [Note: copy and paste the output in another browser before leaving this page. You can use [a note pad](https://anotepad.com/)]")
        
            st.write(output)

            st.markdown("____")
        
# Frontend Panel 3
if choice == 'Grocery List': 

    st.markdown("## Generate Grocery List for a Meal Plan :memo:")

    with st.form(key="form2"):
        prompt = st.text_input("Paste your meal plan")

        submit_button = st.form_submit_button(label='Generate Grocery List')

        boilerPrompt = ("Generate a list of what to buy from the grocery store from this: %s" %prompt)

        if submit_button:
            with st.spinner("Generating grocery list..."):
                output = mealplan(boilerPrompt)
            st.markdown("### Grocery list output:")
            st.markdown("#### [Note: copy and paste the output before leaving this page, if you will need it.]")
        
            st.write(output)

            st.markdown("____")        

# Frontend Panel 4
if choice == 'Recipe App': 

    st.markdown("## Generate Recipe for Your Meal :green_salad:")

    with st.form(key="form3"):
        prompt = st.text_input("Name of the meal")
        st.info(f"Copy and paste a meal from your generated meal plan (or any meal for that matter).")

        submit_button = st.form_submit_button(label='Generate meal recipe')

        boilerPrompt = ("Provide a detailed step-by-step plan to make this meal: %s " %prompt)

        if submit_button:
            with st.spinner("Generating Mealplan..."):
                output = mealplan(boilerPrompt)
            st.markdown("### Meal plan Output:")
        
            st.write(output)

            st.markdown("____")