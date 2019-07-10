from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import captions as Captions

def hello(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)

    transcript = Captions.getTranscript("yBBJgFQxUlg",driver)
    timestamps = Captions.getTimestamps(transcript,"Skillshare")

    driver.close()
    driver.quit()

    response = {
        "statusCode": 200,
        "Transcripts": transcript,
        "Timestamps": timestamps
    }

    return response
