from pycricbuzz import Cricbuzz
import json
import cricgui
# now start by sudo pip install pycrickbuzz
def get_scores():
    output = []
    c = Cricbuzz()
    matches = c.matches()

    for match in matches:
        l=[]
        if (match['mchstate'] == 'inprogress') or (match['mchstate'] == 'stump') or (match['mchstate'] == 'lunch'):
            a = c.livescore(match['id'])
            #print c.commentary(match['id'])
            #print c.scorecard(match['id'])
            b = a["batting"]
            m = a["matchinfo"]
            j = b["score"]
            k = j[0]
            l.append(m["mchdesc"])  #instead print add it to a list
            l.append(b["team"]+":- "+k["runs"]+"/"+k["wickets"])
            l.append("Overs: "+k["overs"])
            output.append(l)
    cricgui.display_score(len(output),output)
    return True
