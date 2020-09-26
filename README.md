# Heart-Disease-Web-Application
![Repo Size](https://img.shields.io/github/repo-size/Sayar1106/Heart-Disease-Web-Application?style=for-the-badge)
![License](https://img.shields.io/github/license/Sayar1106/Heart-Disease-Web-Application?style=for-the-badge)
![Code Quality](https://img.shields.io/lgtm/grade/python/github/Sayar1106/Heart-Disease-Web-Application?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/Sayar1106/Heart-Disease-Web-Application?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/Sayar1106/Heart-Disease-Web-Application?style=for-the-badge)

A data web application to predict heart disease using Streamlit.

## Data source

The data is taken from the UCI Machine Learning repository. 

[Heart Disease UCI dataset](https://www.kaggle.com/ronitf/heart-disease-uci)

These are the setup and concept instructions to be able to follow the project
end to end.

##  Software instructions
* Ensure that you have Git installed on your system. Install instructions [here](https://git-scm.com/downloads)
* If you are using Git and/or Github for the first time, [follow this guide](https://docs.github.com/en/github/getting-started-with-github/set-up-git) to set up the CLI for Github
* Ensure that Anaconda is installed on you system. You can check the setup instructions [here]("https://docs.anaconda.com/anaconda/install/")
* Create an account on [Heroku](https://signup.heroku.com/). 
* Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

## Setting up environment

### Virtual Environment setup:
First you will create an Anaconda virtual environment. To do this first check whether your Conda CLI is working as intended.

`$ conda --version`

This should show something like:
 
 `conda 4.8.5`

 After this, create a new conda environment by:

 `
 $ conda create --name heart-disease-app
 `

Or, you could follow the instructions mentioned [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)

 Check the environment `conda` is using by:

 `conda env list`

 You should see the `*` next to `heart-disease-app`.

### Pip setup:

 Next, check whether pip is installed properly using:

 `$ pip3 --version`

 This will show something like:

 `pip 20.2.2 from /Users/Sayar/anaconda3/lib/python3.6/site-packages/pip (python 3/6)`

 ### Heroku setup:

Lastly, ensure Heroku CLI is working properly:

`$ heroku --version`

Should show something like:

`heroku/7.42.5 darwin-x64 node-v12.16.2`

Ensure that your Heroku CLI is using the correct account:

`$ heroku login`

This will prompt you to press any key after which a tab will open on your browser via which you have to authenticate your account. Once this is done, you should see the confirmation of
the account display on your terminal with the correct email id.

## Clone repository and install dependencies:

Next, clone this repository into your local machine using:

`$ git clone https://github.com/Sayar1106/Heart-Disease-Web-Application.git`

Activate the virtual environment:

`$ conda activate heart-disease-app`

Next, install the `requirements.txt` in the cloned repository. `cd` into the source of the repository and do the following:

`$ pip3 install -r requirements.txt`

This should install all the required libraries for the workshop.

_**If you have reached this point you can wait until the workshop webinar.**_

## Running the application

To run the application make sure you are in the project directory:

`$ streamlit run app/app.py`

This will either automatically open a new tab in the browser or will give you a link to paste onto the browser.

## Deploying to Heroku

we will be doing this during the session.

## Concepts to know before the workshop
Required:

* Python and it's Data Structures.
* Understanding of ML and Data Anlaysis.

Recommended:
* Pandas
* Numpy
* Plotly
* Scikit-learn

Optional
* Shell

## Choice of editor/IDE

I will be using Visual Studio Code for this project because they offer fantastic support for Python and for IPython Notebooks. I will be demoing code in both in an IPython Notebook as well as Python3.

You can install Visual Studio Code [here](https://code.visualstudio.com/download)

Feel free to submit pull requests or add issues to the project.