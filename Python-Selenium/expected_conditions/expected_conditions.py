# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.implicitly_wait(5)
file = "file:///" + os.path.abspath("test.html")
driver.get(file)

# title_is(title) 判断title是否匹配，若完全匹配则返回True，否则返回False
title = EC.title_is('this is tite')
print(title(driver))

# alert_is_present 判断alert是否存在，若存在则切换到alert，若不存在则返回false
driver.find_element_by_id('button1').click()
alert = EC.alert_is_present()
if alert(driver):
    print(alert(driver).text)
    alert(driver).accept()
else :
    print('no alert')
    print(alert(driver))

# element_selection_state_to_be(element, is_selected) 判断某元素的选中状态是否与预期相同，相同则返回True，不同则返回False
checkbox = driver.find_element_by_id('checkbox1')
for n in range(2):
    checkbox.click()
    element = EC.element_selection_state_to_be(checkbox,True)
    print(element(driver))

#  element_located_to_be_selected(locator) 判断某元素是否被选中，locator为一个（by, path)元祖
locator = (By.ID, 'checkbox1')
for n in range(2):
    driver.find_element_by_id('checkbox1').click()
    element = EC.element_located_to_be_selected(locator)
    print(element(driver))

# element_to_be_clickable(locator) 判断某元素是否可访问并且可启用，比如能够点击，若可以则返回元素本身，否则返回False。locator为一个元祖(by, path)  
locator = (By.ID, 'button2')
locator2 = (By.XPATH, 'html/body/p')
element = EC.element_to_be_clickable(locator)
element2 = EC.element_to_be_clickable(locator2)
print('button2 result : ', element(driver))
print('<p> result : ', element2(driver))

# frame_to_be_available_and_switch_to_it(locator) 判断某个frame是否可以切换过去，若可以则切换，否则返回False
try :
    driver.find_element_by_id('kw').send_keys('test')
except Exception as msg:
    print('error is : ', msg)
finally:
    locator = (By.XPATH, 'html/body/iframe')
    element = EC.frame_to_be_available_and_switch_to_it(locator)
    if element(driver):
        driver.find_element_by_id('kw').send_keys('test')
        print('switch successed')
    else :
        print(element(driver))

# invisibility_of_element_located(locator) 判断某个元素是不是不可访问或者不存在在DOM树中,不存在则返回True，存在则返回True
locator = (By.ID, 'button4')
element = EC.invisibility_of_element_located(locator)
print(element(driver))

# new_window_is_opened(current_handles)  判断是否会打开新窗口，并且增加窗口句柄的数量
current_handles = driver.window_handles
new_window = EC.new_window_is_opened(current_handles)
print('before click, is there new window? ', new_window(driver))
driver.find_element_by_id('link').click()
new_window_2 = EC.new_window_is_opened(current_handles)
print('after click, is there new window? ',new_window_2(driver))

# number_of_windows_to_be(num_windows) 判断窗口数量是否是特定数值，是该数值则返回True，否则返回False
windows = EC.number_of_windows_to_be(2)
print('now there is 2 windows? ', windows(driver))
driver.find_element_by_id('link').click()
print('now there is 2 windows? ',windows(driver))

# presence_of_all_elements_located(locator) 判断定位的元素范围内，至少有一个元素存在于页面当中，存在则以数组形式返回元素本身，不存在则报错
locator = (By.CLASS_NAME, 'test')
element = EC.presence_of_all_elements_located(locator)
print(element(driver))

# staleness_of(element) 判断某个元素是否不再附加于于DOM树中，不再附加的话返回True，依旧存在返回False
element = EC.staleness_of(driver.find_element_by_id('p1'))
print(element(driver))
driver.find_element_by_id('button4').click()
print(element(driver))

# text_to_be_present_in_element(locator, text_)  判断给定文本是否出现在特定元素中，若存在则返回True，不存在返回False    
locator = (By.ID, 'p2')
element = EC.text_to_be_present_in_element(locator, 'para')
print(element(driver))

# text_to_be_present_in_element_value(locator, text_)  判断某文本是否是存在于特定元素的value值中，存在则返回True，不存在则返回False，对于查看没有value值的元素，也会返回False  
locator = (By.ID, 'p2')
element = EC.text_to_be_present_in_element_value(locator, 'para') 
print(element(driver)) 

# title_contains(title) 判断网页title是否包含特定文本，
element = EC.title_contains('This')
print(element(driver))

# title_is(title)  判断网页title是否是特定文本（英文区分大小写），若完全相同则返回True，否则返回False  
element = EC.title_is('this is title')
print(element(driver))

# url_changes(url)  判断网页是否更改了，若更改了则返回True，若没有更改则返回False
current_window = driver.current_window_handle
driver.find_element_by_id('link').click()
all_windows = driver.window_handles
for w in all_windows:
    if w != current_window:
        driver.switch_to_window(w)
element = EC.url_changes(file)
print(element(driver))

# url_contains(url)  判断网址是否包含特定文本（区分大小写），包含则返回True，不包含则返回False  
element = EC.url_contains('Test')
print(element(driver))

# url_matches(pattern) 判断网址是否符合特定格式，符合则返回True，不符合则返回False  
current_window = driver.current_window_handle
driver.find_element_by_id('link').click()
all_windows = driver.window_handles
for w in all_windows: # 利用for循环，切换到新窗口
    if w != current_window:
        driver.switch_to_window(w)
pattern = r'(https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
element = EC.url_matches(pattern)
print(element(driver))

# url_to_be(url)  判断网页是否为特定网页，是则返回True，否则返回False 
current_window = driver.current_window_handle
driver.find_element_by_id('link').click()
all_windows = driver.window_handles
for w in all_windows:
    if w != current_window:
        driver.switch_to_window(w)
url = 'https://www.baidu.com'
element = EC.url_to_be(url)
print(element(driver))
print(driver.current_url)

# visibility_of_element_located(element) 判断特定元素是否存在于DOM树中并且可，可访问意为元素的高和宽都大于0，元素存在返回元素本身 ，否则返回False  
locator = (By.ID, 'p2')
presence_element = EC.presence_of_element_located(locator)
visibility_element = EC.visibility_of_element_located(locator)
driver.find_element_by_id('button3').click()
print('presence result : ',presence_element(driver))
print('visibility result : ', visibility_element(driver))

# visibility_of(element)  判断特定元素是否存在于DOM树中并且可，可访问意为元素的高和宽都大于0，元素存在返回元素本身 ，否则返回False  
driver.find_element_by_id('button3').click()
element = EC.visibility_of(driver.find_element_by_id('p2'))
print(element(driver))

# visibility_of_all_elements_located(locator) 判断locator定位的所有元素都存在于DOM树中并且可见，可见意为元素高和宽都大于0,存在则以list形式返回元素，否则返回False   
locator = (By.TAG_NAME, 'p')
element = EC.visibility_of_all_elements_located(locator)
print(element(driver))
driver.find_element_by_id('button3').click()
print(element(driver))

# visibility_of_any_elements_located(locator) 判断locator定位的所有元素中，至少有一个存在于DOM树中并且可见，可见意为元素高和宽都大于0，存在则以list形式返回元素，否则返回False  
locator = (By.TAG_NAME, 'p')
driver.find_element_by_id('button3').click()
element = EC.visibility_of_any_elements_located(locator)
print(element(driver))
driver.quit()