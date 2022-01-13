import tkinter as t
import get_input_generate_output as gigo


class GraphicInterface:
    def __init__(self):
        """
        GraphicInterface class constructor that creates a basic GUI and
        takes the hashtag and number of tweets from the user
        """
        # Create window
        self.window = t.Tk()
        self.window.title("Search for tweets")
        self.window.geometry("600x500")
        self.window.configure(background="black")

        # Get the hashtag from user
        self.hashtag_variable = t.StringVar(value="#something")
        ask_user_hashtag = t.Label(
            text="What hashtag do the tweets you're looking for have?",
            bg="black", fg="white", font="Arial 9 bold")
        hashtag_entry = t.Entry(textvariable=self.hashtag_variable, width=25,
                                bg="black", fg="white")

        # Get the number of tweets from user
        self.number_variable = t.IntVar(value=10)
        ask_user_number = t.Label(
            text="How many tweets with that hashtag shall we look for?",
            bg="black", fg="white", font="Arial 9 bold")
        number_entry = t.Entry(textvariable=self.number_variable, width=25,
                               bg="black", fg="white")

        # Submit input button
        okay = t.Button(self.window, text="All good", bg="sky blue",
                        fg="black", width=15, height=2,
                        font="Arial 9 bold",
                        command=self.button_action_function)

        # Close window button
        close_window_button = t.Button(self.window, text="Done searching",
                                       bg="sky blue", fg="black", width=15,
                                       height=2, font="Arial 9 bold",
                                       command=self.close_window)

        # Put entries, widgets and buttons in a grid
        ask_user_hashtag.grid(column=0, row=0, pady=(20, 10), padx=(10, 20))
        hashtag_entry.grid(column=1, row=0, pady=(20, 10), padx=(20, 10))

        ask_user_number.grid(column=0, row=1, pady=(10, 10), padx=(10, 20))
        number_entry.grid(column=1, row=1, pady=(10, 15), padx=(20, 10))

        okay.grid(column=0, row=2, pady=(10, 0), padx=(10, 10))
        close_window_button.grid(column=1, row=2, pady=(10, 0), padx=(10, 10))

        # Display the window
        self.window.mainloop()

    def button_action_function(self):
        """
        Class function to call the submitted_input function with arguments in
        order to avoid a circular import
        :return: void
        """
        gigo.submitted_input(self.hashtag_variable, self.number_variable, self.window)

        # Open new window and show map photo
        newWindow = t.Toplevel(self.window)
        newWindow.title("Map")
        newWindow.geometry("1000x1000")
        background_image = t.PhotoImage(file="map.png")
        background_label = t.Label(newWindow, image=background_image)
        background_label.place(x=0, y=0)
        newWindow.mainloop()

    def close_window(self):
        """
        Class function to close the window after the user is done searching
        :return: void
        """
        self.window.destroy()
