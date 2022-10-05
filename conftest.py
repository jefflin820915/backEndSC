import pytest
import os
import threading
from common import connectSQL
from common import loadYaml
from datetime import datetime
from py._xmlgen import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 主大類
#  - 分py
#  - 名稱先以 Test_Case_Home、Test_Case_Sport.....為命名
#  - 類名 = py檔名
#  - pytest開頭需添加Test_
#
# 測試案例模組
#  - 分方法
#  - 方法名=模組名稱, test_Home_Header_Home....為命名
#  - pytest開頭需添加test_
#
# 執行用例
# - 執行全部用例
#   - pytest
# - 執行特定方法用例
#   - pytest PyFileName.py::ClassName::MethodName
# - 執行特定類用例
#   - pytest PyFileName.py::ClassName
# - 執行特定py檔用例
#   - pytest PyFileName.py
# - 執行全部用例並生成報告
#   - pytest --html=report.html --self-contained-html
# - 執行特定方法用例並生成報告
#   - pytest --html=report.html --self-contained-html PyFileName.py::ClassName::MethodName
# - 執行特定類用例並生成報告
#   - pytest --html=report.html --self-contained-html PyFileName.py::ClassName
# - 執行特定py檔用例並生成報告
#   - pytest --html=report.html --self-contained-html PyFileName.py

driver = None
threadLocal = threading.local()
load_yaml = loadYaml.loadYaml()

@pytest.fixture()
def driver(request):
    global driver
    driver = getattr(threadLocal, 'driver', None)
    if driver is None:
        chrome_options = Options()
        # todo : download位置,位置解決, 把路徑設成變數或常數
        prefs = {"download.default_directory": os.path.abspath(os.path.join(os.getcwd(), os.path.pardir, load_yaml['FolderPath']['download'])), "download.prompt_for_download": False,
                 "profile.default_content_setting_values.automatic_downloads": 1, 'profile.default_content_settings.popups': 0}
        chrome_options.add_experimental_option("prefs", prefs)
        # 以下為關閉設置, 提升執行速度,效能
        # 圖形化開關, 註解掉 == 開
        # chrome_options.add_argument("blink-settings=imagesEnabled=false")
        # 禁用javaScript
        # chrome_options.add_argument('--disable-javascript')
        # 瀏覽器開啟關閉 註解掉 == 開
        # chrome_options.add_argument("headless")
        # 無痕模式
        # chrome_options.add_argument('--incognito')
        # 隱藏滾動條
        # chrome_options.add_argument('--hide-scrollbars')
        # 關閉"瀏覽器正在被自動化程序控制"的提示
        # chrome_options.add_argument('--disable-infobars')
        # 禁用瀏覽器擴展
        chrome_options.add_argument("--disable-extensions")
        # 禁用GPU加速
        chrome_options.add_argument("--disable-gpu")
        # Disables the use of a 3D software rasterizer
        chrome_options.add_argument("--disable-software-rasterizer")
        # Disables the sandbox for all process types that are normally sandboxed. Meant to be used as a browser-level switch for testing purposes only
        chrome_options.add_argument('--no-sandbox')
        # 禁用擴展插件並實現窗口最大化
        chrome_options.add_argument('--ignore-certificate-errors')
        # 允許運行不安全內容
        chrome_options.add_argument('--allow-running-insecure-content')
        chromeService = ChromeDriverManager().install()
        driver = webdriver.Chrome(chromeService, chrome_options=chrome_options)
        driver.get(load_yaml['WebsiteURL']['SC_BackEnd'])
        driver.set_window_size(1680, 1280)
        driver.implicitly_wait(20)

        yield driver
        driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screenshot = _capture_screenshot()
            if file_name:
                pytst_html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:258;height:512px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot
                extra.append(pytest_html.extras.html(pytst_html))
        report.extra = extra
        report.description = str(item.function.__doc__)

def _capture_screenshot():
    '''
    截圖保存
    :return:
    '''
    return driver.get_screenshot_as_base64()

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名稱'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "Selenium+pytest"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists('../reports'):
        os.makedirs('../reports')
    config.option.htmlpath = '../reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"