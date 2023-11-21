#Lab 9
# Author: Frank R. Leotta III

"""_summary_

This lab is designed to create a simple web 
application using streamlit and create a simple Date counter using datetime.
"""

# 1. We will first need to activate and install streamlit.
# create virtual environment (in terminal) : python -m venv venv (venv is the name of the virtual environment)
# pip install streamlit (in terminal)

# 2. Import streamlit here as st and datetime as dt
import datetime as dt
import streamlit as st

# 3. Create a title for your web application. Streamlit has a function for this called title
st.title("Date Counter  Web Application")

# 4. Create a subheader for your web application. Streamlit has a function for this called subheader
st.subheader("This Web Application will calculate the number of days until a certain date")
# 5. Create a date input for the user to enter a date. Streamlit has a function for this called date_input
# Make sure to save the input into a variable
date = st.date_input("Enter a date: ", format="MM/DD/YYYY") 
#(additional ideas), value=dt.datetime.now())  min_value=dt.date(1900, 1, 1), max_value=dt.date(2100, 12, 31))

# 6. Create a button for the user to click. Streamlit has a function for this called button
# Make sure to save the button click into a variable
button = st.button("Calculate")
#at this point, need to go to question 8 and create the app function to view
# if true it triggures something



# 7. Create a function that will calculate the number of days until the date entered by the user.
# You will need to use the datetime library for this.
# You will need to convert the user input into a datetime object.
# You will need to get the current date and convert it into a datetime object.
# You will need to subtract the current date from the user input date.
# You will need to return the number of days.
# The function should take in a datetime.date as a parameter.
# The function should return an integer.
# The function should be called calculate_days
def calculate_days(date)->int:
    """_summary_
        Returns the number of days until the date entered by the user.

    Args:
        date (date): The date entered by the user. Format: YYYY-MM-DD

    Returns:
        int: The number of days until the date entered by the user.
    """
    #get the current date
    current_date = dt.datetime.now().date()
    #calculate the number of days until the date entered by the user
    days_difference = date - current_date
    #Debugging to see if what the days_difference is
    st.write(days_difference.days)
    if days_difference.days < 0:
        raise ValueError("The date entered is in the past.")
    return days_difference.days

 #additonal way of doing it:
# try:
#     date = dt.datetime.strptime(date, '%Y-%m-%d')
#     today = dt.datetime.now()
#     days = date - today
#     return days.days
# except:
#     return "Error"


# 8. Create an app function that will run the web application.
# Check if the button has been clicked, then call the calculate_days function and pass in the date entered by the user. Use a try except block to catch any errors.
# Save the result into a variable.
# Print out the result.
def app():
    if button:
        # st.write("you clicked me")  #this is just to test if the button works
        try:
            result = calculate_days(date)
        #    st.write(" Hello, you pressed me") returns a press me statment
        except ValueError:
            st.write("Please enter a valid date.")
            return
    st.write(f"Current Date: {dt.datetime.now().date()}")
    st.write(f"Selected Date: {date}")
    st.write(f'Days until selected date: {result}')

        # try:    # this is to test if the date is being entered correctly
        #     result = calculate_days(date)
        #     st.write(result)
        # except:
        #     st.write("Error")

# 9. Run the web application by typing streamlit run Lab9.py in the terminal.

# 10. Enter a date in the format of YYYY-MM-DD and click the button.
# 11. Check to see if the number of days until the date entered is correct.
# 12. If the number of days is correct, then you have completed the lab.
# 13. If the number of days is incorrect, then you will need to debug your code.

if __name__ == '__main__':
    app()
