import pytest

from selenium import webdriver

from selenium.webdriver.common.proxy import Proxy, ProxyType

@pytest.fixture
def driver(request):
    #wd = webdriver.Ie()
    #wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Firefox Developer Edition\\firefox.exe", desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})
    #wd = webdriver.Chrome()
    #wd = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpsProxy": "127.0.0.1:8888"}})
    #wd = webdriver.Firefox()
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = "127.0.0.1:8888"
    prox.socks_proxy = "127.0.0.1:8888"
    prox.ssl_proxy = "127.0.0.1:8888"

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    wd = webdriver.Chrome(desired_capabilities=capabilities)
    request.addfinalizer(wd.quit)


    return wd

def test_proxy(driver):
    driver.delete_all_cookies()
    driver.get("https://ya.ru")

