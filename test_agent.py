from src.agents.graph import starfleet_agent

def main():
    print("🖖 Starfleet Computer Online")
    print("Type 'exit' to quit\n")

    # Create a thread ID for this conversation session
    thread_id = "enterprise-bridge-001"  # ← Add this

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {'exit', 'quit'}:
            print("Shutting down Starfleet Computer. Live long and prosper! 🖖")
            break

        if not user_input:
            continue

        try:
            # Invoke the agent with thread_id for memory
            response = starfleet_agent.invoke({
                "messages": [("user", user_input)]},
                config={"configurable": {"thread_id": thread_id}}
            )

           # Get the last message (agent's response) 
            agent_response = response["messages"][-1].content
            print(f"Starfleet Computer:: {agent_response}\n")

        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()