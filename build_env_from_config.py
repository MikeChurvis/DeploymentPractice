"""
# .env.config.json structure:
{
  "env": [
    {
      "label": string,
      "value": string,
      "consumers": {
        "consumerName": "environmentVariableKey",
        ...
      }
    }
  ],
  "hardlinks": {
    "consumerName": [
        "link/path/relative/to/project/root/.env",
        ...
    ],
    ...
  }
}
"""

import json
import os

base_dir = os.path.dirname(__file__)
config_filename = ".env.config.json"
config_path = os.path.join(base_dir, config_filename)

output_dir = os.path.join(base_dir, "env")

def env_filename(consumer_name: str): return f".{consumer_name}.env"
        
        

def main():
    with open(config_path) as config_file:
        config = json.load(config_file)
    
    print(f"Building .env files from config at {config_path}")
    
    env_data = {}
    
    for variable in config["env"]:
        for consumer, key in variable["consumers"].items():
            if consumer not in env_data:
                env_data[consumer] = {}
            
            print("  -", f"writing {variable['label']} to {env_filename(consumer)} as {key}")
            env_data[consumer][key] = variable["value"]
            
    for consumer, variables in env_data.items():
        env_filepath = os.path.join(output_dir, env_filename(consumer))
        env_content = "\n".join(
            f"{key}=\"{value}\"" 
            for key, value in variables.items()
        )
    
        with open(env_filepath, mode='w') as env_file:
            env_file.write(env_content)
    
    if 'hardlinks' not in config or len(config['hardlinks']) == 0:
        return
    
    print("Generating hard links:")
    
    for consumer, link_paths in config['hardlinks'].items():
        env_filepath = os.path.join(output_dir, env_filename(consumer))
        
        for link_path in link_paths:
            link_path_abs = os.path.join(base_dir, link_path)
            
            print('  -', f"{env_filename(consumer)}", '<-->', f"{link_path}")
            
            if os.path.exists(link_path_abs):
                os.remove(link_path_abs)
            
            os.link(env_filepath, link_path_abs)
        

if __name__ == '__main__':
    main()