from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import captions as Captions
import json

def hello(event, context):

    print('[event]',event['queryStringParameters'])

    params = event['queryStringParameters']
    video_id = params['videoID']
    client = params['client']

    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)

    transcript = Captions.getTranscript(video_id,driver)
    timestamps = Captions.getTimestamps(transcript,client)

    driver.close()
    driver.quit()

    body = {
        "Transcripts": transcript,
        "Timestamps": timestamps
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
