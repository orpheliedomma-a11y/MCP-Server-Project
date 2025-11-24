def generate_itinerary(destination: str, days: int):
    from functions.get_weather_forecast import get_weather_forecast
    from functions.recommend_hotels import recommend_hotels

    weather = get_weather_forecast(city=destination)
    hotels = recommend_hotels(city=destination)

    itinerary = []
    for day in range(1, days + 1):
        itinerary.append({
            "day": day,
            "activities": [
                f"Explore major attractions in {destination}",
                "Try local cuisine",
                "Visit museums or parks",
                "Take a scenic evening walk"
            ]
        })

    return {
        "destination": destination,
        "days": days,
        "weather": weather,
        "hotel_recommendations": hotels,
        "itinerary": itinerary
    }