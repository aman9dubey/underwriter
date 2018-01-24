import csv
from collections import defaultdict

import re
from datetime import datetime

number = r'\d{2,3}'

gender = r'(\b[Mm]ale)|(\b[Ff]emale)|(\bFEMALE)|(\bMALE)'

Date = r'(([A-Z0-9][A-Z0-9]?[/-])?[A-Z0-9][A-Z0-9]?[/-][A-Z0-9][A-Z0-9][A-Z0-9]?[A-Z0-9]?)|([A-Za-z][A-Za-z][A-Za-z]\s..?[,]\s....)'

DOB  = r'DOB|[Dd][aA][tT][eE]\s[oO][fF]\s[Bb][iI][rR][tT][hH]'

year_four_digit = r'\b(19|20)\d{2}(w+)?'
year_two_digit = r'\d{2}$(w+)?'

product_type = r'(\b[Pp]roduct\s[Tt]ype):\s?.*'
permanent = r'[Pp][eE][rR][mM]([aA][nN][aA][nN][tT])?'
term = r'[tT][eE][rR][mM]'

#Assuming USA currency dollar
amount_with_dollar = r'(\$\s?\d{1,3}(,\d{2,3})*(\.\d+)?)([kK]?)([mM]?)([bB]?)'
amount_without_dollar = r'(\$?\s?\d{1,3}(,\d{2,3})*(\.\d+)?)(K?)([mM]?)([bB]?)'
faceamount = r'(\b[Ff]ace\s?[Aa]mount:?\s?.*)'
termamount = r'(.*)?[Tt][eE][rR][mM]\s?(.*)?'   			#Regex to read single line from first newline to next newline
seeking = r'(.*)?[Ss][eE][eE][kK]([iI][nN][gG])?\s?(.*)?'

weight = r'(.*)?\b[wW][eE][iI][gG][hH][tT]\s?(.*)?' 
weight_num = r'(\d*\.?\d+)\s?(lb|lbs|Lbs|LB|LBS|kg|Kg|KG)'		#r'(.*)\s?([lL][bB][sS]|[oO][zZ]|[gG]|[kK][Gg])' 

age = r'(.*\s?[Yy]([eE][aA])?[rR]?[sS]?\s?([oO][lL][dD])?)'

height = r'((.*)?\s?([Ff][eE][eE][tT])((.*)?\s?([iI][nN][Cc][Hh][Ee][Ss]))?)'

smoker = r'\b[sS][Mm][oO][Kk]'
non_smoker = r'\b[nN][oO][nN][-]?\s?[sS][Mm][oO][Kk]'
tobacco = r'(.*)?[Tt][oO][bB][aA][cC][cC][oO]\s?(.*)?'
no = r'[nN][oO]'

