l='html.parser'
k='Groupe'
j='titre module'
i=enumerate
h=input
d='cadrenormal'
b='table'
a=False
Z='D'
Y='C'
X='B'
W='A'
V='N° module'
U=open
T=len
S=int
R=float
L='Dispositifs'
K='N° dispo.'
J=True
F='Modules'
D=print
B='Dates'
A=''
import re as C
from pathlib import Path as M
import pandas as E
from openpyxl import load_workbook as m
from openpyxl.styles import Border as n,Side,Alignment as o
import time
from datetime import datetime as p
import sys,math,browser_cookie3 as q,requests as r
from bs4 import BeautifulSoup as c
def s(step,total_steps,bar_width=60,title=A,print_perc=J):
	F=title;import sys;G=['█','▏','▎','▍','▌','▋','▊','█'];C=100*R(step)/R(total_steps);H=bar_width*8;E=S(round(C/100*H));J=E/8;I=E%8;B=D=A;D+=G[0]*S(J)
	if I>0:D+=G[I]
	D+='▒'*S(H/8-R(E)/8.)
	if T(F)>0:B=F+': '
	B+='\x1b[0;32m';B+=D;B+='\x1b[0m'
	if print_perc:
		if C>1e2:C=1e2
		B+=' {:6.2f}'.format(C)+' %'
	sys.stdout.write('\r'+B);sys.stdout.flush()
