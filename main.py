import uvicorn
from configparser import ConfigParser
from typing import Optional

def get_config_value(config: ConfigParser, section: str, key: str, default: Optional[str] = None) -> str:
    try:
        return config.get(section, key)
    except:
        return default

def main():
    config = ConfigParser()
    config.read('config/config.ini')

    host = get_config_value(config, 'server', 'host', '0.0.0.0')
    port = get_config_value(config, 'server', 'port', '8000')

    try:
        uvicorn.run("app.api:app", host=host, port=int(port), reload=True)
    except ValueError:
        print(f"Error: Invalid port number {port}")

if __name__ == "__main__":
    main()