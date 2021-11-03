import requests
from bs4 import BeautifulSoup
domain='https://en.wikipedia.org'


def get_citations_needed_count(url):
    '''
     
     get_citations_needed takes in a url and returns an integer
    '''
    history_of_mexico= f'{domain}/wiki/History_of_Mexico'
    resp=requests.get(history_of_mexico)
    result=resp.text
    file=open('history_of_mexico.html','w')
    file.write(result)
    file.close()
    parsed=BeautifulSoup(result,'html.parser')
    cites=parsed.find_all('a', { "title" : "Wikipedia:Citation needed"})
   
    return len(cites)


def get_citations_needed_report(url):
    domain = url
    citation_url = f"{domain}/wiki/History_of_Mexico"
    res = requests.get(citation_url)
    html_text = res.text
    soup = BeautifulSoup(html_text, "html.parser")
    citation = soup.find_all('a', { "title" : "Wikipedia:Citation needed"})
    result_string=[]
    for c in citation:
        par=c.parent.parent.parent
        result_string+=[par.text] 
    return result_string    


# print(get_citations_needed_count(history_of_mexico))
# print(get_citations_needed_report(history_of_mexico))


