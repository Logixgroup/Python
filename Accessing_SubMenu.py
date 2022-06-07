from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\Arvind.Kumar\\Desktop\\chromedriver\\chromedriver.exe")
driver.get("https://www.keysight.com/in/en/home.html")
product_services=driver.find_element(by=By.XPATH,value="//div[@id='gnavbar']/div/ul/li[1]/a[@href='/in/en/products.html']")
product_list=driver.find_element(by=By.XPATH,value="/html//div[@id='gnavbar']/div/ul/li[1]/div/div/ul")
def count_sublists(key):
    """
    :param key: key is the menu
    :return: True on success, else false
    """
    try:
        product_services = driver.find_element(by=By.XPATH,
                                               value="//div[@id='gnavbar']/div/ul/li[1]/a[@href='/in/en/products.html']")
        product_services.click()
        main_menu = driver.find_elements(by=By.XPATH, value="/html//div[@id='gnavbar']/div/ul/li[1]/div/div/ul/li/a")
        start_locator="//*[@id='gnavbar']/div/ul/li[1]/div/div/ul//li["
        end_element="]/div/ul/li/a"
        for menu in main_menu:
            if key == menu.get_attribute("data-value"):
                i = main_menu.index(menu)
                menu.click()
                sub_menu = driver.find_elements(by=By.XPATH, value=start_locator + str(i+1) + end_element)
                print("Total sublist menu items count for-->", key, "is", len(sub_menu), "\n")
                print("Passed key/menu: ", key)
                for each_menu in sub_menu:
                    print("corresponding submenu's are:", each_menu.get_attribute("data-value"))
                return True
        else:
            print("Invalid key given")
            return False
    except Exception as err:
        print("Exception caught".format(err))
        return False
#Call below in Test case based on different keys
count_sublists(key="Meters")
