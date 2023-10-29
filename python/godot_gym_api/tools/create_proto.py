import fire
import shutil
from pathlib import Path


def create_proto(target_path: str) -> None:
    destination_path = Path(target_path).joinpath("message.proto")
    base_path = Path(__file__).absolute().parents[0]
    shutil.copy2(base_path.joinpath("files").joinpath("message.proto"), destination_path)
    print("Done!")
    
if __name__ == "__main__":
    fire.Fire(create_proto)