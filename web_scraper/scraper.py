import requests
from bs4 import BeautifulSoup

domain='https://en.wikipedia.org'
history_of_mexico= f'{domain}/wiki/History_of_Mexico'




def get_citations_needed_count(url):
    '''
     Count function must be named get_citations_needed_count
     get_citations_needed takes in a url and returns an integer
    '''
    resp=requests.get(url)
    result=resp.text
    file=open('history_of_mexico.html','w')
    file.write(result)
    file.close()
    parsed=BeautifulSoup(result,'html.parser')
    cites=parsed.find_all('a', { "title" : "Wikipedia:Citation needed"})
   
    return cites


def get_citations_needed_report(url):
    resp=requests.get(url)
    result=resp.text
    parsed=BeautifulSoup(result,'html.parser')
    cites=parsed.find_all('a', { "title" : "Wikipedia:Citation needed"})
    paragraph_list=''
    for cite in cites:
        paragraph=cite.parent.parent.parent
        # print(str(cite.parent.parent.parent).split('<'))
        paragraph_list+=f'\n{paragraph.text}'
    return paragraph_list

print(get_citations_needed_report(history_of_mexico))
quit()