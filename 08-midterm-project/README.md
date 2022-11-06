# Dataset
I've created my own dataset. I've downloaded some music from spotify with the notebook [spotify-notebook](notebooks/spotify_data.ipynb), then I concataned the data.
You can find de data documentation (playlist and artists) in this [notebook](notebooks/notebook.ipynb).
# Main Goal
The main goal of this project is to classified all kind of music and predict if I'd like or not.
# Enviroment
I've created a conda enviroment for this project
## Create a conda enviroment
`conda create -n midterm-project python=3.9`
## Activate the conda enviroment
`conda activate midterm-project`
## Install Ipykernel
`conda install ipykernel`
## Install requirements.txt
`pip install -r requirements.txt`

## Working on notebook (EDA-train-model evaluation)
The EDA, train and model-evaluation is in this [notebook](notebooks/notebook.ipynb).
## Train script
Train script is [here](train.py)
## Predict script
Predict script is [here](predict.py)
## Testing predict-script.
I'll test the script with a random music of the dataset.
### Results
![Predict-script](images/testing-script.PNG)
## Docker
I'll create a pipenv for this and use `Pipfile` and `Pipfile.lock` for the docker container.
### Create a pipenv
`pipenv install`
### Activate the pipenv
`pipenv shell`
### Install requirements.txt
`pip install -r requirements.txt`
### Build the docker image
`docker build -t midterm-project .`
### Run the docker image
`docker run -it midterm-project`
