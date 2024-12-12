from transformers import Trainer, TrainingArguments

from model_build_folder.model_build import llm_model
from tokenizer.tokenizer_main import token_generating
from master.config import config

# 훈련 설정
training_args = TrainingArguments(
    output_dir=config['output_dir'],
    overwrite_output_dir=config['overwrite_output_dir'],
    per_device_train_batch_size=config['per_device_train_batch_size'],
    num_train_epochs=config['num_train_epochs'],
    logging_dir=config['logging_dir'],
    logging_steps=config['logging_steps'],
    fp16=config['fp16'],
    gradient_accumulation_steps=config['gradient_accumulation_steps'],
    learning_rate=config['learning_rate'],
)

# Trainer 설정 및 훈련 시작
trainer = Trainer(
    model=llm_model,
    args=training_args,
    train_dataset=token_generating(),
)