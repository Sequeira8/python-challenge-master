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
