

## Feature Tasks and Requirements


Scrape a Wikipedia page and record which passages need citations.

E.g. History of Mexico has a few “citations needed”.

Your web scraper should report the number of citations needed.

Your web scraper should identify those cases AND include the relevant passage.

E.g. Citation needed for “lorem spam and impsum eggs”
Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes

[x]Count function must be named get_citations_needed_count
[x]get_citations_needed takes in a url and returns an integer
[x]Report function must be named get_citations_needed_report
[x]get_citations_needed_report takes in a url and returns a string
[x]the string should be formatted with each citation needed on own line, in order found.
