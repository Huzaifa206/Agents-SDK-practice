import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,enable_verbose_stdout_logging

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

biling_agent=Agent(
    name="biling_agent",
    instructions='you handle all billing related queries,provide clear and consice information regarding billing issues',
    handoff_description='you help user in billing queries'
)

refund_agent=Agent(
    name="refund_agent",
    instructions='you handle all refund related queries,assist users in processing refunds efficiently',
    handoff_description='you help uswer in refund agent'
)

agent = Agent(
    name='Huzaifa',
    instructions='you always delgate task to the appropiate agent',
    model=OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=client
    ),
    handoffs=[biling_agent,refund_agent]
)

query=input("User:   ")
Result=Runner.run_sync(starting_agent=agent,input=query)

print("AI Agent: ",Result.final_output)
print("Last agent:",Result._last_agent.name)