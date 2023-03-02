# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list,start_index,end_index):
    newlist = []
    for index in range(start_index,end_index):
        newlist.append(input_list[index])
    return newlist

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def subset(input_list,step_size):
    newlist = []
    for index in range(0,len(input_list),step_size):
        newlist.append(input_list[index])
    return newlist

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    return len(input_list)==len(set(input_list))

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    flattened = []
    for sublist in input_list:
        for item in sublist:
            flattened.append(item)
    return flattened


# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    merged = []
    for lst in args:
        merged.extend(lst)
    return merged

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    reversed_lst = []
    for t in input_list:
        reversed_lst.append(tuple(reversed(t)))
    return reversed_lst
    #return [tuple(reversed(t)) for t in input_list]

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list):
    return set(input_list)

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    transposed_matrix = []
    for i in range(len(input_list[0])):
        new_row = []
        for j in range(len(input_list)):
            new_row.append(input_list[j][i])
        transposed_matrix.append(new_row)
    return transposed_matrix

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list,chunk_size):
    result = []
    sublist = []
    for item in input_list:
        sublist.append(item)
        if len(sublist) == chunk_size:
            result.append(sublist)
            sublist = []
    if sublist:
        result.append(sublist)
    return result

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    new_dict={}
    for item in dict:
        new_dict.update(item)
    return new_dict
    

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    new_dict = {}
    evenls=[]
    oddls=[]
    for n in input_list:
        if n % 2 == 0:
            evenls.append(n)
        else:
            oddls.append(n)
    new_dict["even"]=evenls
    new_dict["odd"]=oddls
    return new_dict

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        mean_value = sum(value) / len(value)
        result_dict[key] = mean_value
    return result_dict


# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


