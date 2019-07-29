'''Tests for the autocomplete.py file'''

import unittest
import csv

import sys
sys.path.append("..")
import autocomplete

class TestAutoComplete(unittest.TestCase):
    '''Testing autocomplete system'''

    @classmethod
    def setUpClass(cls):
        '''Defines a trie with inserted names that can be used in all the tests'''

        cls.t = autocomplete.Trie()
        cls.titles = []

        with open('test_files/6500titles.csv', newline='\n') as file:
            data = csv.reader(file)
            for row in data:
                cls.titles.append(row[0])

        cls.t.insertNames(cls.titles)

    def test_insert(self):
        '''Testing one name inserts in the Trie Data Structure'''

        trie = autocomplete.Trie()

        #simple insert
        trie.insert('ola')
        self.assertEqual(trie.search(''),['ola'])

        #numbers
        trie.insert('123')
        self.assertEqual(trie.search('1'),['123'])

        #double insert
        trie.insert('ola')
        self.assertEqual(trie.search('o'),['ola'])

        #blank space
        trie.insert('blank space')
        self.assertEqual(trie.search('b'),['blank space'])


    def test_insertNames(self):
        '''Testing several name inserts in the Trie Data Structure'''

        trie = autocomplete.Trie()
        list = ['z','1','a','abc','FACEBOOK','zebras and lions']

        #simples insert and order check
        trie.insertNames(list)
        self.assertEqual(trie.search(''),['1','a','abc','facebook','z','zebras and lions'])

        #double insert
        trie.insertNames(list)
        self.assertEqual(trie.search(''),['1','a','abc','facebook','z','zebras and lions'])

        #capital letter check
        self.assertEqual(trie.search('FACEBOOK'),['facebook'])

        #black space
        self.assertEqual(trie.search('z'),['z','zebras and lions'])


    def test_search(self):
        '''Testing searches for names'''

        #Not found
        self.assertEqual(self.t.search('12345a'),[])

        #only one option
        self.assertEqual(self.t.search('facebook lite'),['facebook lite'])

        #capital letter check
        self.assertEqual(self.t.search('FACEBOOK LITE'),['facebook lite'])

        #empty input check
        self.assertEqual(self.t.search(''),['10 bullets','100 cells','100 doors','100 doors 2013','100 doors 2015','100 doors remix','100 efect selfie foto','100 pushups'])


if __name__ == '__main__':
    unittest.main()
