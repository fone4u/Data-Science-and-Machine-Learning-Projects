import numpy
import pandas
import statsmodels.api as sm


def simple_heuristic(file_path):
    '''
    Given a list of Titantic passengers and their associating
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data. 

    Write a simple heuristic that will use
    the passengers' gender to predict if they survived the Titanic diaster.
    
        
    If the passenger is female, your heuristic should assume that the
    passenger survived. If the passenger is male, you heuristic should
    assume that the passenger did not surive.
    
    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger["Sex"] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survied or 0 otherwise. 

    For example, if a passenger survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    Or if a passenger perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for i,n in df.iterrows():
		if n[PassengerId] == 'male':
			predictions[PassengerId] = 0
		else:
		    predictions[PassengerId] = 1
	return predictions 
 

print simple_heuristic('/home/shubham/Documents/Kaggle/Titanic/train.csv')



        

