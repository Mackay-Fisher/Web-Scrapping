from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
cacao_ratings = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(cacao_ratings.content,"html.parser")
rating_tags = soup.find_all(attrs={"class": "Rating"})
ratings = []
for Rating in rating_tags[1:]:
  ratings.append(float(Rating.get_text()))
plt.hist(ratings)
plt.show()
company_tags = soup.find_all(attrs={'class':'Company'})
companies = []
for Company in company_tags[1:]:
     companies.append(Company.get_text())
Coco_percentage=soup.find_all(attrs={'class':'CocoaPercent'})
coco = []
for CocoaPercent in Coco_percentage[1:]:
    s=CocoaPercent.get_text()
    s=float(s.translate({ord('%'): None}))
    coco.append(s)
loc_tags= soup.find_all(attrs={'class': 'CompanyLocation'}) 
location = []   
for CompanyLocation in loc_tags[1:]:
    location.append(CompanyLocation.get_text())
Coco_bean =soup.find_all(attrs={'class':'BroadBeanOrigin'})
bean = []
for BroadBeanOrigin in Coco_bean[1:]:
    bean.append(BroadBeanOrigin.get_text())
plt.scatter(ratings,coco)
print("Top ten companies")
d = {"Company": companies, "Rating": ratings , "Coaco_Percentage": coco}
company_choc_df = pd.DataFrame.from_dict(d)
mean_ratings=company_choc_df.groupby("Company").mean()
ten_best =mean_ratings.nlargest(10,'Rating')
print(ten_best)
print()
print("Top ten company Locations")
a = {"Company Location": location, "Rating": ratings}
company_choc_df1 = pd.DataFrame.from_dict(a)
mean_ratings=company_choc_df1.groupby("Company Location").Rating.mean()
ten_best =mean_ratings.nlargest(10)
print(ten_best)
print()
print("Top ten Beans")
a = {"Bean Origin": bean, "Rating": ratings}
company_choc_df1 = pd.DataFrame.from_dict(a)
mean_ratings=company_choc_df1.groupby("Bean Origin").Rating.mean()
ten_best =mean_ratings.nlargest(10)
print(ten_best)
