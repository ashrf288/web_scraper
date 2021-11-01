import requests
from bs4 import BeautifulSoup

domain='https://en.wikipedia.org'
history_of_mexico= f'{domain}/wiki/History_of_Mexico'




def get_citations_needed_count(url):
    '''
     
     get_citations_needed takes in a url and returns an integer
    '''
    resp=requests.get(url)
    result=resp.text
    file=open('history_of_mexico.html','w')
    file.write(result)
    file.close()
    parsed=BeautifulSoup(result,'html.parser')
    cites=parsed.find_all('a', { "title" : "Wikipedia:Citation needed"})
   
    return len(cites)


def get_citations_needed_report(url):
    resp=requests.get(url)
    result=resp.text
    parsed=BeautifulSoup(result,'html.parser')
    cites=parsed.find_all('a', { "title" : "Wikipedia:Citation needed"})
    paragraph_list=''
    for cite in cites:
        paragraph=cite.parent.parent.parent
        paragraph_list+=f'{paragraph.text}\n'
    return paragraph_list

# print(get_citations_needed_count(history_of_mexico))
# print(get_citations_needed_report(history_of_mexico))
