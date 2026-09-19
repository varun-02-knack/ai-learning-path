"""
Multi-agent parallel fan-out demo.

Mirrors the sync vs async lesson: independent I/O-bound agents should
run concurrently, not one after another. Total wall-clock time should
be bounded by the slowest agent, not the sum of all agents.
"""

import asyncio
import time


async def agent_a_call_llm() -> dict:
    """Simulates an LLM call. I/O-bound -> ~4s of waiting, not computing."""
    print("[Agent A] Calling LLM...")
    await asyncio.sleep(4)
    print("[Agent A] LLM responded")
    return {"agent": "A", "task": "llm_call", "result": "summary generated"}


async def agent_b_call_tool_api() -> dict:
    """Simulates a tool/API call. I/O-bound -> ~7s of waiting."""
    print("[Agent B] Calling tool API...")
    await asyncio.sleep(7)
    print("[Agent B] Tool API responded")
    return {"agent": "B", "task": "tool_api_call", "result": "action executed"}


async def agent_c_query_db() -> dict:
    """Simulates a database query. I/O-bound -> ~3s of waiting."""
    print("[Agent C] Querying DB...")
    await asyncio.sleep(3)
    print("[Agent C] DB query returned")
    return {"agent": "C", "task": "db_query", "result": "rows fetched"}


async def orchestrator() -> list[dict]:
    """
    Fans out to independent agents concurrently, then joins/merges
    their results once all have completed.
    """
    print("[Orchestrator] Dispatching agents A, B, C in parallel...\n")

    results = await asyncio.gather(
        agent_a_call_llm(),
        agent_b_call_tool_api(),
        agent_c_query_db(),
    )

    print("\n[Orchestrator] All agents done. Merging results...")
    return results


async def main() -> None:
    start_time = time.time()

    merged_results = await orchestrator()

    end_time = time.time()

    print("\nMerged results:")
    for r in merged_results:
        print(f"  - {r}")

    print(f"\nTotal time: {end_time - start_time:.2f}s (expected ~7s, "
          f"bounded by the slowest agent, not 4+7+3=14s)")


if __name__ == "__main__":
    asyncio.run(main())