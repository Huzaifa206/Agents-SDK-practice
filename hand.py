import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,enable_verbose_stdout_logging,Handoff,RunContextWrapper
from agents.extensions import handoff_filters
from pydantic import BaseModel

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

class model_refund(BaseModel):
    input:str

my_schema=model_refund.model_json_schema()
my_schema["additionalProperties"]=False

async def my_invoke_function(ctx:RunContextWrapper,input:str):
    
    return refund_agent

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

refund_agent_handoff=Handoff(
    agent_name='refund_agent',
    tool_name="refund_agent",
    tool_description='you provide user support in refund process',
    input_json_schema=my_schema,
    on_invoke_handoff=my_invoke_function,
    input_filter=handoff_filters.remove_all_tools,
    strict_json_schema=True,
    is_enabled=True
)

agent = Agent(
    name='Huzaifa',
    instructions='you always delgate task to the appropiate agent',
    model=OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=client
    ),
    handoffs=[biling_agent]
)

query=input("User:   ")
Result=Runner.run_sync(starting_agent=agent,input=query,max_turns=1)

print("AI Agent: ",Result.final_output)
print("Last agent:",Result._last_agent.name)
