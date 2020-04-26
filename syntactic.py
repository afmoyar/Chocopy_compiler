import pickle
with open('token.list', 'rb') as token_file:
 
    # Step 3
    tokens = pickle.load(token_file)
 
    # After config_dictionary is read from file
