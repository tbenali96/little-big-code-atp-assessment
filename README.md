little-big-code-atp-assessment
==============================

The goal of the project is to create a model capable of predicting the winners of tennis matches.

Project Organization
------------

    ├── Makefile           <- Makefile with the necessary commands to work with the repository
    ├── README.md          <- The top-level README for developers using this project
    ├── data
    │   ├── test           <- Test data
    │   ├── processed      <- The final, canonical data sets for modeling
    │   └── raw            <- The original, immutable data dump
    │
    ├── visualizations     <- Data Exploration Charts
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks for data exploration and modeling
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │
    │   ├── utils       <- Scripts with util functions
    │   │    ├── __init__.py    <- Makes features a Python module 
    │   │    └── utils.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │    ├── __init__.py    <- Makes features a Python module 
    │   │    └── build_features.py
    │   │
    │   ├── app       <- Scripts to create a simple dashboard on streamlit
    │   │    ├── __init__.py    <- Makes features a Python module 
    │   │    ├── logo.png    <- LittleBigCode Logo 
    │   │    └── app.py
    │   │
    │   └── models         <- Scripts to train models and then use trained models to make
    │       │                 predictions
    │       ├── __init__.py    <- Makes models a Python module  
    │       ├── predict_model.py
    │       └── train_model.py
    │
    ├── test               <- Tests
    ├── setup.cfg          <- Configuration file
    ├── .pre-commit-config.yaml     <- Configuration file for creating a pre-commit hook to evaluate the code's format with black and flake8
    ├── pyproject.toml               <- Configuration files
    │
    └── .gitignore         <- A gitignore file


--------

The following are some command lines to help use the source code of this project : 

Once you cloned the repository, you first need to create a virtual environment and make sure to download the right libraries. To do so, use :
```
make requirements
```
To launch the web app in order to see some visualizations, you use : 
```
make app
```
For our project, the data is stored in the repository. To build the features, you use :
```
make data
```
To train the model, you use :
```
make train
```
For the inference part, we are here working with a sample dataset. The following command will help make the inference on this particular dataset. 
But, in a production environment, we will have to make the dataset an argument for our inference function. 
```
make predict
```
To test and evaluate coverage of our code, you can use :
```
make test
```
Ultimately, the objective of the tests is to create a CI/CD pipeline to validate the correctness of our source code. It is important to note that the tests 
that we created are only related to the code itself, not the Machine Learning artifacts. 
We can, for example, add other tests that evaluate the validity of the model before putting into production. 