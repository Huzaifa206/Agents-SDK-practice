# alt z screen out
# win . emoji
import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,output_guardrail,GuardrailFunctionOutput,RunContextWrapper,TResponseInputItem,OutputGuardrailTripwireTriggered
from typing import Any
from pydantic import BaseModel,Field

load_dotenv()
set_tracing_disabled(disabled=True)  

class president_ornot(BaseModel):
    is_president:bool=Field(description="if user is asking anything about president then insert true in this field")


guardrial_agent= Agent(
    name='guardrial_agent',
    instructions='you always check if the user is asking about president or not',
    model='gpt-4.1-mini',
    output_type=president_ornot
)

@output_guardrail
async def president_check(ctx:RunContextWrapper,agent: Agent,output:Any)->GuardrailFunctionOutput:

    guardrial_result=await Runner.run(guardrial_agent,output,context=ctx)

    return GuardrailFunctionOutput(
        output_info=guardrial_result.final_output,
        tripwire_triggered=guardrial_result.final_output.is_president
    )

sec_agent = Agent(
    name='sec_agent',
    instructions='you are an helpful assistant',
    model='gpt-4.1-mini',
    output_guardrails=[president_check],
    
)

agent = Agent(
    name='Huzaifa',
    instructions='you are an helpful assistant',
    model='gpt-4.1-mini',
    output_guardrails=[president_check],
    handoffs=[sec_agent]
    
)

try:
    Result=Runner.run_sync(starting_agent=agent,input='who is the president of pakistan in 2023,delegate to second agent')
    print("AI Agent: ",Result.final_output)
except OutputGuardrailTripwireTriggered as e:
    print("🦶",e)
# query=input("User:   ")

