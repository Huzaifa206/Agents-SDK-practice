from agents import Agent, Runner, RunHooks, AgentHooks

class AllRunHooks(RunHooks):
    async def on_agent_start(self, ctx, agent):
        print(f"[GLOBAL] Agent '{agent.name}' starting.")
    async def on_agent_end(self, ctx, agent, output):
        print(f"[GLOBAL] Agent '{agent.name}' finished with output: {output}")
    async def on_handoff(self, ctx, from_agent, to_agent):
        print(f"[GLOBAL] Handoff from '{from_agent.name}' to '{to_agent.name}'.")
    async def on_tool_start(self, ctx, agent, tool):
        print(f"[GLOBAL] '{agent.name}' invoking tool: {tool.name}")
    async def on_tool_end(self, ctx, agent, tool, result):
        print(f"[GLOBAL] '{agent.name}' tool '{tool.name}' completed. Result: {result}")

class SingleAgentHooks(AgentHooks):
    async def on_start(self, ctx, agent):
        print(f"[{agent.name}] Starting.")
    async def on_end(self, ctx, agent, output):
        print(f"[{agent.name}] Ended with output: {output}")
    async def on_handoff(self, ctx, agent, source):
        print(f"[{agent.name}] Received handoff from '{source.name}'.")
    async def on_tool_start(self, ctx, agent, tool):
        print(f"[{agent.name}] Starting tool: {tool.name}")
    async def on_tool_end(self, ctx, agent, tool, result):
        print(f"[{agent.name}] Tool {tool.name} gave: {result}")

agent = Agent(name="SupportAgent", instructions="Help the user.", hooks=SingleAgentHooks())
result = await Runner.run(agent, "Need help with account", hooks=AllRunHooks())
