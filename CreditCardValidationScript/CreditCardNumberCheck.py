#!/usr/bin/env python3.6

#purpose: Evaluate given set of credit card numbers valid or invalid

import re

def isCreditNumberValid(ccn):
    if(ccn.count("-") > 0):
        sublist_ccn = ccn.split("-")
        statusCode= 1
        if(len(sublist_ccn) != 4):
            statusCode=None
            sublist_ccn=[]
        for item in sublist_ccn:
            if len(item) != 4:
                statusCode=None
                break
    else:
        statusCode= re.search("[456][0-9]{15}",ccn)

    ccn=ccn.replace("-","")
    statusCode2= re.search(".*([0-9])\\1{3}.*",ccn)

    return statusCode, statusCode2

for i in range(0, int(input())):
    creditNumber = input()
    statusCode, statusCode2 = isCreditNumberValid(creditNumber)
    if statusCode!=None and statusCode2==None:
        print("Valid")
    else:
        print("Invalid")
