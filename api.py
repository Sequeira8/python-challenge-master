'''
API that receives a query and returns the possible results for that query
using the autocomplete system defined in the autocomplete.py file
'''

from flask import Flask, request, jsonify, render_template
from wtforms import TextField, Form
import autocomplete
import csv
import sys

app = Flask(__name__)
app.config["DEBUG"] = True

#Create a Trie data Structure
t = autocomplete.Trie()


class SearchForm(Form):
    '''Form for the user Input'''

    input = TextField('Name:')


@app.route('/', methods=['GET', 'POST'])
def mainPage():
    '''Gets the names in the input file and stores them in the autocomplete Trie
    Also creates a form that will be used in the rendered html file and where
    the user can write his input'''

    #List where the names in the input file will be stored
    titles = []

    #Open the input file and stores all the names in the titles list
    with open(sys.argv[1], newline='\n') as file:
        data = csv.reader(file)
        for row in data:
            titles.append(row[0])

    #Insert Names in the Trie Data Structure
    t.insertNames(titles)

    #Creates one form
    form = SearchForm(request.form)

    #Searches for appsearch.html in the templates folder and renders it
    #Also the form we created is sent
    return render_template("appsearch.html", title='App Search', form=form)


@app.route('/_possibilities', methods=['POST'])
def _possibilities():
    '''Receive input, searches for the possible names in the Trie
    and returns a list of them'''

    #Gets the User Input
    input = request.form.get('input')

    #List of the possible names
    list = t.search(input)

    #Transforms list to the desired format to present to the user
    return jsonify({'data': render_template("namepossibilities.html", list=list)})


@app.errorhandler(404)
def page_not_found(e):
    '''Error page in case the user tries to acess an undefined path'''

    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
