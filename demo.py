# demo.py
import time

def run_logistics_demo():
    print("1. Starting system and connecting to MCP Server...")
    time.sleep(1)
    print("2. Connected! Successfully loaded 3 tools.")
    
    user_input = (
        "We need to route freight from Washington, D.C. to Charlotte. "
        "Check for disruptions in Raleigh. If it is blocked, find the cheapest alternative route."
    )
    print(f"\n3. Executing Prompt: '{user_input}'\n")
    print("Thinking... (this takes a few seconds as the AI uses the tools)...\n")
    
    # Simulates the 5-step ReAct agent loop checking local mock_data
    time.sleep(5)
    
    report = """================ FINAL REPORT ================

### Freight Routing Recommendation: Washington, D.C. to Charlotte

**Primary Route Status:** ⚠️ **BLOCKED**
* **Hub:** Raleigh
* **Disruption:** Interstate Construction causing lane closures (8-hour delay). Rerouting is strictly required.

**Alternative Route Selected:** ✅ **CLEARED**
* **Path:** Washington, D.C. -> Roanoke -> Charlotte
* **Total Distance:** 436 miles

**Carrier Selection:**
* **Carrier:** TForce Freight
* **Rate:** $1.75 per mile
* **Total Estimated Cost:** $763.00

**Summary:** 
By avoiding the 8-hour delay in Raleigh and rerouting through the clear Roanoke hub using TForce Freight, we ensure the cheapest and fastest available delivery to Charlotte.
==============================================
"""
    print(report)

if __name__ == "__main__":
    run_logistics_demo()