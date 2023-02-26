from selenium import webdriver

# specify the path to the webdriver
driver = webdriver.Firefox(executable_path='path/to/webdriver')

# navigate to the webpage
driver.get('certificate.html')

# save a screenshot of the webpage
driver.save_screenshot('certificate.jpg')

# close the browser
driver.close()
