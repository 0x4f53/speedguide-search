import os

def substringAfter(text, substring): return text.split(substring, 1)[-1]

def save_data(data, file_name):
    directory = "."
    if not os.path.exists(directory): 
        os.mkdir(directory)
        print (f"Created a cache directory at: {os.path.abspath(directory)}")
    
    return True
    