from flask import Flask, request, jsonify, render_template
from wtforms import TextField, Form
import autocomplete

app = Flask(__name__)
app.config["DEBUG"] = True

#Create a Trie With the Given input
t = autocomplete.Trie()

#Form for the user Input
class SearchForm(Form):
    input = TextField('Name:')


@app.route('/', methods=['GET', 'POST'])
def mainPage():
    #Creates one form
    form = SearchForm(request.form)

    #Searches for appsearch.html in the templates folder and renders it
    #Also the form we created is sent
    return render_template("appsearch.html", title='App Search', form=form)


#Error page in case the user tries to acess an undefined path
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
