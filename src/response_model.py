"""Pydantic model example"""

import asyncio

from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()


async def main() -> None:
    """Main function"""
    agent = Agent("openai:gpt-4o-mini", result_type=int)

    result = await agent.run("長野オリンピックが開催された年は？")

    print(f"result: {result.data}, data-type: {type(result.data)}")


if __name__ == "__main__":
    asyncio.run(main())