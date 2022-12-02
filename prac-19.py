from asyncore import close_all
import xml.etree.ElementTree as ET
import pandas as pd

xml_data=open('demo.xml','y').read()
root=ET.XML(xml_data)

data=[]
cols=[]

for i,child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df=pd.DataFrame(data).Tdf.columns= cols 
print(df)
