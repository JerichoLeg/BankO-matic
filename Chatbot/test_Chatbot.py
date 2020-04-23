import unittest
import os
from Chatbot import preProcessing, createModel, bag_of_words, botChat
import pickle

process = preProcessing()
model = createModel(process.getTraining(),process.getOutput())
start = botChat()

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
    
    def test_BagOfWords(self):
        self.assertIsNotNone(bag_of_words("Random set of words here",process.getWords()))
    
    def test_botChat1(self):
        self.assertEqual(start.chat("What time do you open?"), "Opening and closing times depend on the branch")
    
    def test_botChat2(self):
        self.assertEqual(start.chat("Where are you located?"), "Visit our location finding feature for more information")
        
    def test_botChat2(self):
        self.assertEqual(start.chat("AcCounts cReatIosn online please?"),"Once you have an account in the bank, you can register an account online")

if __name__ == '__main__':
    unittest.main()