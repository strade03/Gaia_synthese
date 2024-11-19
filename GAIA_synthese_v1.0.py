A2=range
A1=float
h='D'
g='C'
f='B'
e='A'
d='w'
c=int
T=enumerate
S=input
K=open
J=len
D=print
A=''
A3='html.parser'
i='candidat_module_choix_etat'
j='validation'
k='pageActionSuivante'
l='pageAction'
m='cadrenormal'
n='table'
o='ISO-8859-15'
p='Groupe'
q='titre module'
U='Dispositifs'
V='N° module'
W='N° dispo.'
G=False
H='Inscriptions'
I='Modules'
F='Dates'
C=True
import re as B
from pathlib import Path as L
import pandas as E
from openpyxl import load_workbook as A9
from openpyxl.styles import Border,Side,Alignment as AA
import time
from datetime import datetime as AB
import sys,math,browser_cookie3 as r,requests as s
from bs4 import BeautifulSoup as A4
def t(step,total_steps,bar_width=60,title=A,print_perc=C):
	F=title;import sys;G=['█','▏','▎','▍','▌','▋','▊','█'];C=100*A1(step)/A1(total_steps);H=bar_width*8;E=c(round(C/100*H));K=E/8;I=E%8;B=D=A;D+=G[0]*c(K)
	if I>0:D+=G[I]
	D+='▒'*c(H/8-A1(E)/8.)
	if J(F)>0:B=F+': '
	B+='\x1b[0;32m';B+=D;B+='\x1b[0m'
	if print_perc:
		if C>1e2:C=1e2
		B+=' {:6.2f}'.format(C)+' %'
	sys.stdout.write('\r'+B);sys.stdout.flush()
