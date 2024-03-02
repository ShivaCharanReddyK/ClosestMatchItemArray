# Closest Match Program

This program is written in Python and uses the `streamlit`, `spacy`, `sklearn`, and `numpy` libraries. It is designed to find the closest match to a user's input string from a predefined list of array items.

## Prerequisites

Before running this program, you need to have Python installed on your system. You also need to install the following Python libraries:

- streamlit
- spacy
- sklearn
- numpy

You can install these libraries using pip:

```bash
pip install streamlit spacy sklearn numpy
```

Also, you need to download the `en_core_web_lg` model for `spacy`:

```bash
python -m spacy download en_core_web_lg
```

OR (to install libraries at a time)

Just Clone or download the Repo 

and use 
```bash
pip install -r requirements.txt
```

## How to Run the Program

To run the program, navigate to the directory containing the `main.py` file in your terminal and type:

```bash
streamlit run main.py
```

This will start the Streamlit server and open the application in your default web browser.

## How to Use the Program

Once the Streamlit application is running:

1. You will see a text input field labeled 'Enter a String:'.
2. Enter a string into this field.
3. The program will find the closest match to your input from the predefined list of array items.
4. The closest match will be displayed on the screen.

The program uses the cosine similarity between the vector representation of the user's input and the vector representations of the country names to find the closest match. The vector representations are generated using the `spacy` library's `en_core_web_lg` model.
