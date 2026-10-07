from celery import shared_task
from playwright.sync_api import sync_playwright

from .models import Vehicle

@shared_task
def complete_vechile_data(licence_plate):
    url = 'https://pycodebr.com.br/placas-carros/'

    brand = None
    mode = None
    color = None

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('table')
        xpath_expression = f"//table//tr[td[1][normalize-space() ='{licence_plate}']]"
        row = page.query_selector(xpath_expression)
        if row:
            cells = row.query_selector_all('td')
            brand = cells[1].inner_text().strip()
            mode = cells[2].inner_text().strip()
            color = cells[3].inner_text().strip()
        browser.close()

    if brand and mode and color:
        Vehicle.objects.filter(
            licence_plate=licence_plate
        ).update(
            brand=brand,
            model=mode,
            color=color
        )