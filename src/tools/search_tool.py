from langchain_core.tools import tool
from tavily import TavilyClient
import os


@tool
def search_stellar_cartography(query: str) -> str:
    """Access the stellar cartography database to search for current information.
    
    Use this tool when you need:
    - Current events or recent information
    - Facts you don't have in your knowledge base
    - Real-time data
    
    Args:
        query: The search query
        
    Returns:
        Search results with relevant information
    """
    try:
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = client.search(query, max_results=3)

        # Format the results
        results = []
        for result in response.get("results", []):
            title = result.get("title", "No Title")
            content = result.get("content", "No Content")
            url = result.get("url", "No URL")
            results.append(f"Title: {title}\nContent: {content}\nURL: {url}\n")
        return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Error accessing Stellar Cartography Database: {str(e)}"