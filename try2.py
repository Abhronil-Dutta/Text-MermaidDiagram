from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re
import subprocess

# model used
model_name = "TroyDoesAI/MermaidStable3B"

# 1. Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model     = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

def extract_mermaid(raw_text: str) -> str:
    """
    Extracts the last Mermaid code block starting with 'graph' (possibly with direction)
    and ending at a line containing '[End]' as a node label. Includes the [End] node.
    """
    # Find all code blocks starting with 'graph ...' and ending at a line with [End]
    blocks = re.findall(
        r'(graph\s+\w+[\s\S]+?\[End\][^\n]*\n?)', raw_text, flags=re.IGNORECASE
    )
    
    if not blocks:
        raise RuntimeError("Could not find Mermaid code ending with [End] in the model's output.")
    
    return blocks[-1].strip()




def generate_mermaid(user_query: str, filename: str = "diagram.mmd") -> None:
    """
    Given a plain-English instruction, prompts the model to output only Mermaid DSL,
    extracts it, and saves to filename.
    """
    # Short, direct prompt
    prompt = f"""Create a flowchart in Mermaid for the following process. Output ONLY the Mermaid DSL, starting with "graph" and ending with "[End]". Do not include any explanations, steps, or extra text.

                Process: {user_query}
            """

    # Tokenize and generate
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=False
    )

    # Decode output
    raw = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(f"Model output:\n{raw}\n")

    # Extract Mermaid code
    mermaid_code = extract_mermaid(raw)

    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(mermaid_code)

    print(f"Saved Mermaid code to {filename}.")

def render_mermaid_to_png(mmd_file, png_file):
    """
    Calls Mermaid CLI (mmdc) to convert .mmd to .png.
    """
    try:
        subprocess.run([r'C:\Users\abhro\AppData\Roaming\npm\mmdc.cmd', '-i', mmd_file, '-o', png_file], check=True)
        print(f"PNG saved as {png_file}")
    except subprocess.CalledProcessError as e:
        print("Error running mmdc:", e)
    except FileNotFoundError as e:
        print("FileNotFoundError:", e)


if __name__ == "__main__":
    # Example usage
    generate_mermaid(
        "Make a cup of coffee using a French press, including steps for grinding beans, boiling water, steeping, and serving.",
        "coffee_process.mmd"
    )
    render_mermaid_to_png("coffee_process.mmd", "coffee_process.png")

