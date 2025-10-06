import os
import google.generativeai as genai


# Get generator
models_gen = genai.list_models()

# Convert to list to print nicely
models = list(models_gen)

for model in models:
    print(model)
