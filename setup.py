from setuptools import find_packages, setup


def get_version():
    """Gets the RL-pytorch version."""
    path = "rlpyt/__init__.py"
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("__version__"):
            return line.strip().split()[-1].strip().strip('"')
    raise RuntimeError("bad version data in __init__.py")


setup(
    name="rlpyt",
    version=get_version(),
    description="A clean code base for deep reinforcement learning.",
    author="Yi-Chen Li",
    author_email="ychenli.X@gmail.com",
    url="https://github.com/BepfCp/rlbase",
    packages=find_packages(include=["rlpyt*"]),
    python_requires="<3.11,>=3.7",
    install_requires=[
        "gymnasium[all]",
        "h5py",
        "hydra-core==1.3.2",
        "numba",
        "numpy==1.23.5",
        "omegaconf==2.3.0",
        "setuptools",
        "stable_baselines3",
        "torch",
        "tqdm",
        "rlplugs @ git+https://github.com/BepfCp/rlplugs@main",
    ],
)
