from flask import Flask, request, jsonify, render_template
from wtforms import TextField, Form
import autocomplete
import csv
import sys

app = Flask(__name__)
app.config["DEBUG"] = True

#Create a Trie With the Given input
t = autocomplete.Trie()

#Form for the user Input
class SearchForm(Form):
    input = TextField('Name:')


@app.route('/', methods=['GET', 'POST'])
def mainPage():

    #List where the names in the input file will be stores
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
    #Receive input, searches for the possible names and returns a list of them

    #Gets the User Input
    input = request.form.get('input')

    #List of the possible names
    list = t.search(input)

    #Transforms list to the desired format to present to the user
    return jsonify({'data': render_template("namepossibilities.html", list=list)})


#Error page in case the user tries to acess an undefined path
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
