import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_locations_names():
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    global __data_columns
    global __model

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts(): # load
    print("Loading the saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns'] # converting objects to dictionary
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f: # pickle is a binary - rb
        __model = pickle.load(f)

    print("Loading saved artifacts is done")





if __name__ == '__main__':
    load_saved_artifacts() # runs only when util.py is called directly
    print(get_locations_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other
    print(get_estimated_price('Ejipura', 1000, 2, 2)) # other