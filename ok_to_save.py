import tensorflow as tf
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("johngiorgi/declutr-small")
model = AutoModelForMaskedLM.from_pretrained("johngiorgi/declutr-small")
tokenizer.save_pretrained("./hugging_face_model")
model.save_pretrained("./hugging_face_model")