t='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/animPedagogiques/liste_dispoAnim.jsp'
u='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/dispo/arbre_dispositif.jsp?cCode='
v={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'}
G=[[K,'Circo','titre dispo.']]
N=[[K,V,j,"nombre d'heures"]]
I=[[K,V,k,'date','Heure début','Heure fin']]
A9=[]
e='(E R R E U R|authentification)'
def AA(namefile,data):
	with U(namefile,'w',newline='\r\n',encoding='utf-8')as A:
		for B in data:A.write(f"{B}\n")
def w(page):
	A=C.search(e,page)
	if A:D('\nERREUR, ouvrez une session GAIA sous Firefox, vous êtes actuellement non connecté');D("Si l'erreur persiste cliquer dans Stagiaires=>Personnes ou naviguer sur le site GAIA");h('\nAppuyez sur Entrée pour fermer le programme...');sys.exit()
def x(wb):A=wb[B];A.column_dimensions[W].width=13;A.column_dimensions[X].width=14;A.column_dimensions[Y].width=12;A.column_dimensions[Z].width=11;A.column_dimensions['E'].width=12;A.column_dimensions['F'].width=12;A.column_dimensions['G'].width=60;A.column_dimensions['H'].width=14
def y(wb):A=wb[L];A.column_dimensions[W].width=13;A.column_dimensions[X].width=14;A.column_dimensions[Y].width=80
def z(wb):A=wb[F];A.column_dimensions[W].width=13;A.column_dimensions[X].width=10;A.column_dimensions[Y].width=70;A.column_dimensions[Z].width=16
def O(ws,first_row,first_col,last_col):
	for A in ws.iter_rows(min_row=first_row,max_row=ws.max_row,min_col=first_col,max_col=last_col):
		for B in A:B.alignment=o(horizontal='center')
def P(ws,first_row,first_col):
	A=Side(border_style='thin')
	for B in ws.iter_rows(min_row=first_row,max_row=ws.max_row,min_col=first_col,max_col=ws.max_column):
		for C in B:C.border=n(left=A,right=A,top=A,bottom=A)
def Q(ws,ref):A=ws.auto_filter;A.ref=ref
def A0(ws,col):
	for A in ws[col]:
		if A.row>1:A.number_format='DD/MM/YYYY'
def AB(df,num_module):
	B=df.loc[df[V]==num_module,K]
	if not B.empty:return B.iloc[0]
	return A
def A1(namefile):
	C=namefile;H=I[1:];H.sort(key=lambda x:p.strptime(x[3],'%d/%m/%Y'));D={L:E.DataFrame(G[1:],columns=G[0]),F:E.DataFrame(N[1:],columns=N[0]),B:E.DataFrame(H,columns=I[0])};J=[];K=[]
	for M in range(1,T(I)):J.append(f"=VLOOKUP(B{M+1},Modules!B:D,2,FALSE)");K.append(f"=VLOOKUP(A{M+1},Dispositifs!A:C,2,FALSE)")
	D[B][j]=E.Series(J);D[B]['circo']=E.Series(K)
	with E.ExcelWriter(C,engine='openpyxl')as R:
		for(S,U)in D.items():U.to_excel(R,sheet_name=S,index=a)
	A=m(C);x(A);O(A[B],1,2,6);P(A[B],1,1);A0(A[B],Z);Q(A[B],'A:H');y(A);P(A[L],1,1);Q(A[L],'A:C');z(A);O(A[F],1,2,2);O(A[F],1,4,4);P(A[F],1,1);Q(A[F],'A:D');A.save(C)
def f(url,from_disk=J):
	E=url;D=A;H=C.search('/([^/]+)\\.jsp\\S*',E);I=C.findall('=([^/]+)',E)
	if H:
		F='cache/'+H.group(1)
		if I:F=F+'_'+I[0]
		D=M(__file__).parent/f"{F}.html"
	if from_disk and D.exists():
		with U(D,'r')as G:B=G.read()
		J=C.search(e,B)
		if not J:return B
	K=q.firefox();L=r.get(E,headers=v,cookies=K);B=L.text;w(B)
	if D:
		with U(D,'w',encoding='ISO-8859-15')as G:G.write(B)
	return B
def A2(html):
	H=c(html,l);D=H.find(b,class_=d);I=D.find_all('font',class_='visupetit');E=D.find_all('a',class_='listegras')
	for(F,J)in i(I):K='^^([a-zA-Z]*) ?(\\d)?';B=C.search(K,E[F].text);L=B.group(2)if B and B.lastindex>=2 else A;B=B.group(1)if B else A;G.append([J.text,B+' '+L,E[F].text.replace(';',',').strip()])
def A3(html,num_module):
	H=num_module;M=c(html,l);O=M.find_all(b,class_=d)[1];P=O.find_all('td',class_=lambda c:c!=d and(c=='listeelem1'or c=='listeelem2'));E=0;F=A;J=A
	for B in P:
		Q=B.find(b)
		if Q:B=B.find_all('td')[0]
		if B.text and'<a href='not in B:
			K=C.findall('^\\d{4}',B.text)
			if K:L=C.findall('(\\d) ?H$',B.text);G='^\\d{4} *-? *(.+?)( *-? *\\d *H)?$';R=C.search(G,B.text);F=K[0];J=L[0]if L else A;N.append([H,F,R.group(1).replace(';',',').strip(),J]);E=0
			elif k in B.text:E=B.text[-2:]
			else:
				G='^(\\d{2}\\/\\d{2}\\/\\d{4})\xa0(\\d{2}:\\d{2})\xa0\xa0(\\d{2}\\/\\d{2}\\/\\d{4})\xa0(\\d{2}:\\d{2})$';D=C.search(G,B.text)
				if D:S=D.group(1)if D else A;T=D.group(2)if D and D.lastindex>=2 else A;U=D.group(4)if D and D.lastindex>=4 else A;I.append([H,F,E,S,T,U])
if __name__=='__main__':
	H=M('cache')
	if not H.exists():H.mkdir(parents=J)
	H=M('output')
	if not H.exists():H.mkdir(parents=J)
	D();A4=f(t,from_disk=a);A2(A4)
	for(A5,A6)in i(G[1:]):s(A5+1,T(G[1:]),title='Lecture des modules de formation (MAJ dates)        ');g=A6[0];A7=u+g;A8=f(A7,from_disk=a);A3(A8,g)
	D();D();A1('output/synthese_planning.xlsx');D();D("Traitement terminé, le fichier de synthèse se trouve dans le dossier 'output'");h('Appuyez sur Entrée pour fermer le programme...')
