
import anthropic, os

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def research(idea):

    prompt = f"""
Research this startup idea and produce:

- market demand
- competitors
- product requirements
- architecture

IDEA:
{idea}
"""

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[{"role":"user","content":prompt}]
    )

    return response.content[0].text
