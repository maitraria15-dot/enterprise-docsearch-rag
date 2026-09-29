"""Automated Performance, Tool Selection, & Accuracy Evaluation for Enterprise RAG Agent."""

import time
from langchain_core.messages import HumanMessage

# Import From your enterprise package module
from enterprise_rag.core.agent import rag_graph
from enterprise_rag.db.vectorstore import vector_manager

# Sample Enterprise Test Knowledge Base
TEST_DOCUMENTS = [
    ("Employees are allowed up to 20 days of paid annual leave per calendar year.", "Leave Policy 2026"),
    ("All expense reimbursement requests must be submitted within 30 days of purchase with receipts attached.", "Finance Policy"),
    ("Remote work is permiited up to 2 days per week with direct manager approval.", "Remote Work Policy")
]

# Evaluation test Suite (Query, Expected Tool, Required Keyword)
TEST_SUITE = [
    {"query": "How many days of remote work am I allowed?",
     "expected_tool": "search_internal_knowledge",
     "must_contain": "2 days"},
     {
         "query": "What is the deadline for submitting expense receipts?",
         "expected_tool": "search_internal_knowledge",
         "must_contain": "30 days"
     },
     {
         "query": "How many annual leave days do employess get?",
         "expected_tool": "search_internal_knowledge",
         "must_contain":"20 days"
     }
]

def seed_test_database():
    """Populates FAISS vector database with test policy documents."""
    print("=== 1. Initializing & seeding Vector Store ===")
    for content, source in TEST_DOCUMENTS:
        vector_manager.add_document(content=content, source_name=source)
    print("Knowledge base seeded successfully with test documents.\n")

def run_evaluation():
    """Run automated query evaluation against tool execution and response accuracy. """
    seed_test_database()

    print("=== 2. Running Automated Evaluation Suite ===")
    passed_count = 0

    for idx, test in enumerate(TEST_SUITE, start=1):
        print(F"\n[Test {idx}] Query: '{test['query']}'")
