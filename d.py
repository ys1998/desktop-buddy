import g
def Searcher(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False
def getNews(str):
    User_input=str.lower()
    User_list=User_input.split()
    Database=[["tech","technology","techno","technical","take","geek","geeky","gadgets","gadget"],
    ["sports","sport","sporting","spot","spots",],
    ["business","money","trade","trading","finance","financial","financing","market","marketing","stocks","stock"],
    ["football","soccer","sucker","foosball","liga","league"],
    ["cricket"],
    ["entertainment","celebs","celebrities"],
    ["gaming","games","game"],
    ["science","nature","scientific","natural"],
    ["aus","australia","aus","aussies"],
    ["uk","britain","kingdom","england","british",],
    ["usa","usa","states","america","american"]]
    key=[]
    for i in Database:
        if Searcher(i,User_list):
            key.append(i[0])
    #print key
    if len(key)!=0:
        for i in key:
            print i
            g.main(i)
    else:
        g.main("general")
