import asyncio
from playwright.async_api import async_playwright

async def validate():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        errors = []
        page.on("console", lambda msg: errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(f"Page error: {e}"))

        await page.goto("file:///workspace/landasan-digital/index.html")
        await page.wait_for_load_state("networkidle")

        hero = await page.query_selector(".hero")
        nav = await page.query_selector(".nav")
        footer = await page.query_selector(".footer")

        print(f"Hero section: {'OK' if hero else 'MISSING'}")
        print(f"Navigation: {'OK' if nav else 'MISSING'}")
        print(f"Footer: {'OK' if footer else 'MISSING'}")

        if errors:
            print("\nErrors found:")
            for e in errors:
                print(f"  - {e}")
        else:
            print("\nNo console errors!")

        await browser.close()

asyncio.run(validate())
