# English-Dictionary-App

>This is an interactive English dictionary which will allow the user to type in words to get meaning 

### Python Dictionary Workflow

This particular project is going to be divided into two parts, for the first part we are going to develop a terminal based application and later we will move into developing an interactive GUI app.

The steps taken are:

- The first step, the JSON file will be loaded into python.
- Get user input
- Cross check the meaning of the word from the JSON file

## Creating Dictionary App

### Terminal SetUp

In order for us to create our interactive dictionary and use it in the terminal, we will need:

- dict.py file – which will contain our code.
- A data file – which is a JSON file that contains vocabularies that will be checked against giving meaning of words asked for.
- difflib – help us compare various sequences and give us a list of words which are close to what the user intended to search for. 

 Now that we have all the necessary files and modules we will need, let’s get started by developing our terminal based application.
 
The first step will be for us importing the libraries that we will be using, and that is done as shown below.

```
import json
from difflib import get_close_matches
```

Next we load up the JSON file.

```
data = json.loads(open('data.json').read())
``` 

At this point now we can go ahead and write our main function which will contain the code shown below. Just a simple breakdown of the main function is:

We have defined a function: definition.

Converted all user input into lowercase to match words in JSON file.

If statement to check if words given exist, suggest possible words, and return an error if word does not exist.

```
def definition(name):
    name = name.lower()
    if name in data:
        return data[name]
    elif len(get_close_matches(name, data.keys())) > 0:      
        check = input("Did you mean %s instead? Enter Y if yes, otherwise N to exit: " %
                      get_close_matches(name, data.keys())[0])
        if check == "Y":
            return data[get_close_matches(name, data.keys())[0]]
        elif check == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "Sorry, this word is not an English word. Please double check your spelling."
 ```
 
Next, we now pass in the method that will take in the user input and check it against the set of words passed in the  JSON file.

```
word = input('Enter a name: ')
```

The last step is to add an output format. We need to get our answers arranged in an easier manner to read, and in order to achieve that we make use of the if statement and for loop. Which will list all meanings in a separate line in the terminal.

To achieve that, we make use of the code below.

```
output = definition(word)
if type(output) == list:  
    for item in output:
        print(item)
else:
    print(output)
 ```
 
Now let’s go ahead and test out our program by running it on different instances.

If you check an English word, for example the word “program” the output will be as shown below.

![image](https://user-images.githubusercontent.com/64327691/194912082-d287327f-7c91-45ca-bdf4-5423d12faf3e.png)

From the above code output samples, we have been able to create an interactive dictionary operated from the terminal and we are able to get words meaning and also correctly tell if a word is misspelled or does not exist in the english dictionary.

Now let’s go ahead and create a GUI based dictionary.

## GUI based Dictionary 

In this particular section, we will do things a little bit differently. Since we will need an interface we will interact with we are going to use different modules compared to our terminal app.

In this case apart from having dict.py file, we are going to make use of:

- PyDictionary – A Python module that will help us get meanings, synonyms and antonyms of words.
- Tkinter – A python framework that will enable us to create GUI elements usings its widgets found in the Tk toolkit.

### Step 1: Installing the packages

To install PyDictionary, we will use the pip command on either the terminal or command prompt.
```
pip install PyDictionary
```

Similarly to install tkinter we make use of pip by executing the command below: 

```
pip install tk
```

### Step 2: Import the installed packages

In order for us to use the two modules that we have installed via the terminal, we will need to import them. The code below allows us to do this: 

```
from tkinter import *
from PyDictionary import PyDictionary
```

First, we import tkinter with all its related libraries, which we will use to create the interface. Next, we import PyDictionary, which will enable us to get meaning to words that we put in the search box.

### Step 3: Create instances for the packages

In order for us to make use of the two packages we need an instance. In PyDictionary the instance will take in words, while for tkinter it will initialize the tools for usability.

```
dictionary = PyDictionary()
root = Tk()
```

### Step 4: Set Window Dimensions & Title

When you use tkinter, it’s important to note that geometry determines the position and size of the screen. In our dictionary to set the size of our window we use the geometry() method.

In our code, we have set the window size to 600x400 and the position of the window to 50px from top and left of the screen. We have also added a title by use of the title() method.    

```
# set geometry
root.title("Dictionary")
root.geometry("600x400+50+50")
```

### Step 5: Define main function

Our function will help us to make use of other attributes of the PyDictionary class, such as getting the meaning, synonyms and antonyms of the issued words.
```
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))
```

### Step 6: Add Labels and Buttons

This particular step is where we get to design the interface of our dictionary, that is by setting the fonts, colors, text position etc…
```
# Add labels, buttons and frame
Label(root, text="My Dictionary", font=(
    "Poppins, 20 bold"), fg="Orange").pack(pady=20)
# Frame 1
frame = Frame(root)
Label(frame, text="Enter word: ", font=(
    "Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=30)
word.pack()
frame.pack(pady=10)
# Frame 2
frame1 = Frame(root)
Label(frame1, text="Meaning: ", font=("Aerial, 15 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Poppins, 15"))
meaning.pack()
frame1.pack(pady=10)
# Frame 3
frame2 = Frame(root)
Label(frame2, text="Synonym: ", font=(
    "Roboto, 15 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Roboto, 15"))
synonym.pack()
frame2.pack(pady=10)
# Frame 4
frame3 = Frame(root)
Label(frame3, text="Antonym: ", font=("Helvetica, 15 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetica, 15"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root, text="Search", font=("Helvetica, 15 bold"), command=dict).pack()
```

Now, we only have to do one more step. We just have to add the last piece of code that will execute the program.

### Step 7: Run the App

To execute the app we use the mainloop() method. What it does is, it tells Python to run the tkinter event loop until the user exits it. 
```
# Execute Tkinter
root.mainloop()
```

### Step 8: Output

Running the above code will create a display of our dictionary app that will look as shown below with everything set as defined in the code.

![image](https://user-images.githubusercontent.com/64327691/194912634-ab16cb82-1712-4ccd-8683-b868f46a1d14.png)

### Python dictionary example

Now, let’s get a sample output to be sure everything is working fine:

![image](https://user-images.githubusercontent.com/64327691/194912722-33a5b13d-55e9-4225-acd1-bfcb2844b791.png)


Python dictionary example execution

### Conclusion

Now you can create a Dictionary App using Python that can run through the terminal and an interactive GUI. There is no limitation on the design of the app. Therefore, you can redesign it to meet your own specification and style. You can even add other interactivity features to it. It’s about time you start using your own dictionary.
