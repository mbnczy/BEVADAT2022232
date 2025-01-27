# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def contains_odd(input_list):
    index=0
    while(index<len(input_list) and input_list[index]%2==0):
        index+=1
    if index<len(input_list):
        return True
    else:
        return False
# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
    boollist = []
    for number in input_list:
       if number % 2!=0:
           boollist.append(True)
       else:
           boollist.append(False) 
    return boollist
# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list_1, input_list_2):
    newlist = []
    for a,b in zip(input_list_1,input_list_2):
        newlist.append(a + b)
    return newlist
# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict):
    return list(input_dict.items())

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


