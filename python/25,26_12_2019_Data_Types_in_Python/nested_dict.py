# print all values from the dictionary
data = {'x': {'y': {'z': "1Rivet"},
           'm': "css",
           'l': {'A': "Valsad"}
           }}

t = type(data)
def function_check(dict1):
    for i in dict1.values():
        if type(i) == t:
            function_check(i)
        else:
            print(i)

function_check(data)


# Alternative way

# def function_check(dict1):
#     for i in dict1.values():
#         if isinstance(i,dict):
#             function_check(i)
#         else:
#             print(i)
#
# function_check(data)


