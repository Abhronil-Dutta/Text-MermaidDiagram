from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

model_name = "TroyDoesAI/MermaidStable3B"

# 1) Load tokenizer + model, explicitly trusting remote code
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model     = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

# 2) Build an Alpaca‐style prompt
prompt = """
### Instruction:
Create a flowchart in Mermaid for the following process. Output ONLY the Mermaid DSL (beginning with "graph ..."), without any backticks or extra explanation:

1. Choose your favorite coffee beans.
2. Grind the beans to a medium‐coarse texture.
3. Boil water to about 195–205°F (90–96°C).
4. Place a filter in a coffee maker or dripper.
5. Add the ground coffee (about 1–2 tablespoons per 6 ounces of water).
6. Slowly pour hot water over the grounds in a circular motion.
7. Let the coffee "bloom" for 30 seconds, then continue pouring.
8. Once brewing finishes, pour coffee into a cup.
9. Add milk, sugar, or sweetener if desired.
10. Enjoy your freshly brewed cup of coffee!
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_new_tokens=150,
    pad_token_id=tokenizer.eos_token_id,
    do_sample=False
)

# 4) Decode the raw output and strip whitespace.
raw = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

def extract_mermaid(raw_text):
    # Look for a ```mermaid block and capture everything until the closing ```
    pattern = r"```mermaid\s*(.*?)```"
    m = re.search(pattern, raw_text, flags=re.DOTALL)
    if not m:
        return None
    # m.group(1) is the inner code; add back the opening ```mermaid fence if you need it
    inner = m.group(1).strip()
    return inner 

mermaid_only = extract_mermaid(raw)
print(mermaid_only)


with open("diagram.mmd", "w", encoding="utf-8") as f:
    f.write(mermaid_only)

print("Saved Mermaid code to diagram.mmd")

