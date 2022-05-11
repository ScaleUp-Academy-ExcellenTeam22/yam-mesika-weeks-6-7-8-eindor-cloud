
#I Took this from the web
def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value

#Get a function and an iterable
#Return a dictionary of answers from the function
def group_by(func, iter):
    answers = dict()
    for item in iter:
        x = func(item)
        if x in answers.keys():
            append_value(answers, x, item)
        else:
            answers[x] = item
    return answers

print(group_by(len, ["hi", "bye", "yo", "try"]))