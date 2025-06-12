from huggingface_hub import login
from dotenv import load_dotenv
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TextStreamer,
    BitsAndBytesConfig,
)
import torch
import gc
import os

load_dotenv(override=True)
hf_token = os.getenv("HF_TOKEN")

LLAMA = "meta-llama/Meta-Llama-3.1-8B-Instruct"

login(hf_token, add_to_git_credential=True)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant specialized in converting PDFs into concise summaries. Make sure not to omit any important points under each heading.",
    },
    {
        "role": "user",
        "content": "Please convert the provided PDF into a structured summary, preserving all key points under their respective headings.",
    },
]


# Quantization Config - this allows us to load the model into memory and use less memory

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
)


model = AutoModelForCausalLM.from_pretrained(
    LLAMA, device_map="auto", quantization_config=quant_config
)
memory = model.get_memory_footprint() / 1e6
print(f"Memory footprint: {memory:,.1f} MB")


def generate_and_save_summary(model_name=LLAMA, output_path="summary.txt"):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    # Prepare inputs
    inputs = tokenizer.apply_chat_template(
        messages, return_tensors="pt", add_generation_prompt=True
    ).to("cuda")

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        model_name, device_map="auto", quantization_config=quant_config
    )

    # Generate summary (no streamer)
    outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)

    # Decode and write to file
    summary_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary_text)

    # Clean up
    del model, inputs, outputs, tokenizer
    gc.collect()
    torch.cuda.empty_cache()

    print(f"Summary written to {output_path}")
