# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:39:42 2016

@author: DClarke2
"""
#imports
import dataHandling as dh #custom module
import dataLoad as dl #custom module
import plotting as grph #custom module
import random # standard module

############## Main Body ##############

#define lists
training_set = []
test_set = [] 
neighbours = []   
categories = []     

clear = "\n" * 10
print(clear)
            
dl.get_data("iris_flower.txt", 0.67, training_set, test_set)

#soup = dl.soup_set("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#dataset = dl.struct_soup(soup)
#dl.sort_sets(dataset, 0.67, training_set, test_set)

option = dh.test_opt()

if option == '1':
    test_id = random.randint(0,len(test_set))
    neighbours = dh.find_neighbours(training_set, test_set[test_id], 5)
    categories = dh.set_categories(neighbours) 
    predicted_cat = dh.prediction(neighbours,categories)
    print("test_id = " + str(test_id) + " is an " + predicted_cat)
elif option == '2':
    accuracy = float(dh.get_accuracy(training_set,test_set,5))
    print("Accuracy = " + '%.2f' %accuracy )
else:
    print("there has been a selection error")
    

######## End Body ###############


######### Plots #############
headers = ["sepal length", "sepal width", "petal length", "petal width"]

print("\nYou now have the option to view the data set as a scatter plot \n")
print("Reminder: The variables used were - \n")
print(headers)

x_var = grph.plot_opt("x",headers)
y_var = grph.plot_opt("y",headers)

x1 = grph.set_variables(x_var,training_set)
y1 = grph.set_variables(y_var,training_set)

colours = grph.set_plot_colours(training_set)

grph.plot_graph(x1,y1,x_var,y_var,colours)  
