#uv add openai-agents[litellm]

# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner, set_tracing_disabled
# from agents.extensions.models.litellm_model import LitellmModel
# import litellm

# load_dotenv()
# set_tracing_disabled(disabled=True)
# litellm.disable_aiohttp_transport=True
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if not GEMINI_API_KEY:
#     raise ValueError("Missing GEMINI_API_KEY in .env file")

# agent = Agent(
#     name='Huzaifa',
#     instructions='You are a helpful assistant',
#     model=LitellmModel(
#         model='gemini/gemini-2.0-flash',
#         api_key=GEMINI_API_KEY
#     )
# )

# result = Runner.run_sync(agent, "Who are you?")
# print(result.final_output)