def reg(st,i):
	for line in st: #iterate through every line
		#return list of entities in that line
		num = re.search(number, line.decode('utf-8'), re.I | re.U)
		
		x = re.search(Date, line, re.I | re.U)
		'''if(x):
			print (x.group(0)+"\n")
			data[i][0]=(x.group(0))
		else:
			data[i][0]=" "
		'''
		
		#Gender
		y = re.search(gender, line, re.I | re.U)
		if(y):
			print (y.group(0)+"\n")
			data[i][0]=(y.group(0))
		elif(y and num):
			data[i][0]=(y.group(0))
		else:
			data[i][0]=" "
		
		#Year for DOB
		z = 0
		x1 = re.search(year_four_digit, line, re.I | re.U)
		if(x):
			x1 = re.search(year_four_digit, x.group(0), re.I | re.U)
			x2 = re.search(year_two_digit, x.group(0), re.I | re.U)				
			if(x2):
				z = x2.group(0)									
				print('Last 2 digits of Year of birth='+z)
				data[i][1] = '19'+z
			elif(x1):
				data[i][1]=x1.group(0)
		elif(x1):
			x1 = re.search(year_four_digit, line, re.I | re.U)
			print (x1.group(0))
			data[i][1]=x1.group(0)
		else:
			data[i][1]=" "
		
		
		#Age in years
		age_reg = re.search(age, line, re.I | re.U)
		dob = re.search(DOB, line, re.I | re.U)
		if(data[i][1]!=" "):
			currentYear = datetime.now().year
			data[i][2]=(currentYear-(int)(data[i][1]))
		elif(x1 and dob):
			print ("DOB:"+x1.group(0))
			currentYear = datetime.now().year
			print (currentYear-(int)(x1.group(0)))
			data[i][2]=((currentYear-(int)(x1.group(0))))
		elif(x1 and y):
			print ("DOB:"+x1.group(0))
			currentYear = datetime.now().year
			print (currentYear-(int)(x1.group(0)))
			data[i][2]=((currentYear-(int)(x1.group(0))))
		elif(y and num):
			print (num.group(0))
			data[i][2]=num.group(0)
		elif(age_reg):
			age_num = age_reg.group(0)			
			an = re.search(number, age_num, re.I | re.U)
			if(an):				
				print ("DOB:"+ an.group(0))
				data[i][2]=(an.group(0))
		elif(x1):
			print ("DOB:"+x1.group(0))
			currentYear = datetime.now().year
			print (currentYear-(int)(x1.group(0)))
			data[i][2]=((currentYear-(int)(x1.group(0))))
		else:
			data[i][2]=" "
		
		
		#Product Type
		z=re.search(product_type, line, re.I | re.U)
		perm_reg = re.search(permanent, line, re.I | re.U)
		term_reg = re.search(term, line, re.I | re.U)
		if(z): 
			print (z.group(0)+"\n")
			data[i][3]=(z.group(0))
		elif(perm_reg):
			final_str = "Product Type: Permanent"
			data[i][3]=(final_str)
		elif(term_reg):
			final_str = "Product Type: Term"
			data[i][3]=(final_str)
		else:
			data[i][3]=" "
		
		#Face Amount
		#am = re.search(amount, line, re.I | re.U)
		w = re.search(faceamount, line	, re.I | re.U)
		term_reg = re.search(termamount, line, re.I | re.U)
		seek_reg = re.search(seeking, line, re.I | re.U)
		#With faceAmount
		if(w):
			ans=w.group(0)
			am = re.search(amount_without_dollar, ans, re.I | re.U)
			if(am):
				data[i][4]=(am.group(0))
		#With term Amount
		elif(term_reg):
			amd = re.search(amount_with_dollar, term_reg.group(0), re.I | re.U)
			amwd = re.search(amount_without_dollar, term_reg.group(0), re.I | re.U)			#Find 2nd regex in the same line of 1st regex 
			if(amd):
				data[i][4]=(amd.group(0))
			elif(amwd):
				data[i][4]=(amwd.group(0))
		#With Seeking
		elif(seek_reg):
			am = re.search(amount_without_dollar, seek_reg.group(0), re.I | re.U)
			if(am):
				data[i][4]=(am.group(0))
		else:
			data[i][4]=" "
			
		#Weight
		x=re.search(weight_num, line, re.I | re.U) 
		wt=re.search(weight, line, re.I | re.U)
		if(x): 
			print (x.group(0)+"\n")
			data[i][5]=(x.group(0))
		elif(wt):
			am = re.search(weight_num,wt.group(0), re.I | re.U)
			if(amd):
				data[i][4]=(am.group(0))
		else:
			data[i][5]=" "
			
		#Height
		ht=re.search(height, line, re.I | re.U)
		if(ht): 
			print (ht.group(0)+"\n")
			data[i][6]=(ht.group(0))
		else:
			data[i][6]=" "
			
		#Smoker
		sm = re.search(smoker, line, re.I | re.U)
		nsm = re.search(non_smoker, line, re.I | re.U)
		tob = re.search(tobacco, line, re.I | re.U)
		if(sm): 
			print (sm.group(0)+"\n")
			data[i][7]="Smoker"
		elif(nsm):
			print (sm.group(0)+"\n")
			data[i][7]="Non-Smoker"
		elif(tob):
			if(re.search(no, tob.group(0), re.I | re.U)):
				data[i][7]="Non-Tobacco"
			else:
				data[i][7]="Tobacco"
		else:
			data[i][7]=" "
	wtr.writerows(data)




i=0
w, h = 8, 1;
data = [[-1 for x in range(w)] for y in range(h)]
st = []
out = open('out.csv', 'w')
wtr= csv.writer( out )
wtr.writerow(['Gender','Year_of_birth','DOB','Product Type','Face Amount','Weight','Height','Habit'])
#strs = ["" for x in range(size)]

with open('under.csv') as f:
	rows = csv.reader(f)
	for row in rows:
		print('\n----------------------------------------------')
		st.append(row[8])
		reg(st,i)
		#i+=1
		st=[]
		#print (row[8])  

out.close()


