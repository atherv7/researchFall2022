from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def wait(ob): 
    ob.implicitly_wait(5000)

url = input('Enter the url for the site: ')
linkX = ""
sBarX = ""
eYearX = ""
sYearX = ""
nOfRX = ""
ebsco = False 
if url == 'https://lib.guides.umd.edu/az.php?q=EconLit': 
    linkX = "/html/body/div[5]/section[2]/div/div[1]/div[3]/div[1]/div[1]/a"
    sBarX = '/html/body/form/div[2]/div[1]/div[2]/section/div/fieldset/section/div/ul/li[1]/input[2]'
    sYearX = '/html/body/form/div[2]/div[1]/div[4]/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/input'
    eYearX = '/html/body/form/div[2]/div[1]/div[4]/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/input'
    nOfRX = '/html/body/form/div[2]/div[1]/div[3]/div/div/div/main/div[1]/h1'
    ebsco = True 
elif url == 'https://www.jstor.org/': 
    sBarX = '/html/body/main/div[2]/search-ui-pharos-layout/search-ui-pharos-layout/div/form/div/div/mfe-query-builder-pharos-input-group'
    sYearX = '/html/body/main/div[2]/div/div/div[2]/div[2]/section/div[4]/div/div/div[1]/search-results-vue-pharos-text-input//div/input'
    eYearX = '//*[@id="to-date"]'
    nOfRX = '/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/search-results-vue-pharos-heading/div'
else: 
    #this is only needed for demonstration 
    linkX = input('Enter the xpath for the link to the site: ')
    sBarX = input('Enter the xPath of the search bar: ')
    sYearX = input('Enter the xPath for the start year: ')
    eYearX = input('Enter the xPath for the end year: ')
    nOfRX = input('Enter the xPath of the number of results: ')
    ebsco = True


driver = Chrome(executable_path='chromedriver.exe')
driver.maximize_window() 
driver.get(url)
wait(driver)

if ebsco: 
    link = driver.find_element(by=By.XPATH, value=linkX)
    link.click() 
    wait(driver)

search = driver.find_element(by=By.XPATH, value=sBarX)
search.click() 
search.send_keys("war" + Keys.ENTER)
wait(driver)
start = driver.find_element(by=By.XPATH, value=sYearX) 
start.click() 
start.clear() 
start.send_keys("1990" + Keys.ENTER)
wait(driver)
end = driver.find_element(by=By.XPATH, value=eYearX)
end.click() 
end.clear() 
end.send_keys("2020" + Keys.ENTER)
results = driver.find_element(by=By.XPATH, value=nOfRX)
print(results.text)
driver.close() 
