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
    s = '''
https://www.mysodexo.co.il/b?evGukddIA5mOjDexP
https://www.mysodexo.co.il/b?eendiaRQcIGBNOAJ6
https://www.mysodexo.co.il/b?ehHicZuoT3n_plBepH
https://www.mysodexo.co.il/b?eznzWYqAXlH35JbZn
https://www.mysodexo.co.il/b?e_pH_sgYZYUonPbJZRn
https://www.mysodexo.co.il/b?e4Z75gI_s1u5GFycqL
https://www.mysodexo.co.il/b?eyJzQgqb3koqnqOjq
https://www.mysodexo.co.il/b?eH6EHv3HKRZl3wTiD
https://www.mysodexo.co.il/b?edodumRjsLJYZ7Fau
https://www.mysodexo.co.il/b?ejmiWduAD1zLTXJwe
'''
    for l in s.split('\n'):
        if len(l) > 0:
            text, image = get_text_and_screenshot(l)
            print(text)

