import os
from agents import Runner,Agent,OpenAIChatCompletionsModel,set_tracing_disabled,AsyncOpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
set_tracing_disabled(disabled=True)

client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

agent=Agent(
    name="Huzaifa",
    instructions="You are an helpful assistant",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
    )
)


result=Runner.run_sync(starting_agent=agent,input="hi")
print(result.final_output)