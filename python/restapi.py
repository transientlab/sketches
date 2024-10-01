#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'getAuthorHistory' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
#
# Base urls:
#   https://jsonmock.hackerrank.com/api/article_users?username=
#   https://jsonmock.hackerrank.com/api/articles?author=
#

def getAuthorHistory(author):
    # Write your code here
    history = []
    req_url = "https://jsonmock.hackerrank.com/api/article_users?username=" + author
    res_data = requests.get(req_url).json()['data'][0]['about']
    if res_data not in ['', None]:
        print(res_data)
    req_url = "https://jsonmock.hackerrank.com/api/articles?author=" + author
    res_data = requests.get(req_url).json()['data']
    for record in res_data:
        print(record['title'])    

    
    return history
    
    
if __name__ == '__main__':
    fptr = open('outfile', 'w+')

    author = 'epaga'

    result = getAuthorHistory(author)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
