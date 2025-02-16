**Install Dependencies in omni environment**
```
conda create -n "omni" python==3.12
conda activate omni
pip install -r requirements.txt
```

First time run the following command to download the weights in Powershell:

```
$files = "icon_detect/train_args.yaml", "icon_detect/model.pt", "icon_detect/model.yaml", "icon_caption/config.json", "icon_caption/generation_config.json", "icon_caption/model.safetensors"; foreach ($f in $files) { huggingface-cli download microsoft/OmniParser-v2.0 $f --local-dir weights }
```

**Start Omniarser Server (VM)**

```
cd ~/repo/OmniParser/omnitool/omniparserserver/
python -m omniparserserver
```

**Strat Sandbox (Local)**

Instart and start Docker Desktop first.

In Powershell:
```
cd C:\Users\zihch\repos\OmniParser\omnitool\omnibox\scripts
./manage_vm.ps1 start 
```

**Start UI (Local)**

```
cd C:\Users\zihch\repos\OmniParser\omnitool\gradio
python app.py --windows_host_url localhost:8006 --omniparser_server_url localhost:8001
```