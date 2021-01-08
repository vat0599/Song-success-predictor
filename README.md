# Songs success predictor using Machine Learning
Predicting song’s commercial success based on lyrics and other metrics using Machine Learning.

Make sure that MillionSongSubset folder and other files are in the same local directory in your PC.

*Note: This project is an analysis of the various factors in which a song's "hit factor" is calculated.*
*This is entirely hard-core ML case study and thus live demo is not available.*
*Further development can be done in future to get the live hit factor rating for song that is played.*

## Steps to follow:
- Clone the repo.
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

## Contributions
Do not hesitate to contribute by [filling an issue](https://github.com/vat0599/Song-success-predictor/issues) or [a PR](https://github.com/vat0599/Song-success-predictor/pulls) !
