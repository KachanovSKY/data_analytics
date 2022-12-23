import pandas as pd
import datetime
import vk_api
import os
import requests
import json
import random
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sys
from urllib.parse import urlencode

from io import BytesIO

df = pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-v-kachanovskij-24/Lesson7/step_2_lesson_7.csv')
chrome_count = df.query("browser == 'Google Chrome'").visits[0]
all_count = df.visits.sum()
proc_links = ((df.query("browser == 'Google Chrome'").visits[0] * 100) / df.visits.sum()).round(0)
df.browser.count()