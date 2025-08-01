import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,function_tool,WebSearchTool,FileSearchTool
from rich import print
load_dotenv()
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

@function_tool
def get_name(dummy: str = "ignored")->str:
    """Get my name."""

    return "My name is aman."


client=AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    name='agent',
    instructions='You are a helpful assistant',
    model=OpenAIChatCompletionsModel(
        model='mistralai/mistral-small-24b-instruct-2501',
        openai_client=client
    ),
    tools=[get_name,
           WebSearchTool(),
           FileSearchTool(
               max_num_results=3,
               vector_store_ids=""
           )]
)


result = Runner.run_sync(agent, "Who is the prime minister of pakistan?")
print(result.final_output)

