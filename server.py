# server.py
from mcp.server.fastmcp import FastMCP
import networkx as nx
from mock_data import mock_carriers, mock_locations, mock_disruptions

# Initialize the MCP Server
mcp = FastMCP("LogisticsTMS")

@mcp.tool()
def get_carrier_rates() -> str:
    """Returns the list of available carriers, their rate per mile, and reliability score."""
    return str(mock_carriers)

@mcp.tool()
def check_route_disruptions(location: str) -> str:
    """Checks if a specific transit hub has an active weather or traffic disruption."""
    for disruption in mock_disruptions:
        if disruption["location"].lower() == location.lower():
            return f"ALERT: {disruption['reason']} in {location}. Delay: {disruption['delay_hours']} hours. Rerouting recommended."
    return f"Clear: No disruptions reported for {location}."

@mcp.tool()
def calculate_transit_time_and_cost(path_nodes: list[str], carrier_name: str) -> str:
    """Calculates the total mileage, estimated cost, and transit time for a given route and carrier."""
    if carrier_name not in mock_carriers:
        return f"Error: Carrier {carrier_name} not found."
    
    # Build the transit graph
    G = nx.Graph()
    for city, connections in mock_locations.items():
        for connected_city, distance in connections.items():
            G.add_edge(city, connected_city, weight=distance)
    
    total_distance = 0
    try:
        # Calculate distance across the provided nodes
        for i in range(len(path_nodes) - 1):
            total_distance += G[path_nodes[i]][path_nodes[i+1]]['weight']
    except KeyError:
        return "Error: Invalid route path. One or more connections do not exist."

    rate = mock_carriers[carrier_name]["rate_per_mile"]
    total_cost = total_distance * rate
    transit_hours = total_distance / 50  # Assuming 50mph average speed

    return f"Route: {' -> '.join(path_nodes)} | Distance: {total_distance} mi | Time: {transit_hours} hrs | Cost: ${total_cost:.2f}"

if __name__ == "__main__":
    # Runs the server using standard input/output streams for the client to attach to
    mcp.run(transport="stdio")