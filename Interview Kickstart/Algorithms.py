print('hello world')
item_list = [5,2,9,8,10,1]

def selection_sort(list_of_items):
    for i in range(100):
        for val, idx in enumerate(item_list):
            if item_list[idx] > item_list[idx+1]:
                first_item = item_list[idx]
                second_item = item_list[idx+1]
                item_list[idx] = second_item
                item_list[idx+1] = first_item
    return item_list

sorted_list = selection_sort(item_list)
print(sorted_list)