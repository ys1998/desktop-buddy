import news2
import weather_api
import cricscore
def Searcher(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False
def Searcher_h(l1,l2):
    m=0
    for i in l1:
        for j in l2:
            m=m+1
            if i==j:
                return m
        m=0
    return
newslist=["news","info"]
weatherlist=["climate","weather","raining","cloudy","rain","sunny","chilly","hot","dry","temperature","humidity","pressure"]
scoreslist=["score","scores"]
preplist=["in","at","on","over","of","above"]
def UniversalParser(str):
    User_input=str.lower()
    User_list=User_input.split()
    if Searcher(weatherlist,User_list):
        return weather_api.get_weather(''.join(User_list[Searcher_h(preplist,User_list):]))
    if Searcher(scoreslist,User_list):
        return cricscore.get_scores()
    if Searcher(newslist,User_list):
        return getnews(User_input)
    else:
        return False
def getnews(str):
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
    ["aus","australia","aussies"],
    ["uk","britain","kingdom","england","british",],
    ["us","usa","states","america","american"]]
    key=[]
    for i in Database:
        if Searcher(i,User_list):
            key.append(i[0])
    if len(key)!=0:
        output=[]
        for i in key:
            output.append(news2.main(i))
        return output
    else:
        return news2.main("general")