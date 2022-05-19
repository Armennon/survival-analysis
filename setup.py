from setuptools import setup, find_packages

# Adding install requirements
lif = {"lifelines": ["datasets/*"]}
setup(
    author="Armine Papikyan",
    description="A package for implementing Survival Analysis.",
    name="survival-analysis",
    packages=find_packages(include=["survival_analysis", "survival_analysis.*"]),
    version="0.0.1",
    install_requires=["numpy>=1.22.3", "pandas>=1.4.2", "seaborn>=0.11.2", "matplotlib>=3.2.2"],
    package_data=lif,
    python_requires=">=3.8"
)
