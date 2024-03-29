#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:55:33 2023

@author: lichao
"""

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

### need to be downloaded
DCN_list = load('Data/df_downloaded_file_list.joblib')
DCN_list = DCN_list['DCN'].to_list()

DCN_have_first = pd.read_csv("Data/Elec_DownloadedReport_EleUt_V2.csv",
                             index_col=0)
DCN_have_first.columns = ['X1', 'X2', 'X3', 'X4', 'DCN']
DCN_have_first = DCN_have_first['DCN'].to_list()

DCN_have_second = pd.read_csv("Data/Elec_DownloadedReport_EleUt_V2_second.csv",
                             index_col=0)
DCN_have_second.columns = ['X1', 'X2', 'X3', 'X4', 'DCN']
DCN_have_second = DCN_have_second['DCN'].to_list()

DCN_have_third = pd.read_csv("Data/Elec_DownloadedReport_EleUt_V2_third.csv",
                             index_col=0)
DCN_have_third.columns = ['X1', 'X2', 'X3', 'X4', 'DCN']
DCN_have_third = DCN_have_third['DCN'].to_list()
        
DCN_list = DCN_have_first + DCN_have_second + DCN_list + DCN_have_third

data_info = []
fail_array = []

for page in list(range(14)):
    for batch in list(range(10)):
        for row_number in list(range(1,21)):
            shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
            shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
            element_within_shadow_css = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(12) > div:nth-child({row_number}) > button > span'
            element_within_shadow = WebDriverWait(shadow_root, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_within_shadow_css)))
            element_text_DCN = element_within_shadow.text
            try:
                if int(element_text_DCN) in DCN_list:
                    print(element_text_DCN)
                    time.sleep(1)
                else:
                    shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
                    shadow_root = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath))).shadow_root
                    element_within_shadow_xpath = f'#section0 > div.tr-lg > div.grid-pane.columns > div > div:nth-child(4) > div:nth-child({row_number}) > button > div > app-icon:nth-child(2) > coral-icon'
                    WebDriverWait(shadow_root, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath))).click()
                    time.sleep(300)
                    
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
                    
                    shadow_host_xpath_download = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[2]/app-sidebar/div/app-doc-viewer/carbon-sidebar-layout/div/lib-document-viewer/lib-pdf-viewer-wrapper/div/coral-panel[1]/coral-button[1]"
                    shadow_root_download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath_download))).shadow_root
                    element_within_shadow_xpath_download = '#icon'
                    WebDriverWait(shadow_root_download, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath_download))).click()
                    time.sleep(10)
                    
                    #print(element_text_company_name)
                    #print(element_text_filing_date)
                    #print(stock_name)
                    
                    info = [stock_name, element_text_doc_date, 
                            element_text_country, element_text_industry,
                            element_text_DCN]
                    data_info.append(info)
                    print(info)
                    
                    df = pd.DataFrame(data_info)
                    df.to_csv("Data/Elec_DownloadedReport_EleUt_V2_fourth.csv")
            except:
                print(page, batch, row_number)
                fail_array.append([page, batch, row_number])
                fail_df = pd.DataFrame(fail_array)
                fail_df.to_csv("Data/Elec_DownloadedReport_EleUt_V2_fail_fourth.csv")
        
        shadow_host_xpath = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/emerald-grid"
        shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath)))
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        scrollable_element_selector = 'div.grid-scrollbar.grid-vscroll.grid-scroll-fadeout'
        scrollable_element = shadow_root.find_element(By.CSS_SELECTOR, scrollable_element_selector)
        driver.execute_script("arguments[0].scrollTop += 700;", scrollable_element)
        time.sleep(2)
        
    shadow_host_xpath_download = "/html/body/app-root/app-industry-view/carbon-sidebar-layout/div/carbon-sidebar-layout/div[1]/app-main-grid/coral-panel/app-emerald-grid/div/span/emerald-pagination"
    shadow_root_download = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, shadow_host_xpath_download))).shadow_root
    element_within_shadow_xpath_download = '#next'
    WebDriverWait(shadow_root_download, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_within_shadow_xpath_download))).click()
    time.sleep(10)
    
    print(f"****{page+1}****")





