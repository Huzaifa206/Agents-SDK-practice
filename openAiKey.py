# uv init hello_agent
# cd hello_agent
# uv add openai-agents python-dotenv
# uv run main.py

from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings
load_dotenv()

agent= Agent(
    name = "my agent",
    instructions="you are a helpful assistant",
    model="gpt-4.1-nano",
    model_settings=ModelSettings(temperature=0.1, max_tokens=1000)
)
result = Runner.run_sync(starting_agent=agent, input="hi who are you?")
print(result.final_output)