import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

client=AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    name='Huzaifa',
    instructions='You are a helpful assistant',
    model=OpenAIChatCompletionsModel(
        model='deepseek/deepseek-r1:free',
        openai_client=client
    )
)

Result=Runner.run_sync(starting_agent=agent,input="do you think you can make agi a reality?")

print(Result.final_output)
