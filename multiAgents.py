# instructions=(
#         "persona, work"
#         "working condition , what you do in that condition"
#         "what not to do , tool suggestion to use always"
#     )

import os
from dotenv import load_dotenv
from agents import Runner,Agent,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
from rich import print

set_tracing_disabled(True)
load_dotenv()
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

shopping_agent=Agent(
    name="shopping_agent",
    instructions="you assist user to finding products and making purchase decisions",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    handoff_description="a shopping agent to help user in shopping"
)

support_agent=Agent(
    name="support_agent",
    instructions="you help user with post-purchase support and returns",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    handoff_description="a support agent to help user in post purchase queries"
)

triage_agent=Agent(
    name="triage_agent",
    instructions=(
        "you are a triage agent, you delegate task to appropiate agent"
        "when user asked for shopping related queries, youn always use given tools"
        "you never reply on your own,always use given tools to reply user"
    ),
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    tools=[
        shopping_agent.as_tool(
            tool_name="transfer_to_shopping_agent",
            tool_description="you assist user to finding products and making purchase decisions.always add this emoji ❤ in your reply ,start reply with this❤ emoji"
        ),
        support_agent.as_tool(
            tool_name="transfer_to_support_agent",
            tool_description="you help user with post-purchase support and return.always add this emoji ✔ in your reply ,start reply with this✔ emoji"
        )
    ]
)


result=Runner.run_sync(triage_agent,"i want to return a wristwatch")
print(result.final_output)