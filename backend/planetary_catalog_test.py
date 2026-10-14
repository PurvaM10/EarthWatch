
from builtins import enumerate, print

from pystac_client import Client
import planetary_computer

# Public Microsoft Planetary Computer STAC API
STAC_URL = "https://planetarycomputer.microsoft.com/api/stac/v1"

# Hingna, Nagpur: [west, south, east, north]
HINGNA_BBOX = [78.965, 21.095, 79.005, 21.135]

catalog = Client.open(
    STAC_URL,
    modifier=planetary_computer.sign_inplace,
)

def search_scenes(label, start_date, end_date):
    print(f"\n{'=' * 55}")
    print(f"{label}: {start_date} to {end_date}")
    print("=" * 55)

    search = catalog.search(
        collections=["sentinel-2-l2a"],
        bbox=HINGNA_BBOX,
        datetime=f"{start_date}/{end_date}",
        query={"eo:cloud_cover": {"lt": 80}},
        max_items=100,
    )

    items = list(search.items())
    items.sort(key=lambda item: item.datetime or "")

    print(f"Scenes found: {len(items)}")

    for index, item in enumerate(items, start=1):
        date = item.datetime
        cloud = item.properties.get("eo:cloud_cover", "N/A")
        print(f"{index}. Date: {date} | Cloud cover: {cloud}%")

    return items


if __name__ == "__main__":
    search_scenes("BEFORE", "2022-01-01", "2022-03-31")
    search_scenes("AFTER", "2025-01-01", "2025-06-30")
