import fire
import shutil
from pathlib import Path


def install_addon(target_path: str) -> None:
    addons_path = Path(target_path).joinpath("addons")
    if not addons_path.exists():
        print("Creating addons folder...")
        addons_path.mkdir()

    base_path = Path(__file__).absolute().parents[3].joinpath("godot_addon")

    print("Copying reinforcement_learning addon...")
    shutil.copytree(
        base_path.joinpath("reinforcement_learning"), addons_path.joinpath("reinforcement_learning"), dirs_exist_ok=True
    )

    print("Copying godobuf addon...")
    shutil.copytree(base_path.joinpath("reinforcement_learning"), addons_path.joinpath("godobuf"), dirs_exist_ok=True)

    print("Done!")


if __name__ == "__main__":
    fire.Fire(install_addon)
