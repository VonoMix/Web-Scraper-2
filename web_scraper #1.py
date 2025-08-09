from bs4 import BeautifulSoup
import requests 
import csv
from datetime import datetime  

page_to_scrape = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
country_name = soup.find_all("h3", attrs={"class": "country-name"})
capital = soup.find_all("span", attrs={"class": "country-capital"})
population = soup.find_all("span", attrs={"class": "country-population"})
area = soup.find_all("span", attrs={"class": "country-area"})

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"scraped_countries_{timestamp}.csv"

with open(filename, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country Name", "Capital", "Population", "Area"]) 

    for name, cap, pop, ar in zip(country_name, capital, population, area):
        print(f"{name.text} - {cap.text} - {pop.text} - {ar.text}")
        writer.writerow([name.text, cap.text, pop.text, ar.text])
print(f"CSV file has been saved as {filename}")
