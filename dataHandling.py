import math
import operator

#set similarity measure, euclidian distance between to data points                    
def dist(point_1, point_2, length):
    distance = 0
    for x in range(length):
        distance += (point_1[x] - point_2[x]) ** 2
    return math.sqrt(distance)
    
#sample point compared to all training points, then ordered to find closest    
def find_neighbours(training_set, test_point, n):
    distances = []
    length = len(test_point) -1
    for x in range(len(training_set)):
       separation = (dist(training_set[x], test_point, length))
       distances.append((training_set[x], separation))
    distances.sort(key=operator.itemgetter(1)) # order the list
    neighbours = []
    for x in range(n):
        neighbours.append(distances[x][0])
    return neighbours
    

#use closest point to define relevant categories      
def set_categories(neighbours):
    index = 0
    categories = []
    for x in range(len(neighbours)):
      if(x == 0):
           categories.append(neighbours[x][4])
      elif(neighbours[x][4] != categories[index]):
           categories.append(neighbours[x][4])
           index += 1
    return categories
         
        
        
def prediction(neighbours, categories):
    votes = []
    for x in range(len(categories)):
        votes.append((neighbours.count(categories[x]), categories[x]))
    votes.sort(key=operator.itemgetter(1), reverse = False)
    return str(votes[0][1])
    
def get_accuracy(training_set, test_set,n):
    neighbours = []; categories = [];
    count = 0
    for x in range(len(test_set)):
        neighbours = find_neighbours(training_set, test_set[x],n)
        categories = set_categories(neighbours)
        result = prediction(neighbours,categories)
        if str(result) == str(test_set[x][4]):
            count += 1    
    
    return float(count/len(test_set))    

def test_opt():
    test_choice = 0
    while test_choice not in [1,2]:
        test_choice = input("would you like to test an individual case(1) or the accuracy(2)? \n")
        if test_choice == '1' or test_choice == '2':
            return test_choice
        else:
            print("\n A valid selection was not made")
