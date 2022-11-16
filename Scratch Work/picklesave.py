import pickle

if __name__ == '__main__':
    import seaborn as sns


def test_function():
    data = sns.load_dataset("iris")
    
class MyTestClass:
    a_number = 35
    a_string = 'hey'
    a_list = [1,2,3]

print('salad')

if __name__ == "__main__":

    my_object = MyTestClass()

    with open('test.pkl', 'wb') as file:
        pickle.dump(my_object, file)
