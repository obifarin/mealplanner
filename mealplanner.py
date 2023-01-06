import streamlit as st
import openai
#import pyperclip

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


#def copy_to_clipboard(text):
#    pyperclip.copy(text)
#    st.write(f"Copied to clipboard")

# Copy to clipboard
#text_to_copy = copytext
#button_label = "Copy to clipboard"
#button_text = st.button(button_label)
#if button_text:
#    copy_to_clipboard(text_to_copy)

 # Frontend  

with st.sidebar:
    st.title("Meal Planner :coconut:")
    st.info("App by [Olatomiwa Bifarin](https://twitter.com/BifarinTheFifth) :male-technologist:")
    st.info("""Navigate to different sections via the side bar""")
    choice = st.radio("Navigation", ["Introduction", "Meal Plan", "Grocery List", "Recipe App"])
    st.sidebar.markdown('<a href="mailto:obifarin@yahoo.com">Any feedbacks?</a>', unsafe_allow_html=True)

# Frontend Panel 1
if choice == 'Introduction': 

    st.title("Autogenerate Meal Plans :shallow_pan_of_food:, Grocery Lists :memo:, Recipes :cucumber:")
    st.info(""":warning: The generative AI model (GPT-3) that powers this app will not perform well on meals that are not well represented on the web, such as African dishes. This is because the model was trained on all information on the web. Furthermore, the model can occassionally give errorneous output. **Validation is required**.""")
    st.image("meal-plan.png", caption='Olatomiwa X DALLE-2') #, width=500

# Frontend Panel 2
if choice == 'Meal Plan': 

    st.markdown("## Generate Meal Plan :shallow_pan_of_food:")

    with st.form(key="form"):
        prompt = st.text_input("Name of the diet", value= "Keto")
        st.info(f"Only include the keyword. For example: Keto, Carnivore, Jain, etc.")
        st.write("Don't know where to start? Click here for list of [diet](https://en.wikipedia.org/wiki/List_of_diets)")

        submit_button = st.form_submit_button(label='Generate Meal plan')

        boilerPrompt = ("Give me a detailed meal plan for a week for %s diet starting with the heading Day 1, Day 2, and so on. Be sure to include snacks. Also start each meal (that is breakfast, lunch, dinner, snack) on a new line." %prompt)

        if submit_button:
            with st.spinner("Generating your meal plan, work in progress..."):
                output = mealplan(boilerPrompt)
            st.markdown("### Meal plan Output:")
            st.info(":bookmark: Note: I am aware of the need for a 'copy to clipboard' functionality, in the meantime, copy and paste the entire output in another document before leaving this page. This list will be used to generate your grocery list. You can use :link: [aNotepad](https://anotepad.com/)")
        
            st.write(output)
            st.info(""":warning: Recall that the generative AI model (GPT-3) can occassionally give errorneous output. Validation is required.""")

            st.markdown("____")

  
        
# Frontend Panel 3
if choice == 'Grocery List': 

    st.markdown("## Generate Grocery List for a Meal Plan :memo:")

    with st.form(key="form2"):
        prompt = st.text_input("Paste your meal plan")

        submit_button = st.form_submit_button(label='Generate Grocery List')

        boilerPrompt = ("Generate a list of what to buy from the grocery store from this. Make sure they are raw food: %s" %prompt)

        if submit_button:
            with st.spinner("Generating your grocery list, work in progress..."):
                output = mealplan(boilerPrompt)
            st.markdown("### Grocery list output:")
            st.info(":bookmark: Note: I am aware of the need for a 'copy to clipboard' functionality, in the meantime, copy and paste the output in another document before leaving this page, if you need it. You can use :link: [aNotepad](https://anotepad.com/)")
        
            st.write(output)
            st.info(""":warning: Recall that the generative AI model (GPT-3) can occassionally give errorneous output. Validation is required.""")

            st.markdown("____")        

# Frontend Panel 4
if choice == 'Recipe App': 

    st.markdown("## Generate Recipe for Your Meal :green_salad:")

    with st.form(key="form3"):
        prompt = st.text_input("Name of the meal")
        st.info(f"Copy and paste a meal from your generated meal plan (or other meal).")

        submit_button = st.form_submit_button(label='Generate meal recipe')

        boilerPrompt = ("Provide a detailed step-by-step plan to make this meal: %s " %prompt)

        if submit_button:
            with st.spinner("Generating your recipe, work in progress..."):
                output = mealplan(boilerPrompt)
            st.markdown("### Recipe Output:")
        
            st.write(output)
            st.info(""":warning: Recall that the generative AI model (GPT-3) can occassionally give errorneous output. Validation is required.""")

            st.markdown("____")