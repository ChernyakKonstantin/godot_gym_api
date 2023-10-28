import fire
from .install_addon import install_addon

def main_(command: str, *args, **kwargs):
    if command == "install_addon":
        install_addon(*args, **kwargs)
    else:
        print(f"Unknown command: {command}")
 
def main():
    fire.Fire(main_)
    
if __name__ == '__main__':
    main()