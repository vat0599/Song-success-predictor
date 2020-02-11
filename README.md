# Songs success predictor using Machine Learning
Predicting song’s commercial success based on lyrics and other metrics using Machine Learning.

Regarding the dataset used, as the folder was too large, I uploaded to my drive. So follow this link which connects to google drive and download the folder
https://drive.google.com/open?id=1wZDzx3YhoVTiuMRnbRTd9b73uAR9Oafq

Make sure that this folder and other files are in the same local directory in your PC.

*Note: This project is an analysis of the various factors in which a song's "hit factor" is calculated.*
*This is entirely hard-core ML case study and thus live demo is not available.*
*Further development can be done in future to get the live hit factor rating for song that is played.*

## Steps to follow:
- First download the dataset given in the link
- After the download is done, we need to find the important features that affect the output variable.
- For this reason, run cleaning_data.py
- You will see there will be two csv sheets generated, namely training_data.csv, testing_data.csv
- Once you reach this stage you are good to go.
- Now open the main R file named music_rating.R and run all.
- You will see on your R Studio console, a bunch of plots being plotted with a lot of textual information printed.
- The code is well commented for your understanding.

## Models used:
- Basic Models:
	- Linear Regression
	- Logistic Regression
	- Linear Discriminant Analysis(LDA)
	- Quadratic Discriminant Analysis(QDA)
	- K-Nearest Neighbors(KNN)
	- Cross Validation(CV)
	- Polynomial Logistic Regression
	- Decision Tree
- Advanced/Alternate Models:
	- Best subset, Forward and Backward stepwise
	- Ridge and Lasso
	- Splines
	- Generalised Additive Models(GAMs)
	- Random Forest
	- Boosting

## Conclusion:
For my dataset, it was found that non linear models have higher accuracies and are more stable than the linear ones.

This may vary from dataset to dataset.
