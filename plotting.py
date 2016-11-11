import matplotlib.pyplot as plt


def plot_opt(axis, headers):
    plot_choice_x = ""
    while plot_choice_x not in headers:
        print("\nChose the variable for your %s axis" %axis)
        plot_choice_x = input()
        plot_choice_x = plot_choice_x.lower()
        if plot_choice_x in headers:
            return plot_choice_x
        else:
            print("\nA valid selection was not made")


def set_variables(var_selection,training_set):
    try_dict = {"sepal length" : 0, "sepal width" : 1, "petal length" : 2, "petal width" : 3}
    
    ind = try_dict[var_selection]
    variable = [row[ind] for row in training_set]

    return variable

def set_plot_colours(training_set):
    colours = []
    for x in range(len(training_set)):
        if (training_set[x][4]).lower() == "iris-setosa":
            colours.append("blue")
        elif (training_set[x][4]).lower() == "iris-versicolor":
            colours.append("red")
        elif (training_set[x][4]).lower() == "iris-virginica":
            colours.append("green")
    return colours

def plot_graph(x1,y1,x_var,y_var,colours):
    plt.scatter( x = x1, y =y1, color = colours)

    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.show() 
