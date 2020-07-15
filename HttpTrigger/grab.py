from selenium import webdriver


def get_screenshot(url: str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
    driver.get(url)
    # links = driver.find_elements_by_tag_name("a")
    # link_list = ""
    # for link in links:
    #     if link_list == "":
    #         link_list = link.text
    #     else:
    #         link_list = link_list + ", " + link.text

    driver.get_screenshot_as_png()
    return driver.get_screenshot_as_png()


if __name__ == '__main__':
    get_screenshot('https://www.google.com/')
