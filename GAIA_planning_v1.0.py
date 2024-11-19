k='html.parser'
j='Groupe'
i='titre module'
h=enumerate
g=input
b='cadrenormal'
a='table'
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
G='Modules'
F=True
X=False
D=print
B='Dates'
A=''
import re as C
from pathlib import Path as M
import pandas as E
from openpyxl import load_workbook as l
from openpyxl.styles import Border as m,Side,Alignment as n
import time
from datetime import datetime as o
import sys,math,browser_cookie3 as p,requests as q
from bs4 import BeautifulSoup as c
def r(step,total_steps,bar_width=60,title=A,print_perc=F):
	F=title;import sys;G=['█','▏','▎','▍','▌','▋','▊','█'];C=100*R(step)/R(total_steps);H=bar_width*8;E=S(round(C/100*H));J=E/8;I=E%8;B=D=A;D+=G[0]*S(J)
	if I>0:D+=G[I]
	D+='▒'*S(H/8-R(E)/8.)
	if T(F)>0:B=F+': '
	B+='\x1b[0;32m';B+=D;B+='\x1b[0m'
	if print_perc:
		if C>1e2:C=1e2
		B+=' {:6.2f}'.format(C)+' %'
	sys.stdout.write('\r'+B);sys.stdout.flush()
