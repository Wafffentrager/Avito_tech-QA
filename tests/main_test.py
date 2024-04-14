import os

from playwright.sync_api import sync_playwright

output_path = "output"

if not os.path.exists(output_path):
    os.makedirs(output_path)


def test_counters():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        co2_counter = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кг CO₂'))"
        page.wait_for_selector(co2_counter)
        page.locator(co2_counter).screenshot(path=f"{output_path}/TC1-Счетчик CO2.png")

        water_counter = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('л воды'))"
        page.wait_for_selector(water_counter)
        page.locator(water_counter).screenshot(path=f"{output_path}/TC2-Счетчик воды.png")

        energy_counter = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кВт⋅ч энергии'))"
        page.wait_for_selector(energy_counter)
        page.locator(energy_counter).screenshot(path=f"{output_path}/TC3-Счетчик энергии.png")

        browser.close()


test_counters()
