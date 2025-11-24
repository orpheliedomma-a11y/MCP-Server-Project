from dotenv import load_dotenv
from fastmcp import FastMCP

from functions.generate_itinerary import generate_itinerary
from functions.get_weather_forecast import get_weather_forecast
from functions.recommend_hotels import recommend_hotels

load_dotenv()

app = FastMCP("travel-itinerary-mcp")

# Register tools by passing the function directly
app.tool(generate_itinerary)
app.tool(get_weather_forecast)
app.tool(recommend_hotels)

if __name__ == "__main__":
    app.run(
        transport="sse",      # REQUIRED for network server
        host="0.0.0.0",
        port=8080
    )