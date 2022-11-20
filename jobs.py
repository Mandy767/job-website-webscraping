import bs4
import time

# import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



endpoint = "https://www.naukri.com/research-development-jobs-"
page = 1

row_head=['Company','Job Title','Required Skills','Experience','Qualification']
data=[]

while page != 1112: 

        print(page)
        driver.get(endpoint+str(page))
        page=page+1
        time.sleep(3)
        print('3 secs ended')
        html = driver.page_source

        soup = bs4.BeautifulSoup(html, "html.parser")


        jobs = soup.find_all("article", class_="jobTuple bgWhite br4 mb-8")
        
 

        for job in jobs:
            title = job.find("a", class_="title")
            company=job.find("a",class_="subTitle ellipsis fleft")
            E=job.find('ul',class_="mt-7")
            Experience=E.find('li',class_="fleft grey-text br2 placeHolderLi experience")
            # qualifications=job.find()
            z=job.find('a',class_="title fw500 ellipsis")['href']
            driver.get(z)
            time.sleep(2)
            # print('2 secs ended')
            h = driver.page_source

            x = bs4.BeautifulSoup(h, "html.parser")



            if Experience:
                e=Experience.text
            else:
                e=None

            quali=[]
            education=x.find('div',class_="education")
            if education:
                edu=education.find_all('div',class_="details")
                if edu:
                        edu=edu;          
                        for j in edu:
                            edut=j.find('span')
                            if edut :
                                        edut=edut
                                        quali.append(edut.text)

               
                            else:
                                        edut=None
                else:
                        edu=None
                        
                        
            else:
                edu=None


            a=job.find_all('li',class_="fleft fs12 grey-text lh16 dot")
            
            if a:
                skill=[]

                for i in a:
                    if i:
                        skill.append(i.text)
                    else:
                        skill.append(None)


 
            if title :
                        t=title.text
               
            else:
                t=None


            if company:
                c=company.text
               
            else:
                c=None

            if Experience:
                e=Experience.text
            else:
                e=None


            data.append(c)
            data.append(t)
            data.append(skill)
            data.append(e)
            data.append(quali)
            
            rows=[data[i:i +5]for i in range(0,len(data),5)]

            with open("remaining2.csv","w",newline="") as csvfile:
                csvwriter=csv.writer(csvfile)
                csvwriter.writerow(row_head)
                csvwriter.writerows(rows)


        

        
   


