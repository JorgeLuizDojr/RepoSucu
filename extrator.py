import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

with open('list_id_name_2020.csv', 'r') as f:
    urls = csv.reader(f)

    results_df = pd.DataFrame() #<-- initialize a results dataframe to dump/store the data you collect after each iteration
    for url in urls:   
        my_url = requests.get(url[3]) 
        html = my_url.content
        soup = BeautifulSoup(html,'html.parser')

        data = []  #<-- your data list is "reset" after each iteration of your urls

        name = soup.find('h1', class_="heading name")

        for container in soup.find_all(id="producoes"):
            
            author = name.contents[0]

            article = container.find_all('p')

            data.append({
                'Autor':author,
                'Artigos':article})

            temp_df = pd.DataFrame(data, columns=['Autor', 'Artigos']) #<-- temporary storing the data in a dataframe
            results_df = results_df.append(temp_df).reset_index(drop=True) #<-- dumping that data into a results dataframe

results_df.to_csv('resultado2020.csv', index=False) #<-- writing the results dataframe to csv
