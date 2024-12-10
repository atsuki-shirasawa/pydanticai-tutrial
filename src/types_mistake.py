from dataclasses import dataclass

from pydantic_ai import Agent, RunContext


@dataclass
class User:
    name: str


agent = Agent(
    "test",
    deps_type=User,
    result_type=bool,
)


# agentで定義されたdeps_typeに定義された型(User)と、system_promptの引数の型(str)が一致しない
@agent.system_prompt
def add_user_name(ctx: RunContext[str]) -> str:
    return f"The user's name is {ctx.deps}."


def foobar(x: bytes) -> None:
    pass


result = agent.run_sync('Does their name start with "A"?', deps=User("Anne"))
foobar(result.data)
