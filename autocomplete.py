# Implementing auto-complete using Trie data structure

class TrieNode():

    def __init__(self):
        #Initialize one Node for the Trie data Structure
        #that will represent a letter of the name

        #Dictionary containing all the the next possible letters
        self.children = {}
        #Represents the last char of one name if it is True
        self.last = False



class Trie():

    def __init__(self):
        #Initialize one Trie that will store all the names

        self.root = TrieNode()

        #Used to store all the possibilities that we should present to the user
        #for the given input
        self.names_list = []



    def insert(self, name):
        #Inserts one word into the structure

        node = self.root

        for letter in list(name):

            #Find out if the letter is already in the dictionary, if not
            #we add it as a children of the current letter
            if not node.children.get(letter):
                node.children[letter] = TrieNode()

            #Switch to the children to continue the insert
            node = node.children[letter]

        #At the end we represent this node as the last onde
        node.last = True



    def insertNames(self, names):
        #Uses function "insert" to insert a list of names

        for name in names:
            self.insert(name)



    def searchRec(self, node, name):
        #Appends the possibilities to the names_list

        #If it is the last char possible add the name to the list
        if node.last:
            self.names_list.append(name)

        #Get the letter and node to call the function
        #again with all the new possible words
        for letter,node in node.children.items():
            self.searchRec(node, name+letter)


    def search(self, input):
        #Returns all the names in the trie that start with the given input

        #Reset the list with the possible names
        self.names_list = []

        node = self.root

        #Represents a flag that will only be False when there are no names
        #for the given input
        found = True

        #String with the name that will be added to the names_list
        name = ''

        #First search if the input fits the Trie
        for letter in list(input):
            if not node.children.get(letter):
                found = False
                break

            name += letter

            #Switch to the next node to continue searching
            node = node.children[letter]


        #No possibilities
        if not found:
            return []

        #The only name possible is already the one represented in the input
        elif node.last and not node.children:
            self.names_list.append(name)
            return self.names_list

        #More than one possibilities
        self.searchRec(node, name)

        return self.names_list
