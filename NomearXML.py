from xml.dom import minidom

with open ('C:/Users/Guui/Downloads/01 A 15-07 ND 202272827/41220717609308000212550100000016351303140382.xml','r') as f:
    xml = minidom.parse(f)
    nome = xml.getElementsByTagName('xNome')
    nNF = xml.getElementsByTagName('nNF')
    chaveNF = xml.getElementsByTagName('chNFe')
    print(nome[0].firstChild.data)
    print(nNF[0].firstChild.data)
    print(chaveNF[0].firstChild.data)