AC='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/animPedagogiques/liste_dispoAnim.jsp'
AD='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/dispo/arbre_dispositif.jsp?cCode='
u={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'}
M=[[W,'Circo','titre dispo.']]
N=[[W,V,q,"nombre d'heures",'nb inscrits']]
X=[[W,V,p,'date','Heure début','Heure fin']]
O=[[V,p,'Nom']]
v=[]
Y='(E R R E U R|authentification)'
def AV(namefile,data):
	with K(namefile,d,newline='\r\n',encoding='utf-8')as A:
		for B in data:A.write(f"{B}\n")
def w(page):
	A=B.search(Y,page)
	if A:D('\nERREUR, ouvrez une session GAIA sous Firefox, vous êtes actuellement non connecté');D("Si l'erreur persiste cliquer dans Stagiaires=>Personnes ou naviguer sur le site GAIA");S('\nAppuyez sur Entrée pour fermer le programme...');sys.exit()
def AE(wb):A=wb[F];A.column_dimensions[e].width=13;A.column_dimensions[f].width=14;A.column_dimensions[g].width=12;A.column_dimensions[h].width=11;A.column_dimensions['E'].width=12;A.column_dimensions['F'].width=12;A.column_dimensions['G'].width=60;A.column_dimensions['H'].width=14
def AF(wb):A=wb[U];A.column_dimensions[e].width=13;A.column_dimensions[f].width=14;A.column_dimensions[g].width=80
def AG(wb):A=wb[I];A.column_dimensions[e].width=13;A.column_dimensions[f].width=10;A.column_dimensions[g].width=70;A.column_dimensions[h].width=16;A.column_dimensions['E'].width=10
def AH(wb):A=wb[H];A.column_dimensions[e].width=10;A.column_dimensions[f].width=10;A.column_dimensions[g].width=70;A.column_dimensions[h].width=60;A.column_dimensions['E'].width=14
def Z(ws,first_row,first_col,last_col):
	for A in ws.iter_rows(min_row=first_row,max_row=ws.max_row,min_col=first_col,max_col=last_col):
		for B in A:B.alignment=AA(horizontal='center')
def a(ws,first_row,first_col):
	A=Side(border_style='thin')
	for B in ws.iter_rows(min_row=first_row,max_row=ws.max_row,min_col=first_col,max_col=ws.max_column):
		for C in B:C.border=Border(left=A,right=A,top=A,bottom=A)
def b(ws,ref):A=ws.auto_filter;A.ref=ref
def AI(ws,col):
	for A in ws[col]:
		if A.row>1:A.number_format='DD/MM/YYYY'
def AJ(df,num_module):
	B=df.loc[df[V]==num_module,W]
	if not B.empty:return B.iloc[0]
	return A
def AK(namefile):
	P='A:E';Q='circo';L=namefile;R=X[1:];R.sort(key=lambda x:AB.strptime(x[3],'%d/%m/%Y'));B={U:E.DataFrame(M[1:],columns=M[0]),I:E.DataFrame(N[1:],columns=N[0]),F:E.DataFrame(R,columns=X[0]),H:E.DataFrame(O[1:],columns=O[0])};C=[];D=[]
	for K in A2(1,J(X)):C.append(f"=VLOOKUP(B{K+1},Modules!B:D,2,FALSE)");D.append(f"=VLOOKUP(A{K+1},Dispositifs!A:C,2,FALSE)")
	B[F][q]=E.Series(C);B[F][Q]=E.Series(D);C=[];D=[]
	for K in A2(1,J(O)):C.append(f"=VLOOKUP(A{K+1},Modules!B:D,2,FALSE)");D.append(f'=VLOOKUP("{AJ(B[I],O[K][0])}",Dispositifs!A:C,2,FALSE)')
	B[H][q]=E.Series(C);B[H][Q]=E.Series(D)
	with E.ExcelWriter(L,engine='openpyxl')as S:
		for(T,V)in B.items():V.to_excel(S,sheet_name=T,index=G)
	A=A9(L);AE(A);Z(A[F],1,2,6);a(A[F],1,1);AI(A[F],h);b(A[F],'A:H');AF(A);a(A[U],1,1);b(A[U],'A:C');AG(A);Z(A[I],1,2,2);Z(A[I],1,4,5);a(A[I],1,1);b(A[I],P);AH(A);Z(A[H],1,2,2);a(A[H],1,1);b(A[H],P);A.save(L)
def A5(url,from_disk=C):
	E=url;D=A;H=B.search('/([^/]+)\\.jsp\\S*',E);I=B.findall('=([^/]+)',E)
	if H:
		F='cache/'+H.group(1)
		if I:F=F+'_'+I[0]
		D=L(__file__).parent/f"{F}.html"
	if from_disk and D.exists():
		with K(D,'r')as G:C=G.read()
		J=B.search(Y,C)
		if not J:return C
	M=r.firefox();N=s.get(E,headers=u,cookies=M);C=N.text;w(C)
	if D:
		with K(D,d,encoding=o)as G:G.write(C)
	return C
def AL(html):
	G=A4(html,A3);D=G.find(n,class_=m);H=D.find_all('font',class_='visupetit');E=D.find_all('a',class_='listegras')
	for(F,I)in T(H):J='^^([a-zA-Z]*) ?(\\d)?';C=B.search(J,E[F].text);K=C.group(2)if C and C.lastindex>=2 else A;C=C.group(1)if C else A;M.append([I.text,C+' '+K,E[F].text.replace(';',',').strip()])
def AM(html,num_module):
	H=num_module;L=A4(html,A3);M=L.find_all(n,class_=m)[1];O=M.find_all('td',class_=lambda c:c!=m and(c=='listeelem1'or c=='listeelem2'));E=0;F=A;I=A
	for C in O:
		P=C.find(n)
		if P:C=C.find_all('td')[0]
		if C.text and'<a href='not in C:
			J=B.findall('^\\d{4}',C.text)
			if J:K=B.findall('(\\d) ?H$',C.text);G='^\\d{4} *-? *(.+?)( *-? *\\d *H)?$';Q=B.search(G,C.text);F=J[0];I=K[0]if K else A;N.append([H,F,Q.group(1).replace(';',',').strip(),I,0]);E=0
			elif p in C.text:E=C.text[-2:]
			else:
				G='^(\\d{2}\\/\\d{2}\\/\\d{4})\xa0(\\d{2}:\\d{2})\xa0\xa0(\\d{2}\\/\\d{2}\\/\\d{4})\xa0(\\d{2}:\\d{2})$';D=B.search(G,C.text)
				if D:R=D.group(1)if D else A;S=D.group(2)if D and D.lastindex>=2 else A;T=D.group(4)if D and D.lastindex>=4 else A;X.append([H,F,E,R,S,T])
def AN(url,code_dispo,code_module,from_disk=C):
	M=code_dispo;H=code_module;E=L(__file__).parent/f"cache/coDisp_{H}.html";N=C
	if from_disk and E.exists():
		with K(E,'r')as I:D=I.read()
		Q=B.search(Y,D)
		if not Q:N=G
	O='20'+M[0:2];id=M[0:6];R={'etatCandidatAccueil':j,'modeCandidatAccueil':'choixmodule','pageActionDispoUnique':A,'pageActionPersonneUnique':A,'pageActionPersonneUniqueSansCandidature':A,'pageActionDispoUniqueSansCandidature':A,l:'candidat_accueil',k:i,'sDispoPrefix':id,'modesansactif':'Y','champ_id':id,'champ_annee_dispositif':O,'champ_libl_dispositif':A,'champ_co_modu':f"{H}",'champ_annee_personne':O,'champ_nom_personne':A,'champ_prenom_personne':A,'champ_code_etab':A,'filtrePersActif':'on'}
	if N:
		S=r.firefox();T=s.post(url,headers=u,cookies=S,data=R);D=T.text;w(D)
		if E:
			with K(E,d,encoding=o)as I:I.write(D)
	J='coDisp" value="(\\d*)"';F=B.search(J,D);F=F.group(1)if F else'nop';J='TOUTES <\\/b> \\((\\d*)';P=B.search(J,D);U=c(P.group(1))if P else 0;return[H,F,U]
def AO(url,num_module,num_coDisp,nb_page,from_disk=C):
	R='champ_etat';S=num_coDisp;N='candidat_module_liste_candidature';F='T';H=num_module;U=L(__file__).parent/f"cache/inscrits_{H}"
	for P in A2(nb_page):
		I=U.with_name(f"{U.name}-{P}.html");V=C
		if from_disk and I.exists():
			with K(I,'r')as Q:D=Q.read()
			X=B.search(Y,D)
			if not X:V=G
		if P==0:W={'etatCandidatModuleChoixEtat':j,'modeCandidatModuleChoixEtat':'selection',l:i,k:N,'etat':F,'coModu':H,'coDisp':S,R:F}
		else:W={'etatCandidatModuleListeCandidature':j,'modeCandidatModuleListeCandidature':'avanceposition',l:N,k:N,'pageActionPrecedente':i,'champ_noMatr':A,'champ_noMatrVisuPersonne':A,'champ_coDisp':S,'champ_coModu':H,'etatChoisi':F,R:F,'champ_lettre':A,'champ_reculeposition':A,'champ_avanceposition':f"{15*P}",'champ_positiondepart':'0'}
		if V:
			Z=r.firefox();time.sleep(.5);a=s.post(url,headers=u,cookies=Z,data=W);D=a.text;w(D)
			if I:
				with K(I,d,encoding=o)as Q:Q.write(D)
		E='visualisation_personne\\(\'\\d*\'\\);\\">\\s*([a-zA-Z .-]*)<\\/a>';b=B.findall(E,D);E="visualisation_personne\\('(\\d*)'\\)";c=B.findall(E,D)
		for(e,f)in T(b):E=f'name=\\"candidature{c[e]}GroupeChoisi\\"\\s*value=\\"(\\d*)';M=B.findall(E,D);M=M[0]if J(M)>0 else A;O.append([H,M,f])
if __name__=='__main__':
	P=L('cache')
	if not P.exists():P.mkdir(parents=C)
	P=L('output')
	if not P.exists():P.mkdir(parents=C)
	D("Un système de cache permet d'accèlerer le traitement mais ne mettra à jour que les nouvelles informations");D("Si vous demandez la mise à jour, les informations seront récupérées sur GAIA sinon à partir du cache s'il existe.");D('Que souhaitez-vous faire ?');x=S('Mettre à jour les dates des formations (O/N) :');Q=S("Mettre à jour le nombre d'inscriptions (O/N) : ");y=S('Mettre à jour la listes des enseignants inscrits (O/N) :');x=G if x.lower()=='o'else C;Q=G if Q.lower()=='o'else C;y=G if y.lower()=='o'else C;D();AP=A5(AC,from_disk=G);AL(AP)
	for(R,Q)in T(M[1:]):t(R+1,J(M[1:]),title='Lecture des modules de formation (MAJ dates)        ');A6=Q[0];AQ=AD+A6;AR=A5(AQ,from_disk=x);AM(AR,A6)
	D();A7='https://gaia.phm.education.gouv.fr/gaia/gacmfgest/centrale'
	for(R,z)in T(N[1:]):
		t(R+1,J(N)-1,title="Lecture des dispositifs (MAJ nb d'inscrits)         ");A0=AN(A7,z[0],z[1],from_disk=Q)
		if'nop'not in A0:z[4]=A0[2];v.append(A0)
	D()
	for(R,(AS,AT,A8))in T(v):
		t(R+1,J(v)-1,title='Lecture des inscriptions (liste des inscriptions)   ')
		if A8>0:AU=math.ceil(A8/15);AO(A7,AS,AT,AU,from_disk=y)
	D();AK('output/synthese.xlsx');D();D("Traitement terminé, le fichier de synthèse se trouve dans le dossier 'output'");S('Appuyez sur Entrée pour fermer le programme...')
