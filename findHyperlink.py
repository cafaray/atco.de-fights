def findHyperlink(text):
    for c in range(len(text)):
        if text[c]=='<' and text[c+1]=='a':
            href = ''
            c+=1
            url=''        
            while href!='href=':
                if c>=len(text):
                    return "none"
                if text[c] in 'href=':
                    href+=text[c]
                c+=1
            if href=='href=':
                print(text[c-5:])
                sep = text[c]
                c+=1
                while sep!=text[c]:
                    if c>=len(text):
                        return "none"
                    url+=text[c]
                    c+=1
                return url
            else:
                print("no href")
    return "doamin"

print(findHyperlink("<a href=\"http://www.example.org\">Example1</a>"))
print(findHyperlink("a href=\"http://www.wrong.org\"<a href=\"correct\">Example2 a href /a</a> URL"))
print(findHyperlink("URL a href=\"http://www.wrong.org\"<a href=\"\">Example3 a href /a</a> URL href"))