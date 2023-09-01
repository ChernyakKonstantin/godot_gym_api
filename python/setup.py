from setuptools import setup, find_packages

setup_kwargs = {
    "name": "godot_gym_api",
    "version": "1.1",
    "description": "gym/gymnasium environment API to communicate with Godot Engine.",
    "packages": find_packages(),
    "author": "Konstantin Cherniak",
    "author_email": "chernyakonstantin@gmail.com",
    "keywords": ["Godot", "reinforcement-learning", "api"],
    "url": "https://github.com/ChernyakKonstantin/godot_rl",
}

install_requires = [
    "gymnasium==0.29.0",
    "numpy==1.24.4",
]

if __name__ == "__main__":
    setup(**setup_kwargs, install_requires=install_requires)
