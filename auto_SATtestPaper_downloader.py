import requests
from bs4 import BeautifulSoup



u = 'http://www.ceec.edu.tw/AbilityExam/AbilityExamPaper/105SAT_Paper/105SAT_PaperIndex.htm'
t = '01-106學測國文科定稿.pdf'
years = input('year range(107~96):').split('~')
years = [int(i) for i in years]
years.sort()
##print(years)
y = list(range(years[0], years[-1]+1))	
##print(y)
y.reverse()

for i in y:
  url = 'http://www.ceec.edu.tw/AbilityExam/AbilityExamPaper/%dSAT_Paper/%dSAT_PaperIndex.htm'%(i, i)
  url2 = 'http://www.ceec.edu.tw/AbilityExam/AbilityExamPaper/%dSAT_Paper/%dAbExamPaper.htm'%(i, i)
  url3 = 'http://www.ceec.edu.tw/AbilityExam/AbilityExamPaper/%dSAT_Paper/%d學測試題_Index.htm'%(i, i)
  if i <= 96:
    url = url2
    if i <= 92:
     url = url3
  
  s = requests.Session()
  s.headers.update({'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                   ,'Referer': 'http://www.ceec.edu.tw/AbilityExam/AbilityExamPaper.htm' 
                   ,'Host':'www.ceec.edu.tw'
                   ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                   ,'Accept-Language':'en-US,en;q=0.5'
                   ,'Accept-Encoding':'gzip, deflate'
                   ,'Connection':'keep-alive'
                   ,'Upgrade-Insecure-Requests':'1'
                   ,'If-Modified-Since':'Tue, 07 Mar 2017 11:03:56 GMT'
                   ,'If-None-Match':'"20c8833297d21:0"'
                   ,'Cache-Control':'max-age=0'})
  print('GET %s'%url)
  res = s.get(url)
  res.encoding = 'ut-16'
  soup = BeautifulSoup(res.text, 'html.parser')
  sth = soup.find_all('a', href=True)
  
  if i >=100:
    pad = -21
  elif i > 96:
    pad = -20
  elif i > 92:
    pad = -17  
  else:
    pad = -16
  
  for j in sth:
    if (j['href'].split('.')[-1] == 'pdf') and (ord(j['href'][0]) <= 57):
      fname = j['href']
      path = 'SAT%d\\%s'%(i, fname)
      print('GET '+url[:pad]+fname)
      se = requests.Session()
      se.headers.update({'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                   ,'Referer': 'http://www.ceec.edu.tw/AbilityExam/AbilityExamPaper.htm' 
                   ,'Host':'www.ceec.edu.tw'
                   ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                   ,'Accept-Language':'en-US,en;q=0.5'
                   ,'Accept-Encoding':'gzip, deflate'
                   ,'Connection':'keep-alive'
                   ,'Upgrade-Insecure-Requests':'1'
                   ,'If-Modified-Since':'Tue, 07 Mar 2017 11:03:56 GMT'
                   ,'If-None-Match':'"20c8833297d21:0"'
                   ,'Cache-Control':'max-age=0'})
      pdf = se.get(url[:pad]+fname)
      f = open(fname, 'wb')
      f.write(pdf.content)
      f.close()
      print('SAVED '+j['href'])
  '''  
    f = open(path, 'wb')
    f.write(pdf.content)
    f.close()
  '''  
	