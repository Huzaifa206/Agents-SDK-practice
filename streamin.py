import os
import asyncio
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled
from openai.types.responses import ResponseTextDeltaEvent

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

async def main():
    
    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


asyncio.run(main())

