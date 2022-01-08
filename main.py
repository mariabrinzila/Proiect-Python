import tkinter as t
import get_input_generate_output as gigo


def button_action_function():
    """
    Function to call the submittedInput function with arguments in order to
    avoid a circular import
    :return: void
    """
    gigo.submittedInput(hashtag_variable, number_variable)


def close_window():
    """
    Function to close the window after the user is done searching
    :return: void
    """
    window.destroy()


# Create a basic GUI, get the hashtag and number of tweets from user
# Create window
window = t.Tk()
window.geometry("500x500")

# Get the hashtag from user
hashtag_variable = t.StringVar(value='#something')
ask_user_hashtag = t.Label(text="What hashtag do the tweets you're "
                                "looking for have?")
ask_user_hashtag.pack()
hashtag_entry = t.Entry(textvariable=hashtag_variable, width=25)
hashtag_entry.pack()

# Get the number of tweets from user
number_variable = t.IntVar(value=10)
ask_user_number = t.Label(text="How many tweets with that "
                               "hashtag shall we look for?")
ask_user_number.pack()
number_entry = t.Entry(textvariable=number_variable, width=25)
number_entry.pack()
okay = t.Button(window, text="All good", command=button_action_function)
okay.pack()

# Close window button
close_window = t.Button(window, text="Done searching", bg='black', fg='white',
                        activebackground='white', activeforeground='black',
                        command=close_window)
close_window.pack()

# Display the window
window.mainloop()
