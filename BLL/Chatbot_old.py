import nltk
import os
from nltk.stem.lancaster import LancasterStemmer    
import numpy
import tflearn
import tensorflow as tf
import random
import json
import pickle

stemmer = LancasterStemmer()

#Clear function
if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

data = json.load(open("intents.json")) #Open intents.json file

#start of pre processing
try:
    with open("data.pickle","rb") as f:
        words, labels, training, output = pickle.load(f) #try to import data if there is a file available
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []
    
    for intent in data["intents"]: #loop through intents
        for pattern in intent["patterns"]: #loop through patterns
            wrds = nltk.word_tokenize(pattern) #break text into individiual words
            words.extend(wrds) #wrds list is added to words
            docs_x.append(wrds)
            docs_y.append(intent["tag"])
            
        if intent["tag"] not in labels:#add label if label in json file is not in label list
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"] #get root word, does not get question mark
    words = sorted(list(set(words))) #set makes sure that there are no duplicate words
                                     #list makes words back into list
                                     #sorted sorts the list
    labels = sorted(labels)

    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w) for w in doc]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:] #create a copy of out_empty
        output_row[labels.index(docs_y[x])] = 1 #look through labels, set value to 1 if located in labels

        training.append(bag) #append bag to training list
        output.append(output_row)

    training = numpy.array(training) #turn into numpy array
    output = numpy.array(output) #turn into numpy array
    with open("data.pickle","wb") as f:
        pickle.dump((words, labels, training, output),f) #write all data into a pickle file

#end of preprocessing

tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])]) #Find input shape for model
net = tflearn.fully_connected(net, 8) #8 neurons for hidden layer
net = tflearn.fully_connected(net, 8) #another 8 neurons for hidden layer
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax") #output layer, get probabilities for each output
net = tflearn.regression(net)

model = tflearn.DNN(net) #create model for training

try:
    model.load("model.tflearn") #load model if there is a file available (so that there is no need for retraining)
except:
    model = tflearn.DNN(net)
    model.fit(training,output,n_epoch=2000,batch_size=8,show_metric=True) #2000 iterations for learning
    model.save("model.tflearn") #save model for later use

def bag_of_words(s,words):
    bag=[0 for _ in range(len(words))] #blank bag of words list
    s_words = nltk.word_tokenize(s) #list of tokenized words
    s_words = [stemmer.stem(word.lower()) for word in s_words] #stem words from s_words list
    
    for se in s_words:
        for i,w in enumerate(words):
            if w==se:
                bag[i]=1 #change value of element in bag to 1 if word in words is equal to word in s_words
    
    return numpy.array(bag) #return a numpy array from bag

def chat():
    clear() #clear screen
    print("You can now talk with the chatbot!\nType exit to stop")
    while True:
        inp = input("\nInput: ")
        if inp.lower() == "exit":
            clear()
            break
        results = model.predict([bag_of_words(inp, words)])[0] #generates probability from input for each of the tags
        results_index = numpy.argmax(results) #finds the index of greatest value in the list
        tag = labels[results_index] #returns tag from the index given before
        
        if results[results_index] >0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses'] #get responses from tag
            print(random.choice(responses)) #display a random response from list
        else:
            print("I did not understand. Please try to ask another question.") #asks the user to ask another question if probability is less than 80% 
chat()