s='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/animPedagogiques/liste_dispoAnim.jsp'
t='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/dispo/arbre_dispositif.jsp?cCode='
u={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'}
H=[[K,'Circo','titre dispo.']]
N=[[K,V,i,"nombre d'heures"]]
J=[[K,V,j,'date','Heure début','Heure fin']]
A8=[]
d='(E R R E U R|authentification)'
def A9(namefile,data):
	with U(namefile,'w',newline='\r\n',encoding='utf-8')as A:
		for B in data:A.write(f"{B}\n")
def v(page):
	A=C.search(d,page)
	if A:D('\nERREUR, ouvrez une session GAIA sous Firefox, vous êtes actuellement non connecté');D("Si l'erreur persiste cliquer dans Stagiaires=>Personnes ou naviguer sur le site GAIA");g('\nAppuyez sur Entrée pour fermer le programme...');sys.exit()
def w(wb):A=wb[B];A.column_dimensions[W].width=13;A.column_dimensions[X].width=14;A.column_dimensions[Y].width=12;A.column_dimensions[Z].width=11;A.column_dimensions['E'].width=12;A.column_dimensions['F'].width=12;A.column_dimensions['G'].width=60;A.column_dimensions['H'].width=14
def x(wb):A=wb[L];A.column_dimensions[W].width=13;A.column_dimensions[X].width=14;A.column_dimensions[Y].width=80
def y(wb):A=wb[G];A.column_dimensions[W].width=13;A.column_dimensions[X].width=10;A.column_dimensions[Y].width=70;A.column_dimensions[Z].width=16
def O(ws,first_row,first_col,last_col):
	for A in ws.iter_rows(min_row=first_row,max_row=ws.max_row,min_col=first_col,max_col=last_col):
		for B in A:B.alignment=n(horizontal='center')
def P(ws,first_row,first_col):
	A=Side(border_style='thin')
	for B in ws.iter_rows(min_row=first_row,max_row=ws.max_row,min_col=first_col,max_col=ws.max_column):
		for C in B:C.border=m(left=A,right=A,top=A,bottom=A)
def Q(ws,ref):A=ws.auto_filter;A.ref=ref
def z(ws,col):
	for A in ws[col]:
		if A.row>1:A.number_format='DD/MM/YYYY'
def AA(df,num_module):
	B=df.loc[df[V]==num_module,K]
	if not B.empty:return B.iloc[0]
	return A
def A0(namefile):
	C=namefile;F=J[1:];F.sort(key=lambda x:o.strptime(x[3],'%d/%m/%Y'));D={L:E.DataFrame(H[1:],columns=H[0]),G:E.DataFrame(N[1:],columns=N[0]),B:E.DataFrame(F,columns=J[0])};I=[];K=[]
	for M in range(1,T(J)):I.append(f"=VLOOKUP(B{M+1},Modules!B:D,2,FALSE)");K.append(f"=VLOOKUP(A{M+1},Dispositifs!A:C,2,FALSE)")
	D[B][i]=E.Series(I);D[B]['circo']=E.Series(K)
	with E.ExcelWriter(C,engine='openpyxl')as R:
		for(S,U)in D.items():U.to_excel(R,sheet_name=S,index=False)
	A=l(C);w(A);O(A[B],1,2,6);P(A[B],1,1);z(A[B],Z);Q(A[B],'A:H');x(A);P(A[L],1,1);Q(A[L],'A:C');y(A);O(A[G],1,2,2);O(A[G],1,4,4);P(A[G],1,1);Q(A[G],'A:D');A.save(C)
def e(url,from_disk=F):
	E=url;D=A;H=C.search('/([^/]+)\\.jsp\\S*',E);I=C.findall('=([^/]+)',E)
	if H:
		F='cache/'+H.group(1)
		if I:F=F+'_'+I[0]
		D=M(__file__).parent/f"{F}.html"
	if from_disk and D.exists():
		with U(D,'r')as G:B=G.read()
		J=C.search(d,B)
		if not J:return B
	K=p.firefox();L=q.get(E,headers=u,cookies=K);B=L.text;v(B)
	if D:
		with U(D,'w',encoding='ISO-8859-15')as G:G.write(B)
	return B
def A1(html):
	G=c(html,k);D=G.find(a,class_=b);I=D.find_all('font',class_='visupetit');E=D.find_all('a',class_='listegras')
	for(F,J)in h(I):K='^^([a-zA-Z]*) ?(\\d)?';B=C.search(K,E[F].text);L=B.group(2)if B and B.lastindex>=2 else A;B=B.group(1)if B else A;H.append([J.text,B+' '+L,E[F].text.replace(';',',').strip()])
def A2(html,num_module):
	H=num_module;M=c(html,k);O=M.find_all(a,class_=b)[1];P=O.find_all('td',class_=lambda c:c!=b and(c=='listeelem1'or c=='listeelem2'));E=0;F=A;I=A
	for B in P:
		Q=B.find(a)
		if Q:B=B.find_all('td')[0]
		if B.text and'<a href='not in B:
			K=C.findall('^\\d{4}',B.text)
			if K:L=C.findall('(\\d) ?H$',B.text);G='^\\d{4} *-? *(.+?)( *-? *\\d *H)?$';R=C.search(G,B.text);F=K[0];I=L[0]if L else A;N.append([H,F,R.group(1).replace(';',',').strip(),I]);E=0
			elif j in B.text:E=B.text[-2:]
			else:
				G='^(\\d{2}\\/\\d{2}\\/\\d{4})\xa0(\\d{2}:\\d{2})\xa0\xa0(\\d{2}\\/\\d{2}\\/\\d{4})\xa0(\\d{2}:\\d{2})$';D=C.search(G,B.text)
				if D:S=D.group(1)if D else A;T=D.group(2)if D and D.lastindex>=2 else A;U=D.group(4)if D and D.lastindex>=4 else A;J.append([H,F,E,S,T,U])
if __name__=='__main__':
	I=M('cache')
	if not I.exists():I.mkdir(parents=F)
	I=M('output')
	if not I.exists():I.mkdir(parents=F)
	D();A3=e(s,from_disk=X);A1(A3)
	for(A4,A5)in h(H[1:]):r(A4+1,T(H[1:]),title='Lecture des modules de formation (MAJ dates)        ');f=A5[0];A6=t+f;A7=e(A6,from_disk=X);A2(A7,f)
	D();D();A0('output/synthese_planning.xlsx');D();D("Traitement terminé, le fichier de synthèse se trouve dans le dossier 'output'");g('Appuyez sur Entrée pour fermer le programme...')
