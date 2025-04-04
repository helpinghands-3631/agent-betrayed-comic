from autogen_ext.agent import DockerAgent

# Define multiple agents with different tasks
agents = [
    DockerAgent(
        name="agent-hello",
        image="python:3.11-slim",
        command="python -c 'print(\\\"Hello from Agent 1\\\")'"
    ),
    DockerAgent(
        name="agent-date",
        image="python:3.11-slim",
        command="python -c 'import datetime; print(f\\\"Agent 2 Time: {datetime.datetime.now()}\\\")'"
    ),
    DockerAgent(
        name="agent-math",
        image="python:3.11-slim",
        command="python -c 'print(\\\"Agent 3 Result: \\\" + str(42 * 7))'"
    )
]

# Run all agents
for agent in agents:
    print(f"Running {agent.name}...")
    agent.run()
