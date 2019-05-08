import xml.etree.ElementTree as ET 

def xmlTags(xml):
    root = ET.fromstring(xml)
    print(root.tag)
    print(root.attrib)
    for child in root:
        print("\t", child.tag, child.attrib)
        try:
            for subchild in child:
                print("\t\t", subchild.tag, subchild.attrib)
        except:
            pass
    

xml = '<products><product><TITLE> product #1 </TITLE><PRICE> 10.00 </PRICE></product><product><TITLE> product #2 </TITLE><PRICE> 20.00 </PRICE></product></products>'
outter = ["data()", 
 "--animal(name)", 
 "----genus()", 
 "----family(member, name, subfamily)", 
 "----similar(name, size)", 
 "----order()"]
print("Assertion Test 1: ", xmlTags(xml) == outter)

xml = '<data> <animal name="cat"><genus>Felis</genus><family name="Felidae" subfamily="Felinae"/><similar name="tiger" size="bigger"/></animal><animal name="dog"><family name="Canidae" member="canid"/><order>Carnivora</order><similar name="fox" size="similar"/></animal></data>'
outter = ["products()", 
 "--product()", 
 "----TITLE()", 
 "----PRICE()"]
print("Assertion Test 2: ", xmlTags(xml) == outter)

xml = '<here urlid=\"blah-blah\"><component type=\"Documents\" context=\"User\"><displayName>My Video</displayName><role role=\"Data\"><detects><detect><condition>Helper.hasObject</condition></detect></detects><rules><include filter=\"Helper.IgnoreIrrelevantLinks\"><objectSet><pattern type=\"File\"></pattern></objectSet></include></rules></role></component></here>'
outter = ["here(urlid)", 
 "--component(context, type)", 
 "----displayName()", 
 "----role(role)", 
 "------detects()", 
 "--------detect()", 
 "----------condition()", 
 "------rules()", 
 "--------include(filter)", 
 "----------objectSet()", 
 "------------pattern(type)"]
print("Assertion Test 3: ", xmlTags(xml) == outter)

xml = "<a></a>"    
["a()"]
print("Assertion Test 4: ", xmlTags(xml) == outter)

xml = '<PHONEBOOK><PERSON><NAME>Joe Wang</NAME><EMAIL>joe@yourserver.com</EMAIL><TELEPHONE>202-999-9999</TELEPHONE><WEB>www.java2s.com</WEB></PERSON><PERSON><NAME>Karol</NAME><EMAIL>karol@yourserver.com</EMAIL><TELEPHONE>306-999-9999</TELEPHONE><WEB>www.java2s.com</WEB></PERSON><PERSON><NAME>Green</NAME><EMAIL>green@yourserver.com</EMAIL><TELEPHONE>202-414-9999</TELEPHONE><WEB>www.java2s.com</WEB></PERSON></PHONEBOOK>'
outter = ["PHONEBOOK()", 
 "--PERSON()", 
 "----NAME()", 
 "----EMAIL()", 
 "----TELEPHONE()", 
 "----WEB()"]
print("Assertion Test 5: ", xmlTags(xml) == outter)

xml = '<outer attr1=\"lol hello\" attr2=\"pal how are you\">hello</outer>'
outter = ["outer(attr1, attr2)"]
print("Assertion Test 6: ", xmlTags(xml) == outter)
