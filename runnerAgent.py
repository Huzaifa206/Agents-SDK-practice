import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,RunConfig


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

config = RunConfig(
    model_provider=external_client,
    tracing_disabled=True,
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    ),
)


agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistent.",

)

result = Runner.run_sync(agent, "who are u?", run_config=config)
print(result.final_output)

