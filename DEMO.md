```
conda activate omni
```

**Start Omniarser Server (VM)**

```
cd ~/repo/OmniParser/omnitool/omniparserserver/
python -m omniparserserver
```

**Strat Sandbox (Local)**

```
cd ~/OmniParser/omnitool/omnibox/scripts/
./manage_vm.ps1 start
```

**Start UI (Local)**

```
cd ~/OmniParser/omnitool/gradio/
python app.py --windows_host_url localhost:8006 --omniparser_server_url localhost:8001
```