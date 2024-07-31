
#import nltk library for perform sentiment analysis
#import tkinter for creating GUI app.
import nltk
import tkinter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#importing all the methods an classes from the tkinter
from tkinter import *


#function for clearing the contents
#for all entry boxes and text area in GUI.

def clearALL():

    #deleting the content from the entry box
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    #whole content of text area is deleted
    textArea.delete(1.0, END)

#function to print sentiments of the sentence.
    def Analyse_sentiment():
        sentence = textArea.get("1.0", "end")

        #create a SentimentIntensityAnalyzer(class's) object.
        sid_obj=SentimentIntensityAnalyzer()

        #polarity_scores method of SentimentIntensityAnalyzer
        #object gives a sentiment dictionary.
        #which contains +ve(pos),-ve(neg), neu, and compound scores.

        sentiment_dict=sid_obj.polarity_scores(sentence)

        string = str(sentiment_dict['neg']*100)+ "%Negative"
        negativeField.insert(10, string)

        string = str(sentiment_dict['neu']*100)+ "%Neutral"
        neutralField.insert(10, string)

        string = str(sentiment_dict['pos']*100)+ "%Positive"
        neutralField.insert(10, string)


        # Analyzing sentiment as positive, negative and neutral

        if sentiment_dict['compound'] >= 0.05:
            string = "Positive"
        elif sentiment_dict['compound'] <= -0.05:
            string = "Negative"

        else:
            string = "Neutral"

            overallField.insert(10, string)
#End of code where we define how the sentiment of a
#statement is going to analyze and based on certian
#condition it provide a output in the form of
#Positive Negative Neutral

            #Driver Code
            #Now we going to create the Graphical Interface for the
            #above Sentiment Analyzer Code.

            if __name__ == "__main__":

                #Creating a GUI window
                gui= Tk()

                #Setting the background colour of GUI window
                gui.config(background= "sky blue")

                #Setting the name of tkinter GUI window
                gui.title("Sentimen Analyzer")

                #Setting the configuration of GUI window
                gui.geometry("500x400")

                #Creating a label: To enter the statement for which
                #you want to analyze the sentiment
                enterText=Label(gui, text= "Enter Your Sentence", bg = "sky blue")

                #Creating a text area for the root
                #with lucida 13 font for writing the content into it
                textArea = Text(gui,height=5, width = 25, font = "lucida 13")

                #Creating a Submit Button and place into the root window
                #when the user press the button, the command or
                #function affiliated to that button is executed

                check = Button(gui, text= "Check Sentiment", fg= "Black", bg= "White", command= detect_sentiment)

                #Creating a Negative : label
                negative = Label(gui, text= "Sentence was rated as :", bg = "light orange" )

                #Creating a Neutral : label
                neutral = Label(gui, text= "Sentence was rated as : ", bg = "light pink")

                #Creating a Positive : label
                positve = Label(gui, text= "Sentence was rates as :", bg = "light green")

                #Creating a Overall : label
                overall = Label(gui, text = "Sentence Overall Rated As", bg = "sky blue")

                #Creating a text entry box for negative
                negativeField =Entry(gui)

                #Creating a text entry box for neutral
                neutralField=Entry(gui)

                #Creating a text entry box for positive
                positiveField = Entry(gui)

                #Creating a text entry box for Overall rating
                overallField=Entry(gui)


                #Creating a Clear Button and place into the root window
                #when user press the button, the command or
                #function affiliated to that button is executed

                clear = Button(gui, text="CLear", fg= "Black", bg= "Blue", command = clearALL)

                #Creating a Exit Button and place into the root window
                #when user press the button, the command or
                #function affiliated to that button is executed

                Exit = Button(gui, text = "EXIT", fg="Black", bg="Red", command=exit)


                #Grid method is user for placing
                #the widgets at espective position
                #in table like structure.
                enterText.grid(row = 0, column =2)

                textArea.grid(row=1,column=2,padx=10,sticky=W)

                check.grid(row=2,column=2)

                negative.grid(row=3, column=2)

                neutral.grid(row=5,column=2)

                positive.grid(row =7, column =2)

                overall.grid(row =9,column= 2)

                negativeField.grid(row=4,column=2)

                neutralField.grid(row=6,column=2)

                postiveField.grid(row=8,column=2)

                overallField.grid(row=10, column=2)

                clear.grid(row=11,column=2)

                Exit.grid(row=12, column=2)


                #Starting the GUI
                gui.mainloop()




                
                
                
            
