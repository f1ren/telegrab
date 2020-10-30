from selenium import webdriver


def get_text_and_screenshot(url: str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
    driver.get(url)
    text = driver.find_element_by_tag_name("body").text.strip()

    return text, driver.get_screenshot_as_png()


if __name__ == '__main__':
    s = ''''''
    for l in s.split('\n'):
        if len(l) > 0 and l.startswith('https://www.mysodexo.co.il/b'):
            text, image = get_text_and_screenshot(l)
            print(text)

