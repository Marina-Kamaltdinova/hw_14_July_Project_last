import allure
import os


def screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )


def html(browser):
    source_html = browser.driver.page_source
    allure.attach(
        body=source_html,
        name='page_source',
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )


def video(browser):
    selenoid = os.getenv('SELENOID_URL')
    video_url = f"https://{selenoid}/video/" + browser.driver.session_id + ".mp4"
    html_markup = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
                  + video_url \
                  + "' type='video/mp4'></video></body></html>"
    allure.attach(
        body=html_markup,
        name='video_' + browser.driver.session_id,
        attachment_type=allure.attachment_type.HTML,
        extension='.html')
