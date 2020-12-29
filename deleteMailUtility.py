# -*- coding: utf-8 -*-
"""
Spyder Editor

author - aditya gundawar
"""

import imaplib

# User Credentials
user =  ''
password = ''
imap_url  = 'imap.gmail.com'

def search(con, mailbox = 'INBOX', toDelete ):
    con.select(mailbox)
    # This search will return all the mails in the mailbox regardless of the 'inbox', 'social' and 'promotion'
    # tabs in GMail. 
    typ, data = con.search(None, 'ALL')
    for num in data[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        rawData = str(data[0][1])
        email = rawData[rawData.index('<'):rawData.index('>')][1:]
        dummify = [True if x in email else False for x in toDelete]
        if any(dummify):
            # This will add a delete tag to the mails.
            con.store(num, "+FLAGS", "\\Deleted")
            print(email)
    # this will delete all the mails with a delete tag attached to them.
    con.expunge()
        

if __name__ == '__main__':
    con  = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    # Use this list to enter all the emails you wish to delete
    # The function will search for these keywords in each email address
    keywordsToSearch = ['google','siriusxm','swiggy','zomato', 'facebook', 'pocket']
    search(con)
    con.close()
    con.logout()
    