from googlesearch import search
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import json
from academia.models import (
    ResourceCS,
    ResourceTh,
    ResourceDs,
    ResourceCe,
    ResourceAlg,
    ResourceAlg_Graphs,
    ResourceGraphs
)
# Fill Database for Computer Science
searchCS = "computer science"
search1 = SearchVideos(searchCS, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceCS(link=v['link'])
        res1.save()

# to search
query = "computer science"

links = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceCS(link=j)
    res1.save()

'''Fill Database for Computer Theory'''

searchCS = "theoretical computer science"
search1 = SearchVideos(searchCS, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceTh(link=v['link'])
        res1.save()

# to search
query = "theoretical computer science"

links = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceTh(link=j)
    res1.save()
# -------------------------------
searchCS = "data science"
search1 = SearchVideos(searchCS, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceDs(link=v['link'])
        res1.save()

# to search
query = "data science"

links = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceDs(link=j)
    res1.save()

# ----------------------------------
searchCS = "computer engineering"
search1 = SearchVideos(searchCS, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceCe(link=v['link'])
        res1.save()

# to search
query = "computer engineering"

links = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceCe(link=j)
    res1.save()

# -------------------------------
searchCS = "Algorithms"
search1 = SearchVideos(searchCS, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceAlg(link=v['link'])
        res1.save()

# to search
query = "computer science"

links = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceAlg(link=j)
    res1.save()

# --------------------------
searchGA = "Graphs in Algorithms"
search1 = SearchVideos(searchGA, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceAlg_Graphs(link=v['link'])
        res1.save()

# to search
queryGA = "Graphs in Algorithms"

links = []
for j in search(queryGA, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceAlg_Graphs(link=j)
    res1.save()

# ---------------------------
searchG = "What are graphs in computer science?"
search1 = SearchVideos(searchG, offset=1, mode="json", max_results=5)
obj = json.loads(search1.result())

urls = []
for key, value in obj.items():
    for v in value:
        res1 = ResourceGraphs(link=v['link'])
        res1.save()

# to search
queryG = "What are graphs in computer science?"

links = []
for j in search(queryG, tld="co.in", num=5, stop=5, pause=2):
    res1 = ResourceGraphs(link=j)
    res1.save()
