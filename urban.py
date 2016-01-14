from pyquery import PyQuery as pq

def lookup(word):
    url_template = "http://www.urbandictionary.com/define.php?term=%s"
    d = pq(url=url_template % word)
    meaning = d("div.meaning:first").text()
    example = d("div.example:first").text()

    return meaning, example
