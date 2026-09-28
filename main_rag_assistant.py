import sys
from langchain_core.messages import HumanMessage
from enterprise_rag.core.agent import rag_graph

def run_cli():
    print("=== Enterprise RAG Agent CLI ===")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input or user_input.lower() == "exit":
                break

            response = rag_graph.invoke({"messages": [HumanMessage(content=user_input)]})
            latest_msg = response["messages"][-1].content
            print(f"\nAssistant: {latest_msg}\n")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run_cli()