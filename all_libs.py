import numpy as np
import pandas as pd

import matplotlib as plt
#%matplotlib inline

import seaborn as sns

from chainconsumer import ChainConsumer

import plotly.graph_objects as go
from scipy.stats import multivariate_normal as mn

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# for the ANN
import torch
import torch.nn as nn
import torch.nn.functional as F

# GUI
import tkinter as tk
from PIL import Image, ImageTk
