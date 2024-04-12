import sys
from catrochat_simple import CatrochatSimple as Cc_simple

if __name__ == "__main__":
    catrochat_version = Cc_simple()
    user_query = sys.argv[1]
    return catrochat_version.answer_user(user_query)