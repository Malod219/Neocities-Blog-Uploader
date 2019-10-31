import neocities
from feedgen.feed import FeedGenerator
import os, os.path
from html.parser import HTMLParser

f = open("config.cfg","r")
configs = f.readlines()
f.close()

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

textFileLocation = configs[2][18:-1:]
outputFolderLocation= configs[3][20:-1:]
blogPostHeaderLocation = configs[4][17:-1:]
blogPostTailLocation = configs[5][17:-1:]
blogHubEmpty = configs[6][13:-1:]
blogActualLocation = configs[7][19:-1:]

fg = FeedGenerator()
fg.id(configs[10][7:-1:])
fg.title(configs[11][10:-1:])
fg.author( {'name':configs[12][15:-1:],'email':configs[13][16:-1:]} )
fg.link( href=configs[14][9:-1:], rel='alternate' )
fg.subtitle(configs[15][13:-1:])
fg.link( href=configs[16][10:-1:], rel='self' )
fg.language(configs[17][9:-1:])

nc = neocities.NeoCities(configs[26][9:-1:],configs[27][9:-1:])

numberOfFiles = len([name for name in os.listdir(textFileLocation)])
newLinkTable = []

# Compile all the blog posts

for i in range(0,numberOfFiles):
    nameOfFile=str(i+1)+".txt"
    nameOfOutputFile=str(i+1)+".html"
    f = open(blogPostHeaderLocation,"r")
    head = f.readlines()
    f.close()

    f = open(blogPostTailLocation,"r")
    tail = f.readlines()
    f.close()
    
    f = open(textFileLocation+nameOfFile,"r")
    middle = f.readlines()
    f.close()
    
    newLinkTable.append((nameOfOutputFile,middle[0]))
    #print(middle)
    
    newString=""
    textString=""
    
    for line in head:
        newString+=line
    for line in middle:
        newString+=line
        textString+=line
    for line in tail:
        newString+=line
    fe = fg.add_entry()
    fe.id(configs[21][11:-1:]+str(i))
    fe.title(strip_tags(middle[0]))
    fe.description(strip_tags(textString))
    fe.link(href = configs[21][11:-1:]+str(i))
    
    
    f = open(outputFolderLocation+nameOfOutputFile,"w+")
    f.write(newString)
    f.close()
    nc.upload((outputFolderLocation+nameOfOutputFile,"blogs/"+nameOfOutputFile))

# Compile the hub link to all blog posts

f = open(blogHubEmpty,"r")
text=f.read()
f.close()

linksToAdd=""

newLinkTable.reverse()

for i in newLinkTable:
    title = i[1].replace("<h1>","").replace("</h1>","")
    link = "<p><a href=blogs/"+i[0]+">"+title+"</a></p>"
    linksToAdd+=link

f = open(blogActualLocation,"w+")
f.write(text.replace("<!--PointInsertion-->",linksToAdd))
f.close()

fg.rss_file('test.rss')

nc.upload(("test.rss","blogs.rss"))

nc.upload((blogActualLocation,"blog.html"))
