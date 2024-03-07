# template-openai-langchain

This template combines OpenAI and Langchain

> You must have a OpenAI Key as a pre-requisite


# Setting up Python virtual environment via script

You can use the provided `setup.sh` script to set your Python Virtual Environment if needed:

```
# Setting up the Python Env using a script

```
# Execute the script
. ./scripts/setup.sh
```

Executing the above script will create a virtual environment automatically. 

# Setting up Python virtual environment manually

You can setup your Python virtual env manually as the instructions below demonstrate:
```
# Creating the virtual env

python -m venv .venv
```

```
# Activating the Virtual Env

source .venv/bin/activate
```

# Installing the dependencies

The dependencies for this project are provided in the `requirements.txt` file.

```
# Installing the dependencies

pip install -r requirements.txt
```

Executing the above command should get the dependencies installed. 

# Run the app

```
python src/app.py
```


