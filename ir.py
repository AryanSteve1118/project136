import pandas as pd 

df=pd.read_csv("c134.csv")

#row_num,name,start_name,distance,mass,radius,gravity
n=df["name"].to_list()
m=df["mass"].to_list()
r=df["radius"].to_list()
d=df["distance"].to_list()
g=df["gravity"].to_list()

final_list=[]
final_dict={}
for i in range(0,len(n)):
    final_dict["name"]=n[i]
    final_dict["mass"]=m[i]
    final_dict["radius"]=r[i] 
    final_dict["gravity"]=g[i]
    final_dict["distance"]=d[i]
    final_list.append(final_dict)
    final_dict={}

print(final_list)