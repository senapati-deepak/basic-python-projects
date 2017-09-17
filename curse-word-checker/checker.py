import urllib

def read_text():
    q = open("/home/deepak/Documents/basic-python-projects/curse-word-checker/sample.txt")
    text=q.read()
    check(text)
    q.close()

def check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print("ALERT!! Document has curse words")
    elif 'false' in output:
        print("No curse words in the document")
    else:
        print("not processed properly")
    
    
read_text()
