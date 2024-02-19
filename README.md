Setup Env
```
pip install -r requirements.txt
```

Download the models from bloke. From the root dir, run below
```
huggingface-cli download TheBloke/Llama-2-7b-Chat-GGUF llama-2-7b-chat.Q4_K_M.gguf --local-dir models --local-dir-use-symlinks False
huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir models --local-dir-use-symlinks False

```

Next, edit promptfooconfig.yaml.
Then run:
```
promptfoo eval
```

Afterwards, you can view the results by running `promptfoo view`
