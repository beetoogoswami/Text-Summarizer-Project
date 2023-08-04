import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="Beetoo"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="beetoo.goswami@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer AP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Beetoo/Text-Summarizer-Project",
)