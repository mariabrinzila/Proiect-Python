import tkinter as t
import get_input_generate_output as gigo

# create GUI
# create a window
window = t.Tk()
window.geometry("750x250")

# get hashtag from user
hashtag_variable = t.StringVar()
ask_user_hashtag = t.Label(text="What hashtag do the tweets you're looking for have?")
ask_user_hashtag.pack()
hashtag_entry = t.Entry(textvariable=hashtag_variable, width=25)
hashtag_entry.pack()

# get number of tweets from user
number_variable = t.IntVar()
ask_user_number = t.Label(text="How many tweets with that hashtag shall we look for?")
ask_user_number.pack()
number_entry = t.Entry(textvariable=number_variable, width=25)
number_entry.pack()
okay = t.Button(window, text="All good!", command=gigo.submittedInput)
okay.pack()

# display the window
window.mainloop()
