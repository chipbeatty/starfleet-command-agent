from src.agents.graph import starfleet_agent

def main():
    print("🖖 Starfleet Computer Online")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You:: ").strip()

        if user_input.lower() in {'exit', 'quit'}:
            print("Shutting down Starfleet Computer. Live long and prosper! 🖖")
            break

        if not user_input:
            continue

        try:
            # Invoke the agent
            response = starfleet_agent.invoke({
                "messages": [("user", user_input)]
            })

           # Get the last message (agent's response) 
            agent_response = response["messages"][-1].content
            print(f"Starfleet Computer:: {agent_response}\n")

        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()