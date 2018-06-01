# mira.py
# -------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Mira implementation
import util
PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.legalLabels = legalLabels
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        self.features = trainingData[0].keys() # this could be useful for your code later...

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        """
        This method sets self.weights using MIRA.  Train the classifier for each value of C in Cgrid,
        then store the weights that give the best accuracy on the validationData.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        representing a vector of values.
        """
        "*** YOUR CODE HERE ***"

        """weights = []
        maxAccuracy = 0
        selectedC = Cgrid[0]
        finalWeights=0

        bestWeights = None
        bestCorrect = 0.0
        
        for c in Cgrid:
            for iteration in range(self.max_iterations):
                print "Starting iteration ", iteration, "..."
                for i in range(len(trainingData)):

                    f = trainingData[i]
                    y = self.classify([f])[0]
                   
                    y_actual = trainingLabels[i]
                    if y != y_actual:   # if incorect prediction
                        Tau = (((self.weights[y] - self.weights[y_actual])*f)+1.0)/(2*(f*f))  # calculate a Tau according to the formuale in a way that minimizes difference actual and prediction
                        Tau = min(Tau , c)
                        
                        for key in f:
                            self.weights[y_actual][key] = self.weights[y_actual][key] + Tau
                            self.weights[y][key] = self.weights[y][key] - Tau

            correct = 0
            guesses = self.classify(validationData)
            for i, guess in enumerate(guesses):
                correct = correct + (validationLabels[i] == guess and 1.0 or 0.0)

            if correct > bestCorrect:
                bestCorrect = correct
                bestWeights = self.weights"""

        #self.weights = bestWeights

        """bestWeights = None
        bestCorrect = 0.0
        weights = self.weights.copy()
        for c in Cgrid:
            for iteration in range(self.max_iterations):
                print "Starting iteration ", iteration, "..."
                for i in range(len(trainingData)):
                    f = trainingData[i].copy()
                    y = self.classify([f])[0]
                   
                    y_actual = trainingLabels[i]
                    if y != y_actual:
                        #T = f.copy()
                        tau = min(c, ((self.weights[y_actual] - self.weights[y]) * f + 1.0) / (2.0 * (f * f)))

                        #for j in range(len(f)):
                            #f[j] = f[j] * tau
                            
                        f.divideAll(1.0 / tau)
                        #self.weights[y_actual] = self.weights[y_actual] + f
                        #self.weights[y] = self.weights[y] - f

            correct = 0
            guesses = self.classify(validationData)
            for i, guess in enumerate(guesses):
                correct = correct + (validationLabels[i] == guess and 1.0 or 0.0)

            if correct > bestCorrect:
                bestCorrect = correct
                bestWeights = self.weights

        self.weights = bestWeights"""

        bestWeights = None
        bestCorrect = 0.0
        weights = self.weights.copy()

    
        for c in Cgrid:
            self.weights = weights.copy()
            for n in range(self.max_iterations):
                
                #for i, data in enumerate(trainingData):
                for i in range(len(trainingData)):
                    f= trainingData[i]
                             
                    y_actual = trainingLabels[i]
                    y = self.classify([f])[0]
                    
                    if y_actual != y:
                        
                        f1 = trainingData[i].copy()
                        tau = min(c, ((self.weights[y] - self.weights[y_actual]) * f1 + 1.0) / (2.0 * (f1 * f1)))

                        
                        for key,value in f1.items():
                            f1[key] = f1[key] * tau
                     
                        self.weights[y_actual] = self.weights[y_actual] + f1
                        self.weights[y] = self.weights[y] - f1
                        
                        
                        

            """correct = 0
            guesses = self.classify(validationData)

            print validationData
            for i, guess in enumerate(guesses):
                correct = correct + (validationLabels[i] == guess and 1.0 or 0.0)

            if correct > bestCorrect:
                bestCorrect = correct
                bestWeights = self.weights

        self.weights = bestWeights"""


    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


