"""
Multi-agent sequential (sync) demo.

Same three agents as the async version, but run one after another.
Total wall-clock time is the SUM of all agents, not bounded by the
slowest one. This is the baseline the async version improves on.
"""

import time


def agent_a_call_llm() -> dict:
    """Simulates an LLM call. Blocking -> ~4s of waiting."""
    print("[Agent A] Calling LLM...")
    time.sleep(4)
    print("[Agent A] LLM responded")
    return {"agent": "A", "task": "llm_call", "result": "summary generated"}


def agent_b_call_tool_api() -> dict:
    """Simulates a tool/API call. Blocking -> ~7s of waiting."""
    print("[Agent B] Calling tool API...")
    time.sleep(7)
    print("[Agent B] Tool API responded")
    return {"agent": "B", "task": "tool_api_call", "result": "action executed"}


def agent_c_query_db() -> dict:
    """Simulates a database query. Blocking -> ~3s of waiting."""
    print("[Agent C] Querying DB...")
    time.sleep(3)
    print("[Agent C] DB query returned")
    return {"agent": "C", "task": "db_query", "result": "rows fetched"}


def orchestrator() -> list[dict]:
    """
    Dispatches agents one at a time. Each agent must finish before
    the next one starts.
    """
    print("[Orchestrator] Dispatching agents A, B, C sequentially...\n")

    results = []
    results.append(agent_a_call_llm())
    results.append(agent_b_call_tool_api())
    results.append(agent_c_query_db())

    print("\n[Orchestrator] All agents done. Merging results...")
    return results


def main() -> None:
    start_time = time.time()

    merged_results = orchestrator()

    end_time = time.time()

    print("\nMerged results:")
    for r in merged_results:
        print(f"  - {r}")

    print(f"\nTotal time: {end_time - start_time:.2f}s (expected ~14s, "
          f"since 4+7+3=14, no overlap between agents)")


if __name__ == "__main__":
    main()