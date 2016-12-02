# BT3051 Assignment 3
#Roll number : BE14B002
# Collaborators : None
#Time: 1:30
from bs4 import BeautifulSoup as bs
def parse_SBML(name):
	with open(name) as content:
		soup = bs(content, 'xml')
		name={}
	for ispecies in soup.listOfSpecies:
		if(ispecies.name =="species"):
			name[ispecies.attrs['id']]=ispecies.attrs['name']
	for ireactions in soup.listOfReactions:
		reactflag=0
		prodflag=0
		if ireactions.name == "reaction" :
			print(ireactions.attrs['id'],":",end=" ",sep="")
			for ireactants in ireactions.listOfReactants:				
				if ireactants.name == "speciesReference":
					if reactflag == 1:
						print("+",end=" ")
					if int(float(ireactants.attrs['stoichiometry']))==1:
						print(name[ireactants.attrs['species']],end=" ")
						reactflag=1
					elif float(ireactants.attrs['stoichiometry']).is_integer():
						print(int(float(ireactants.attrs['stoichiometry'])),name[ireactants.attrs['species']],end=" ")
						reactflag=1
					else:
						print(ireactants.attrs['stoichiometry'],name[ireactants.attrs['species']],end=" ")
						reactflag=1
			if ireactions.attrs['reversible'] == "true":
				print("<==>",end=" ")
			else :
				print("==>",end=" ")
			for iproducts in ireactions.listOfProducts:				
				if iproducts.name == "speciesReference":
					if prodflag == 1:
						print("+",end=" ")
					if int(float(iproducts.attrs['stoichiometry']))==1:
						print(name[iproducts.attrs['species']],end=" ")
						prodflag=1
					elif float(iproducts.attrs['stoichiometry']).is_integer():
						print(int(float(iproducts.attrs['stoichiometry'])),name[iproducts.attrs['species']],end=" ")
						prodflag=1
					else:
						print(iproducts.attrs['stoichiometry'],name[iproducts.attrs['species']],end=" ")
						prodflag=1
			print()
parse_SBML("Ec_iAF1260_flux1.xml")