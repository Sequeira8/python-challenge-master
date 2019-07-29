'''
Implementing auto-complete feature using Trie data structure

The system is able to store sentences in a Trie structure where each char
represents a Node of the structure.

Also for a given input the system is able to give up to 8 suggestions
that complete the given input with the objective to help the user
This number can be higher or lower if we change its value in
the searchRec function.
'''

class TrieNode():
    '''Node for the Trie data Structure that
    represents a letter of one name'''

    def __init__(self):

        #Dictionary containing all the the next possible letters
        self.children = {}
        #Represents the last char of one name if it is True
        self.last = False



class Trie():
    '''Trie data structure that will store all the names of the apps'''

    def __init__(self):

        self.root = TrieNode()

        #Used to store all the possibilities that we should present to the user
        #for the given input
        self.names_list = []



    def insert(self, name):
        '''Inserts one word into the structure'''

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
        '''Uses function "insert" to insert a list of names into the structure
        The list is sorted and the names are lower case'''

        for name in sorted(names, key=str.lower):
            self.insert(name.lower())



    def searchRec(self, node, name):
        '''Appends the possibilities to the names_list'''

        #Gives just a list of 8 name sugestions to the user
        if len(self.names_list) == 8:
            return

        #If it is the last char possible add the name to the list
        if node.last:
            self.names_list.append(name)

        #Get the letter and node to call the function
        #again with all the new possible words
        for letter,node in node.children.items():
            self.searchRec(node, name+letter)


    def search(self, input):
        '''Returns all the names in the trie that start with the given input'''

        #Reset the list with the possible names
        self.names_list = []

        node = self.root

        #Represents a flag that will only be False when there are no names
        #for the given input
        found = True

        #String with the name that will be added to the names_list
        name = ''

        #First search if the input fits the Trie (always looks for lower case)
        for letter in list(input.lower()):
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
