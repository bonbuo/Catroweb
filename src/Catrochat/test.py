import sys

def my_function(user_query):
    return "Python received: " + user_query

if __name__ == "__main__":
    user_query = sys.argv[1]
    result = my_function(user_query)
    print(result)
