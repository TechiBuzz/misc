import os

import httpx

async def get_city_location(city_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
        "https://dataservice.accuweather.com/locations/v1/cities/search",
        headers={
            "authorization": f"Bearer {os.environ.get('WEATHER_API_KEY')}",
        },
        params={
            "q": f"{city_name}"
        }
        )

        if response.status_code == 200:
            result = response.json()
            if result:
                return result[0]["Key"]

    return None