# yellowbrick.classifier
# Visualizations related to evaluating Scikit-Learn classification models
#
# Author:   Rebecca Bilbro <rbilbro@districtdatalabs.com>
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Author:   Neal Humphrey
# Created:  Wed May 18 12:39:40 2016 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: __init__.py [5eee25b] benjamin@bengfort.com $

"""
Visualizations related to evaluating Scikit-Learn classification models.
"""

##########################################################################
## Imports
##########################################################################

## Hoist visualizers into the classifier namespace
from ..base import ScoreVisualizer
from .base import ClassificationScoreVisualizer
from .class_balance import ClassBalance
from .classification_report import ClassificationReport, classification_report
from .confusion_matrix import ConfusionMatrix
from .rocauc import ROCAUC, roc_auc
