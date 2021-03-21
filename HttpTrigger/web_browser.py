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
    s = '''Michael N, [20 Dec 2020 at 17:53:27]:
https://www.mysodexo.co.il/b?ewpzagqzlxICL_psS4

https://www.mysodexo.co.il/b?e_pG_sgcYgwignHZ4gl

Michael N, [21 Dec 2020 at 19:53:25]:
https://www.mysodexo.co.il/b?ek3mLZ_s0F2QeFd8o1

https://www.mysodexo.co.il/b?eG3EDb3UNUQstcWIz

Michael N, [22 Dec 2020 at 15:44:39]:
https://www.mysodexo.co.il/b?eQZRZii_smDJhDwAyC

https://www.mysodexo.co.il/b?em5mDh_sXr25SXttj0

Michael N, [28 Dec 2020 at 15:02:42]:
https://www.mysodexo.co.il/b?ev3unZdE3qBHvYaAj

https://www.mysodexo.co.il/b?emGmAd_sYljw3laaor'''
    for l in s.split('\n'):
        if len(l) > 0 and l.startswith('https://www.mysodexo.co.il/b'):
            text, image = get_text_and_screenshot(l)
            print(text)

