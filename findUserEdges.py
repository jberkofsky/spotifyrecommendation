import sys
import spotipy
import spotipy.util as util
import os
import networkx as nx
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from networkx.algorithms.clique import find_cliques
from networkx.algorithms import community as cc

files = os.listdir("SpotifyLibraryDictionaries")
userGraph=nx.DiGraph()
for file in files:
    if file[0] == '.':
        continue
    with open("SpotifyLibraryDictionaries/" + file) as f:
        userDict={}
        for line in f:
            songlist= line.split(":")
            artistName=songlist[0]
            songName=songlist[1]
            userDict[artistName]=songName
        for OTHERfile in files:
            if file[0] == '.':
                continue
            elif OTHERfile==file:
                continue
            with open("SpotifyLibraryDictionaries/" + OTHERfile) as otherF:
                otherUserDict={}
                for otherline in otherF:
                    songlist= otherline.split(":")
                    artistName=songlist[0]
                    songName=songlist[1]
                    otherUserDict[artistName]=songName
                   # if otherUserDict[artistName] in userDict:
                   #     BothLike[artistName]=otherUserDict[artistName]
                   # elif artistName in userDict:
                    #    reccomender[artistName]=otherUserDict[artistName]
                        
            BothLike= set(userDict) & set(otherUserDict)
            if (len(BothLike)>190):
                userGraph.add_edge(file,OTHERfile, weight=len(BothLike))
                
            
# x=list(nx.find_cliques(userGraph.to_undirected()))
#for clique in x:
   #basically want to go through all and create a list of all artists they do not have in common --> union = set(userDict) | set(otherUserDict))
  #then go through artist dictionaries and look to see if there are songs by artist that one person has that other people do not
  #non_intersection = 
  
  #if value in userDict but key not in userDict-->Reccommender!
    # reccommender built by cliques        
            
# go through user edges to determine who has the most songs in common: use score to find who has music in common
with open("edge_weights.txt",'w') as newFile:
     for (u,v,d) in userGraph.edges(data='weight'):
         if d>100: 
            newFile.write(u + " and " + v + " have "+ str(d) +" artists in common. \n")
     width=[w/50 for w in nx.get_edge_attributes(userGraph,'weight').values()]
     nx.draw(nx.Graph(userGraph),node_color=range(4),node_size=500,width=width) 
     plt.savefig("SpotifyVerySmall.pdf")
     
     
     
     
     #community graph
#KC=nx.karate_club_graph()
#plt.clf()
#nx.draw(KC)

#communities=list(cc.label_propagation_communities(KC))
#print(communities)
    # nx.to_agraph(userGraph)
            
x=list(nx.find_cliques(userGraph.to_undirected()))


            
        
    
            

                            
