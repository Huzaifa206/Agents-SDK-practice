# alt z screen out
# win . emoji
import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,input_guardrail,GuardrailFunctionOutput,RunContextWrapper,TResponseInputItem,InputGuardrailTripwireTriggered
from pydantic import BaseModel,Field

load_dotenv()
set_tracing_disabled(disabled=True)  

class prime_minister_check(BaseModel):
    is_primeminister:bool=Field(description="if user is asking anything about prime minister then insert true in this field")


guardrial_agent= Agent(
    name='guardrial_agent',
    instructions='you check if the user is asking about prime minister or not',
    model='gpt-4.1-mini',
    output_type=prime_minister_check
)

@input_guardrail
async def primeminister_check(ctx:RunContextWrapper,agent: Agent,input:str| list[TResponseInputItem])->GuardrailFunctionOutput:

    guardrial_result=await Runner.run(guardrial_agent,input,context=ctx)

    return GuardrailFunctionOutput(
        output_info=guardrial_result.final_output,
        tripwire_triggered=guardrial_result.final_output.is_primeminister
    )

second_agent = Agent(
    name='agent',
    instructions='if user is asking about president,so additionally tell about prime minster and reply him',
    model='gpt-4.1-mini', 
    input_guardrails=[primeminister_check],
    handoff_description='you tell user about president and prime minister'
)

agent = Agent(
    name='Huzaifa',
    instructions='you are an helpful assistant',
    model='gpt-4.1-mini',
    input_guardrails=[primeminister_check],
    handoffs=[second_agent]
)

try:
    Result=Runner.run_sync(starting_agent=agent,input='hi')
    print("AI Agent: ",Result.final_output)
except InputGuardrailTripwireTriggered as e:
    print("🦶",e)
# query=input("User:   ")

