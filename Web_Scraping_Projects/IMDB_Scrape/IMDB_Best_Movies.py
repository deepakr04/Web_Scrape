from selenium import webdriver
from bs4 import BeautifulSoup
import time


def IMDB_Best_Movies():
    url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    time.sleep(2)
    top250movies = soup.find('h1', class_='header').text
    print("-------------{}-------------".format(top250movies))

    movies = soup.find('tbody', class_='lister-list')

    for movie in movies.find_all('td', class_ = 'titleColumn'):
        full_title = movie.text.strip().replace('\n', '').replace('      ', '')
        # print(full_title)

        rank = full_title.split('.')[0]
        print('Movie Ratings : ', rank)

        title = full_title.split('.')[1].split('(')[0]
        print('Movie Title   : ', title)

        year = full_title.split('(')[1][:-1]
        print('Released Year : ', year)

        a = movie.find('a')
        print('Movie Link    : ', "https://www.imdb.com/"+a['href'])
        print("============")

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=r'D:\WebScraping_Projects\chromedriver.exe')
    IMDB_Best_Movies()
    time.sleep(5)
    driver.quit()