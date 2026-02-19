# IA-102 Azure AI Engineer Associate

# 1. Agents

# 1. Sign in to Azure Portal and open Azure AI services
1. Go to **[Azure Portal](https://portal.azure.com/)**.
2. Sign in with your Azure account.
3. Go to **[Azure AI Services](https://ai.azure.com/)** to access Azure AI services.

## 2. To create virtual environment and install required libraries
1. Open a terminal or command prompt.
2. Navigate to your project directory.
3. Create a virtual environment:

```bash
python -m venv venv
```
4. Activate the virtual environment:
   - On Windows:

```bash
cd venv\Scripts\activate
```

- If you are activating for the first time, you may need to run the following command to allow script execution:

```bash

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Source - https://stackoverflow.com/a/77712241
# Posted by MingJie-MSFT
# Retrieved 2026-02-19, License - CC BY-SA 4.0

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```


5. Go back to root directory and install required libraries, run:

```bash
cd .. # Go back to root directory
cd .. # Go back to root directory
pip install -r requirements.txt
```

## 3. To run the application
1. Make sure you are in the root directory of the project.
2. Activate the virtual environment if you haven't already (see step 2).
3. Run the application:

```bash
python 1.agents.py
```

4. Follow the prompts in the terminal to interact with the application.

5. You can try this setting using GitHub Code Spaces, which provides a cloud-based development environment. To do this, simply click on the "Open in GitHub Codespaces" button at the top of the repository page. This will launch a new Codespace instance with the project preloaded, allowing you to run the application without needing to set up a local environment.

6. For GitHub Codespaces you need the .devcontainer configuration file to set up the development environment. This file specifies the necessary tools, extensions, and settings for the Codespace. If you don't have a .devcontainer folder in your repository, you can create one and add a devcontainer.json file with the appropriate configuration for your project. This will ensure that when you open the repository in GitHub Codespaces, it will automatically set up the environment according to your specifications.

# 2. Computer Vision
> - You can use Azure CLI with no storage settings.
> - You can use the Project Locally.

```bash
ls -a -l # Shows hidden files and folders
```

```bash
# Following the same principles in powershell on Azure CLI
# Create a virtual environment
python -m venv venv
# Activate the virtual environment
cd venv\bin\Activate.ps1
# Go back to root directory and install required libraries
cd .. # Go back to root directory
cd .. # Go back to root directory
# Install required libraries
pip install -r requirements.txt
# To check code files, this enables to edit the files in the current directory
code ./requirements.txt
# This removes the folder in Azure CLI If already exists, you can skip this step
rm -r mslearn-ai-vision -f
# To save changes on edit you must save using right click and close control + q
```