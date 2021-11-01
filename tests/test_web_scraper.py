from web_scraper.scraper import (get_citations_needed_count,get_citations_needed_report)


file=open('data.txt','r')

def test_get_citations_needed_count():
     # input
    domain='https://en.wikipedia.org'
    history_of_mexico= f'{domain}/wiki/History_of_Mexico'
    #output
    expected=5
    actual=get_citations_needed_count(history_of_mexico)
    assert expected==actual







