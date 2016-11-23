
#1 
my_list = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]

#1.a
my_list[4]

#1.b
my_list.append(55.2)

#1.c
my_list.pop(5)

#1.d
for i in my_list:
    if i > 45:
        print(i)

#2.a
import numpy

#2.b
np_array = numpy.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])

#2.c
numpy.mean(np_array)
numpy.std(np_array)


#2.d
comprehension = [round(x,3) for x in np_array if x <= 45]


#2.e
numpy.max(np_array)
numpy.min(np_array)

#3.a
import pandas

#3.b
iris = pandas.read_csv("Iris.csv")

#3.c
iris.head()

#3.d
iris = iris.drop('Id', 1)
#confirm change
iris.head()

#3.e
head(iris.loc[(iris.Species == 'Iris-setosa')])

#3.f
iris.describe()

#3.g
head(iris.groupby(iris['Species']))