import pickle
print(f'pickle version: {pickle.format_version}')

from picklesave import MyTestClass
# import picklesave

with open('test.pkl', 'rb') as file:
    loaded_pickle = pickle.load(file)
