from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from enterprise_rag.config import settings
from enterprise_rag.core.state import AgentState
from enterprise_rag.tools.knowledge_tools import tools

#Initialize LLM & Bind Tools

llm = ChatGoogleGenerativeAI(
    model = settings.LLM_MODEL_NAME,
    goole_api_key = settings.GOOGLE_API_KEY,
    temperature = 0
)
model_with_tools = llm.bind_tools(tools)

SYSTEM_PROMPT = (
    "You are an enterprise document QA assistant."
    "Always search internal knowledge base using 'search_internal_knowledge"
    "before answering specific company policy questions."
)

def call_model(state: AgentState):
    messages = [SystemMessage(content=SYSTEM_PROMPT), *state["messages"]]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("assistant", call_model)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")

    return builder.compile()

rag_graph = build_graph()