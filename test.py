from selenium_stealth import stealth
import undetected_chromedriver
import time


driver = undetected_chromedriver.Chrome()

stealth(driver,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        languages=["en-US", "en"],
        hairline="retina",
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url_bot = "https://bot.sannysoft.com/"
url = "https://gleam.io/cAnK8/winter-games-giveaway"
driver.get(url)
time.sleep(100)
