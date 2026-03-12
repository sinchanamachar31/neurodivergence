def generate_flowchart(concept_text):

    flowchart_prompt = f"""
Convert the following concept into a simple educational flowchart.

Use arrows and steps.

Example format:

Step 1
  ↓
Step 2
  ↓
Step 3

Concept:
{concept_text}
"""

    return flowchart_prompt