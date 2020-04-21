import nltk
import os
from nltk.stem.lancaster import LancasterStemmer    
import numpy
import tflearn
import tensorflow
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

try:
    with open("data.pickle","rb") as f:
        words, labels, training, output = pickle.load(f)  
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

    words = [stemmer.stem(w.lower()) for w in words if w != "?"] #get root word
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

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)
    with open("data.pickle","wb") as f:
        pickle.dump((words, labels, training, output),f)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model = tflearn.DNN(net)
    model.fit(training,output,n_epoch=1000,batch_size=8,show_metric=True)
    model.save("model.tflearn")
def bag_of_words(s,words):
    bag=[0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i,w in enumerate(words):
            if w==se:
                bag[i]=1
    
    return numpy.array(bag)

clear()

def chat():
    print("You can now start talking with the chatbot!\nType quit to stop")
    while True:
        inp = input("\nInput: ")
        if inp.lower() == "quit":
            clear()
            break
        results = model.predict([bag_of_words(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        if results[results_index] >0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            print(random.choice(responses))
        else:
            print("I did not understand. Please try to ask another question.") 
chat()
