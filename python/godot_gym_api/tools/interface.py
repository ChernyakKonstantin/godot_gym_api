import fire
from .install_addon import install_addon
from .create_proto import create_proto

def main_(command: str, *args, **kwargs):
    if command == "install_addon":
        install_addon(*args, **kwargs)
    elif command == "create_proto":
        create_proto(*args, **kwargs)
    else:
        print(f"Unknown command: {command}")
 
def main():
    fire.Fire(main_)
    
if __name__ == '__main__':
    main()