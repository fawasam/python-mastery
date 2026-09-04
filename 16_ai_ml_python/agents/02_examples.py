"""
Advanced AI Agents: ReAct Autonomous Execution Loop.
"""

from dataclasses import dataclass


@dataclass
class AgentStep:
    thought: str
    tool_name: str | None
    tool_input: dict[str, str] | None
    observation: str | None


class ReActAgent:
    """Simulated ReAct Agent running Thought -> Action -> Observation execution steps."""
    def run_goal(self, goal: str, max_steps: int = 3) -> str:
        print(f"=== Agent Started Goal: '{goal}' ===")
        
        # Step 1: Decide to call tool
        step1 = AgentStep(
            thought="I need to check the temperature in London before answering.",
            tool_name="get_weather",
            tool_input={"city": "London"},
            observation="Weather in London: 18°C, Partly Cloudy"
        )
        print(f"Step 1 Thought: {step1.thought}")
        print(f"Step 1 Action: Call {step1.tool_name}({step1.tool_input})")
        print(f"Step 1 Observation: {step1.observation}\n")

        # Step 2: Final Answer
        final_answer = "The current weather in London is 18°C and partly cloudy."
        print(f"Final Answer: {final_answer}")
        return final_answer


if __name__ == "__main__":
    agent = ReActAgent()
    agent.run_goal("What is the weather like in London today?")
