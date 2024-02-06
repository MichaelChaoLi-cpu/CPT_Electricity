# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:05:18 2023

@author: Li Chao
"""
# Utilities > Utilities > Electric Utilities & IPPs > Electric Utilities > Electric Utilities (NEC)

from glob import glob 
from joblib import dump, load
import pandas as pd
import regex as re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open('Key/EikonKey.txt', 'r') as file:
    file_content = file.read()

print(file_content)

driver = webdriver.Chrome()

eikon = 'https://apac1-apps.platform.refinitiv.com/web/Apps/IndustryApp#/filings'
driver.get(eikon)

#driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

iframe_xpath = '//*[@id="AppFrame"]'
iframe_element = driver.find_element(By.XPATH, iframe_xpath)
driver.switch_to.frame(iframe_element)

iframe_xpath = '//*[@id="contentframe"]'
iframe_element = driver.find_element(By.XPATH, iframe_xpath)
driver.switch_to.frame(iframe_element)

iframe_xpath = '//*[@id="AppFrame"]'
iframe_element = driver.find_element(By.XPATH, iframe_xpath)
driver.switch_to.frame(iframe_element)

iframe_xpath = '/html/body/ui-view/div/ui-view/div/div[2]/iframe'
iframe_element = driver.find_element(By.XPATH, iframe_xpath)
driver.switch_to.frame(iframe_element)

##### first round
data_info = []

for page in list(range(14)):
    for batch in list(range(10)):
        for row_number in list(range(1,21)):
            try:
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(3) > div:nth-child({row_number}) > button > span > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                stock_name = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(7) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_doc_date = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(10) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_country = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(11) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_industry = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(12) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_DCN = element_within_shadow.text

                info = [stock_name, element_text_doc_date, 
                        element_text_country, element_text_industry,
                        element_text_DCN]
                data_info.append(info)
                print(info)
                
                df = pd.DataFrame(data_info)
                df.to_csv("Data/Elec_DownloadedReport_v2_AllInfoTab.csv")
                time.sleep(1)
            except:
                print(page, batch, row_number)
                
        shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
        shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath)))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        scrollable_element_selector = 'div.grid-scrollbar.grid-vscroll.grid-scroll-fadeout'
        scrollable_element = shadow_root.find_element(By.CSS_SELECTOR, scrollable_element_selector)
        driver.execute_script("arguments[0].scrollTop += 650;", scrollable_element)
        time.sleep(2)
        
    shadow_host_xpath_download = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/div/span/emerald-pagination"
    shadow_root_download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath_download))).shadow_root
    element_within_shadow_xpath_download = '#next'
    WebDriverWait(shadow_root_download, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath_download))).click()
    time.sleep(5)
    
    print(f"****{page+1}****")                
                

df_once = df.drop_duplicates()   
df_once.columns = ['Code', 'Doc_Time', 'Country',
                   'Industry', "DCN"] 
have_list = df_once['DCN'].to_list()

##### second round
data_info = []

for page in list(range(14)):
    for batch in list(range(10)):
        for row_number in list(range(1,21)):
            try:
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(3) > div:nth-child({row_number}) > button > span > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                stock_name = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(7) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_doc_date = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(10) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_country = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(11) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_industry = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(12) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_DCN = element_within_shadow.text
                
                if element_text_DCN not in have_list:
                    info = [stock_name, element_text_doc_date, 
                            element_text_country, element_text_industry,
                            element_text_DCN]
                    data_info.append(info)
                    print(info)
                    
                    df = pd.DataFrame(data_info)
                    df.to_csv("Data/Elec_DownloadedReport_v2_AllInfoTab_add.csv")
                time.sleep(1)
            except:
                print(page, batch, row_number)
                
        shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
        shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath)))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        scrollable_element_selector = 'div.grid-scrollbar.grid-vscroll.grid-scroll-fadeout'
        scrollable_element = shadow_root.find_element(By.CSS_SELECTOR, scrollable_element_selector)
        driver.execute_script("arguments[0].scrollTop += 680;", scrollable_element)
        time.sleep(2)
        
    shadow_host_xpath_download = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/div/span/emerald-pagination"
    shadow_root_download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath_download))).shadow_root
    element_within_shadow_xpath_download = '#next'
    WebDriverWait(shadow_root_download, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath_download))).click()
    time.sleep(5)
    
    print(f"****{page+1}****")   

df_second = df.drop_duplicates()   
df_second.columns = ['Code', 'Doc_Time', 'Country',
                     'Industry', "DCN"] 
have_list_second = df_second['DCN'].to_list()
have_list_merge = have_list + have_list_second

##### third round
data_info = []

for page in list(range(14)):
    for batch in list(range(10)):
        for row_number in list(range(1,21)):
            try:
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(3) > div:nth-child({row_number}) > button > span > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                stock_name = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(7) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_doc_date = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(10) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_country = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(11) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_industry = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(12) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_DCN = element_within_shadow.text
                
                if element_text_DCN not in have_list_merge:
                    info = [stock_name, element_text_doc_date, 
                            element_text_country, element_text_industry,
                            element_text_DCN]
                    data_info.append(info)
                    print(info)
                    
                    df = pd.DataFrame(data_info)
                    df.to_csv("Data/Elec_DownloadedReport_v2_AllInfoTab_add2.csv")
                time.sleep(1)
            except:
                print(page, batch, row_number)
                
        shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
        shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath)))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        scrollable_element_selector = 'div.grid-scrollbar.grid-vscroll.grid-scroll-fadeout'
        scrollable_element = shadow_root.find_element(By.CSS_SELECTOR, scrollable_element_selector)
        driver.execute_script("arguments[0].scrollTop += 620;", scrollable_element)
        time.sleep(2)
        
    shadow_host_xpath_download = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/div/span/emerald-pagination"
    shadow_root_download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath_download))).shadow_root
    element_within_shadow_xpath_download = '#next'
    WebDriverWait(shadow_root_download, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath_download))).click()
    time.sleep(5)
    
    print(f"****{page+1}****")   


df_third = df.drop_duplicates()   
df_third.columns = ['Code', 'Doc_Time', 'Country',
                     'Industry', "DCN"] 
have_list_third = df_third['DCN'].to_list()
have_list_merge = have_list + have_list_second + have_list_third

##### third round
data_info = []

for page in list(range(14)):
    for batch in list(range(10)):
        for row_number in list(range(1,21)):
            try:
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(3) > div:nth-child({row_number}) > button > span > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                stock_name = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(7) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_doc_date = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(10) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_country = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(11) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_industry = element_within_shadow.text
                
                shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(12) > div:nth-child({row_number}) > button > span'
                element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
                element_text_DCN = element_within_shadow.text
                
                if element_text_DCN not in have_list_merge:
                    info = [stock_name, element_text_doc_date, 
                            element_text_country, element_text_industry,
                            element_text_DCN]
                    data_info.append(info)
                    print(info)
                    
                    df = pd.DataFrame(data_info)
                    df.to_csv("Data/Elec_DownloadedReport_v2_AllInfoTab_add3.csv")
                time.sleep(1)
            except:
                print(page, batch, row_number)
                
        shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
        shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath)))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        scrollable_element_selector = 'div.grid-scrollbar.grid-vscroll.grid-scroll-fadeout'
        scrollable_element = shadow_root.find_element(By.CSS_SELECTOR, scrollable_element_selector)
        driver.execute_script("arguments[0].scrollTop += 680;", scrollable_element)
        time.sleep(2)
        
    shadow_host_xpath_download = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/div/span/emerald-pagination"
    shadow_root_download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath_download))).shadow_root
    element_within_shadow_xpath_download = '#next'
    WebDriverWait(shadow_root_download, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath_download))).click()
    time.sleep(5)
    
    print(f"****{page+1}****")  


### need to be downloaded
df1 = pd.read_csv("Data/Elec_DownloadedReport_v2_AllInfoTab.csv", index_col=0)
df2 = pd.read_csv("Data/Elec_DownloadedReport_v2_AllInfoTab_add.csv", index_col=0)
df3 = pd.read_csv("Data/Elec_DownloadedReport_v2_AllInfoTab_add2.csv", index_col=0)

merge_df = pd.concat([df1, df2, df3])
merge_df = merge_df.drop_duplicates()

merge_df.columns = ['Code', 'Doc_Time', 'Country',
                     'Industry', "DCN"] 

def GetRID(text):
    match = re.search(r'\d+(?=\.pdf)', text)
    if match:
        number = match.group()
        return number
    else:
        number = ''
        return number

downloaded_file_list = glob('AnnualReport10K/*.pdf')
df_downloaded_file_list = pd.DataFrame(downloaded_file_list)
df_downloaded_file_list.columns = ['nake_name']
df_downloaded_file_list['DCN'] = df_downloaded_file_list['nake_name'].apply(GetRID)
df_downloaded_file_list = df_downloaded_file_list[['DCN']].drop_duplicates()
dump(df_downloaded_file_list, 'Data/df_downloaded_file_list.joblib')




  