import os

from playwright.sync_api import sync_playwright, Route
from src.responses import generate_response

output_path = "output"

if not os.path.exists(output_path):
    os.makedirs(output_path)

URL = "https://www.avito.ru/avito-care/eco-impact"


def test_counters():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)

        co2_counter = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кг CO₂'))"
        page.wait_for_selector(co2_counter)
        page.locator(co2_counter).screenshot(path=f"{output_path}/TC1_1-Счетчик CO2.png")

        water_counter = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('л воды'))"
        page.wait_for_selector(water_counter)
        page.locator(water_counter).screenshot(path=f"{output_path}/TC1_2-Счетчик воды.png")

        energy_counter = ".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кВт⋅ч энергии'))"
        page.wait_for_selector(energy_counter)
        page.locator(energy_counter).screenshot(path=f"{output_path}/TC1_3-Счетчик энергии.png")

        browser.close()


def test_response():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        replaceable_responses = [
            generate_response(co2=1, energy=100, water=900),
            generate_response(co2=1000, energy=1000, water=1000),
            generate_response(co2=1000000, energy=1000000, water=1000000),
            generate_response(co2=1000000000, energy=1000000000, water=1000000000)
        ]

        for index, value in enumerate(replaceable_responses):
            def change_response(route: Route):
                route.fulfill(
                    body=value
                )

            page.route("**/web/1/charity/ecoImpact/init", change_response)
            page.goto(URL)

            load_counter = page.locator(".desktop-impact-items-F7T6E")
            load_counter.wait_for()

            screenshot_path = {"path": os.path.join("output", f"TC2_{index + 1}.png")}
            load_counter.screenshot(**screenshot_path)

        context.close()
        browser.close()


test_counters()
