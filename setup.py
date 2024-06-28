from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.0.1',
    author='anjal',
    install_requires=["openai","langchain","streamlit","python_dotenv","PyPDF2","langchain_community"],
    packages=find_packages()

)