import os
from dotenv import load_dotenv
from agents import Agent,Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled,RunContextWrapper,function_tool
from pydantic import BaseModel

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

class userinfo(BaseModel):
    name : str
    age: int
    alive: bool
    rollno: int

my_info = userinfo(name="huzaifa", age=19, alive=True, rollno=34)

def dynamic_ins(wrapper:RunContextWrapper[userinfo],agent:Agent):
    return f"whenever user ask for users roll number then use given tool huzaifa_information to get rollno.user name is {wrapper.context.name} and users age is {wrapper.context.age} "


@function_tool
async def huzaifa_information(wrapper:RunContextWrapper[userinfo]):
    return f"the user's roll number is {wrapper.context.rollno}"

client=AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

agent = Agent[userinfo](
    name='Huzaifa',
    instructions=dynamic_ins,
    model=OpenAIChatCompletionsModel(
        model='gemini-2.0-flash',
        openai_client=client
    ),
    tools=[huzaifa_information]
)

query=input("User:   ")
Result=Runner.run_sync(starting_agent=agent,input=query,context=my_info)

print("AI Agent: ",Result.final_output)
