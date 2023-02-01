"""
Create a python script called googlesearch that provides a command line utility to perform google search.
It gives you the top links (search results) of whatever you want to search on google.
"""

import tkinter as tk
import webbrowser
import requests
from bs4 import BeautifulSoup

def search(links=None):
    query = entry.get()

    print(query)

    # send GET request to Google
    r = requests.get(f'https://www.google.com/search?q={query}')

    print(r.status_code)

    print(links)

    # parse the response and extract the top links
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.select('.r a')

    # open the top links in new tabs
    for link in links:
        webbrowser.open(link['href'])

    label['text'] = 'Done!'

# create the GUI
root = tk.Tk()
root.title('Google')

# create the search field
entry = tk.Entry(root, width=50)
entry.pack(padx=5, pady=5)

# create the search button
button = tk.Button(root, text='Search', command=search)
button.pack(padx=5, pady=5)

# create the status label
label = tk.Label(root, text='')
label.pack(padx=5, pady=5)

# start the GUI loop
root.mainloop()

