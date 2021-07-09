from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
from data import students
import time

# df = pd.read_excel('data.xlsx')
# dataframe = pd.read_excel('data.xlsx')


browser = webdriver.Chrome()
browser.get('http://nemis.education.go.ke/Learner/Listlearners.aspx')
LoginUserName = '//*[@id="ctl00_ContentPlaceHolder1_Login1_UserName"]'
LoginPassword = '//*[@id="ctl00_ContentPlaceHolder1_Login1_Password"]'
LoginBtn = '//*[@id="ctl00_ContentPlaceHolder1_Login1_LoginButton"]'
findMyLearners = '/html/body/div[2]/div[8]/form/div[3]/div[3]/ul/li[2]/ul/li[2]/a'

AddNewLearnerBtn = '//*[@id="ctl00_ContentPlaceHolder1_Button1"]'

#form
formFirstName = '//*[@id="ctl00_ContentPlaceHolder1_FirstName"]'
formLastName = '//*[@id="ctl00_ContentPlaceHolder1_Surname"]'
formBirthNo = '//*[@id="ctl00_ContentPlaceHolder1_Birth_Cert_No"]'
#use visibletext Grade 1
formDOB = '//*[@id="ctl00_ContentPlaceHolder1_DOB"]'
formMomId = '//*[@id="ctl00_ContentPlaceHolder1_txtMotherIDNo"]'
formMomName = '//*[@id="ctl00_ContentPlaceHolder1_txtMotherName"]'
formMomNumber = '//*[@id="ctl00_ContentPlaceHolder1_txtMothersContacts"]'
formDadId = '//*[@id="ctl00_ContentPlaceHolder1_txtFatherIDNO"]'
formDadName = '//*[@id="ctl00_ContentPlaceHolder1_txtFatherName"]'
formDadNumber = '//*[@id="ctl00_ContentPlaceHolder1_txtFatherContacts"]'

SubmitBtn = '//*[@id="ctl00_ContentPlaceHolder1_btnUsers"]'

browser.find_element_by_xpath(LoginUserName).send_keys('p3jy')
browser.find_element_by_xpath(LoginPassword).send_keys('lugulup3jy')
browser.find_element_by_xpath(LoginBtn).click()
# browser.find_element_by_xpath('//*[@id="Menu1"]/li[2]/a').click()
browser.get('http://nemis.education.go.ke/Learner/Listlearners.aspx')
browser.find_element_by_xpath(AddNewLearnerBtn).click()

if browser.find_element_by_xpath(AddNewLearnerBtn):
    time.sleep(2)
    for i in students:
        entry = i
        firstname = browser.find_element_by_xpath(formFirstName)
        firstname.clear()
        firstname.send_keys(entry['formFirstName'])

        lastname = browser.find_element_by_xpath(formLastName)
        lastname.clear()
        lastname.send_keys(entry['formLastName'])

        birthno = browser.find_element_by_xpath(formBirthNo)
        birthno.clear()
        birthno.send_keys(entry['formBirthNo'])

        dob = browser.find_element_by_xpath(formDOB)
        dob.clear()
        dob.send_keys(entry['formDOB'])

        grade = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlClass"]/option[5]')
        grade.click()
        if entry['formGender'] == 'M':
            gender = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Gender"]/option[2]')
            gender.click()
        else:
            gender = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_Gender"]/option[3]')
            gender.click()
        browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlmedicalcondition"]/option[7]').click()

        browser.find_element_by_xpath('//*[@id="home"]/div[9]/div[2]/div/label[2]').click()
        browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlcounty"]/option[4]').click()
        time.sleep(6)
        browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlsubcounty"]/option[4]').click()
        
        motherid = browser.find_element_by_xpath(formMomId)
        motherid.clear()
        motherid.send_keys(entry['formMomId'])

        momname = browser.find_element_by_xpath(formMomName)
        momname.clear()
        momname.send_keys(entry['formMomName'])

        momnumber = browser.find_element_by_xpath(formMomNumber)
        momnumber.clear()
        momnumber.send_keys(entry['formMomNumber'])

        dadname = browser.find_element_by_xpath(formDadName)
        dadname.clear()
        dadname.send_keys(entry['formDadName'])

        dadid = browser.find_element_by_xpath(formDadId)
        dadid.clear()
        dadid.send_keys(entry['formDadId'])

        dadnumber = browser.find_element_by_xpath(formDadNumber)
        dadnumber.clear()
        dadnumber.send_keys(entry['formDadNumber'])

        browser.find_element_by_xpath(SubmitBtn).click()
        time.sleep(4)


# for i in dataframe.index:
#     entry = dataframe.iloc[i]

#     firstName = browser.find_element_by_xpath(formFirstName)
#     firstName.send_keys(entry['First Name'])

#     secondName = browser.find_element_by_xpath(formLastName)
#     secondName.send_keys(entry['Last name'])

#     gender_xpath = f"//input[@name=\"gender\"][@value=\"{entry['Gender']}\"]"
#     gender_input = browser.find_element_by_xpath(gender_xpath)
#     gender_input.click()

    

#     status_select = Select(browser.find_element_by_name('workingstatus'))
#     status_select.select_by_value(entry['Working Status'])

#     print('Sleeping for 5 seconds before submitting...')
#     time.sleep(3)

#     # email_input.submit()

#     submit_btn = browser.find_element_by_css_selector('input[type="submit"]')
#     browser.execute_script("return arguments[0].click()", submit_btn)

#     time.sleep(2)
