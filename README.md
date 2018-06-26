# RussiaLago: Safeguarding Voters from State Sponsored Content

## Description

Comprehensively analyzed over 200,000 Russian sponsored tweets in order to recognize the features of state sponsored content
* Used regular expressions and NLTK to extract frequently named entities & common hashtags
* Employed Afinn for lexicon based sentiment analysis of individual tweets
* Visualized results with Plotly.py and created a showcase with the Dash web framework
* Trained and tested multiple Naive Bayes classifiers with scikit-learn to identify tweets of Russian origin

## Running the web applet

Requires the Anaconda distribution and the following libraries (and their dependencies) will need to be installed if not already present: 
* plotly `pip install plotly`
* dash `pip install dash==0.21.1`
* dash-renderer `pip install dash-renderer==0.13.0`
* dash-html-components `pip install dash-html-components==0.11.0`
* dash-core-components `pip install dash-core-components==0.23.0`  

You can run the Flask app locally by executing `python3 app.py`. Make sure to have 'functions.py' and 'data.csv' in the same directory as the applet.
Note: the data processing and analytics behind these results can be found in 'main.ipynb'. 

## Contributers:

* Siddharth Nanda (Lead Developer)
* [Dhyey Parikh](https://www.linkedin.com/in/dhyey-parikh/)
* [Dale Wilson](https://www.linkedin.com/in/dale-wilson-4a3893150/)
* [Clara Na](https://www.linkedin.com/in/clara-na/)

## Environment

The project was developed with Python 3.6.5 on MacOS 10.13 

## References

The higher level technologies used are:
* [Conda](https://conda.io/docs/) for package management
* [Git](https://git-scm.com/) for version control
* [Jupyter](http://jupyter.org) for interactive Python notebooks
* [Natural Language Toolkit](http://www.nltk.org) for text analysis
* [scikit-learn](http://scikit-learn.org/stable/) for machine learning classification
* [Plotly](https://plot.ly) for interactive data data visualization
* [Dash](https://plot.ly/products/dash/) as a framwork for creating the web application

## Final Notes from the Developers [June 25, 2018]

This project was orginally completed in March 2018 at HackUVA, and since then we spent some time since then continuing to test models and ideas on the same dataset. While doing so we noted and addressed a number of issues. 
* Our orginal code was extremely hard to follow at times and there were several redundant processes throughout (such as csv generation): all cells now have comments, and unneccessary code has since been removed
* The naive bayes classifiers we created suffered due to the selection of training/testing data (we streamed data from Twitter in order to create our train/test sets). As it is not possible to clearly replicate the results of our classifiers, we have decided not to upload them to this repository. However, no edits have been made to our hackathon presentation to preserve the veracity of the project in retrospect. 
* While we explored other classification models that we could have created and uploaded to 'replace' the naive bayes classifiers, such as topic modelling via Latent Dirichlet allocation, we ultimately felt that these would not yield any further insight into the data
  * Note: it is possible to create and view the results of such a model through packages such as [MALLET](http://mallet.cs.umass.edu), and we encourage anyone who is interested to do so

Additional information about contributor roles and an overview of the project and findings can be found in the PDF presentation!
