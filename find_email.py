#!/bin/usr/python3
import re

def find_emails(rC=[]):
    reForm = re.compile(r'[\w\.-]+@[\w\.-]+')
    try:
        emails = reForm.findall(rC)   #rC - replaced content
        return list(set(emails))
    except:
        return []

some_text = "some@mail.com and other@thing.pl"

emails = find_emails(some_text)
print(emails)
