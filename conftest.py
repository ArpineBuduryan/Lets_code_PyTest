import os
import logging
import pytest
from datetime import datetime
from selenium import webdriver


@pytest.fixture(autouse=True)
def get_driver():
    # Run Chrome in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    #Open a visible browser window and maximize it
   
    yield driver
    driver.quit()


@pytest.fixture()
def test_logger(request):
    today_date = datetime.today().date()
    os.makedirs(f"logs_{today_date}", exist_ok=True)

    test_name = request.node.name
    log_path = f"logs_{today_date}/{test_name}.log"

    logging.basicConfig(
        filename=log_path,
        filemode="w+",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )
    logging.info(f"{test_name} is started")
    yield logging
    logging.info(f"{test_name} is finished")