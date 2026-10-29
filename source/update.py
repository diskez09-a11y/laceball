import re
A='/mnt/user-data/attachments/b658cdee-d155-5d95-b76a-2d6e3cb0ab6f/'
fifa={}
for l in open(A+'1067d0fc-attachment.txt',encoding='utf8'):
    m=re.match(r'^(\d+)\.\s+(.+?)(?:\s+\d+\.\d+|\s+\(.*\))$',l.strip())
    if m: fifa[m.group(2)]=int(m.group(1))
rug={}; ifaf={}
for l in open('rugby.txt',encoding='utf8'):
    n,t=l.strip().split(' ',1); rug[t]=int(n)
for l in open('ifaf.txt',encoding='utf8'):
    n,t=l.strip().split(' ',1); ifaf.setdefault(t,int(n))
L=open(A+'b5ea57aa-attachment.txt',encoding='utf8').read().split('\n')
fiba={}
for i,l in enumerate(L):
    if re.fullmatch(r'\d+\.',l) and i+2<len(L) and L[i+1]=='' : fiba.setdefault(L[i+2].strip(), int(l[:-1]))
print(len(fifa),len(rug),len(ifaf),len(fiba))
D={'fifa':215,'rug':115,'ifaf':60,'fiba':160}
GB={'England','Scotland','Wales','Northern Ireland'}
def get(tbl,key,names,default):
    for n in names:
        if n in tbl: return tbl[n], True
    return default, False
def row(name):
    out=[name]; flags=[]
    f={'United States':'USA','Czech Republic':'Czechia','Korea Rep.':'South Korea',"Cote d'Ivoire":'Ivory Coast','Turkiye':'Turkey','UAE':'United Arab Emirates','China PR':'China','Ireland':'Republic of Ireland','Trinidad & Tobago':'Trinidad and Tobago','The Bahamas':'Bahamas',"Hawai'i":'US Virgin Islands','Hong Kong':'Hong Kong','Bosnia & Herzegovina':'Bosnia and Herzegovina'}
    r={'United States':'USA','Czech Republic':'Czechia','Korea Rep.':'Korea',"Cote d'Ivoire":"Côte d'Ivoire",'Turkiye':'Turkey','UAE':'United Arab Emirates','China PR':'China','Northern Ireland':'Ireland','The Bahamas':'Bahamas',"Hawai'i":'US Virgin Islands','Hong Kong':'Hong Kong China'}
    i={'United States':'USA','Czech Republic':'Czechia','Korea Rep.':'Korea','China PR':'China',"Hawai'i":'US Virgin Islands','Hong Kong':'Hong Kong, China'}
    for g in GB: i[g]='Great Britain'
    b={'United States':'USA','Czech Republic':'Czechia','Korea Rep.':'Korea',"Cote d'Ivoire":"Côte d'Ivoire",'Turkiye':'Türkiye','China PR':'China','DR Congo':'Congo DR','The Bahamas':'Bahamas',"Hawai'i":'Virgin Islands','Hong Kong':'Hong Kong, China','Bosnia & Herzegovina':'Bosnia and Herzegovina'}
    for g in GB: b[g]='Great Britain'
    f.update({'Sao Tome and Principe':'São Tomé and Príncipe','Antigua & Barbuda':'Antigua and Barbuda'})
    b.update({'Central African Republic':'Central African Rep.','Antigua & Barbuda':'Antigua & Barbuda','Equatorial Guinea':'Equatorial Guinea'})
    for tbl,m,k in((fifa,f,'fifa'),(rug,r,'rug'),(ifaf,i,'ifaf'),(fiba,b,'fiba')):
        v,ok=get(tbl,k,[m.get(name,name)],D[k]); out.append(v)
        if not ok: flags.append(k)
    return out,flags
