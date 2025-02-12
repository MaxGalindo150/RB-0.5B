from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-0.5B"  # Cambia esto según el modelo que quieras
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Guarda el modelo y el tokenizer en tu directorio local
model.save_pretrained("./model/Qwen-05B")
tokenizer.save_pretrained("./model/Qwen-05B")

