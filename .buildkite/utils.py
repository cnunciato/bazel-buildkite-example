import json, os, subprocess

def run(command):
    return subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip().splitlines()

def group(targets, exclude=None):
    groups = set()

    for target in targets:
        directory, _, _ = target.rpartition(":")
        groups.add(directory.lstrip("/"))
    
    if exclude:
        groups.discard(exclude)
    
    return list(groups)

def is_dir(path):
    return os.path.isdir(path)

def command_step(key, emoji, label, commands=[], plugins=[]):
    step = {"key": key, "label": f":{emoji}: {label}", "commands": commands}
    
    if len(plugins) > 0:
        step[plugins] = {"plugins": plugins}
    
    return step

def to_json(data, indent=None):
    return json.dumps(data, indent=indent)

def dirs(paths):
    return list(filter(lambda p: is_dir(f"{p}"), paths))