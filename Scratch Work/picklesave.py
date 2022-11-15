import pickle

class MyTestClass:
    a_number = 35
    a_string = 'hey'
    a_list = [1,2,3]

my_object = MyTestClass()

with open('test.pkl', 'wb') as file:
    pickle.dump(my_object, file)
