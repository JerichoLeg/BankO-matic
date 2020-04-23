import unittest
import os
from Chatbot import preProcessing, createModel, bag_of_words, chat
import pickle

process = preProcessing()
model = createModel(process.getTraining(),process.getOutput())

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

clear()

with open("data.pickle","rb") as f:
    words, labels, training, output = pickle.load(f)


class TestChatBot(unittest.TestCase):
    def test_Training(self):
        self.assertTrue((process.getTraining()==training).all())
    
    def test_Words(self):
        self.assertEqual(process.getWords(),words)
    
    def test_Output(self):
        self.assertTrue((process.getOutput()==output).all())
    
    def test_Data(self):
        self.assertIsNotNone(process.getData())

    def test_Labels(self):
        self.assertEqual(process.getLabels(),labels)
        
    def test_Model(self):
        self.assertIsNotNone(model.getModel())
    
    def test_chat(self):
        self.assertIsNone(chat())
    
    def test_BagOfWords(self):
        self.assertIsNotNone(bag_of_words("Random set of words here",process.getWords()))

if __name__ == '__main__':
    unittest.main()