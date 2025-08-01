import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

agent = Agent(
    name='Huzaifa',
    instructions='you are an helpful assistant',
    model=OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=client
    ),
)

query=input("User:   ")
Result=Runner.run_sync(starting_agent=agent,input=query)

print("AI Agent: ",Result.final_output)
