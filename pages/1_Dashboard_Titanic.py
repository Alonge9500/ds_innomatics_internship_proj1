import streamlit as st
from matplotlib import image
import os
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)
st.text('This Page shows A Few Exploratory data analysis of the Titanic dataset')

df = pd.read_csv(DATA_PATH)
st.dataframe(df.head(8))
st.text('The Above Table shows the sample of the dataset')

fares= df.fare
ages = df.age
fig, (ax,ax1) = plt.subplots(1,2)
ax.set_title('The distribution of the Fare paid by Passengers',fontdict={'fontsize':7})
ax.hist(fares, bins=20)

ax1.set_title('The distribution of the age of Passengers',fontdict={'fontsize':7})
ax1.hist(ages, bins=20)

st.pyplot(fig)

histogram_text =""" * Base on the figure in plot 1 which show the distibution of fares
* it's obvious that most of the passengers paid a fee within the range of 0-200 dollars
* And the second plot which shows the age,
* Clearly shows that the majority passenger are within the age range of 20-40 Years"""

st.text(histogram_text)
label = df.sex.value_counts().index
value = df.sex.value_counts()

class_label = df['class'].value_counts().index
class_value = df['class'].value_counts()

fig2, (axe,axe1) = plt.subplots(1,2)
axe.set_title('The Bar plot of the sex of passengers',fontdict={'fontsize':8})
axe.bar(label,value)

axe1.set_title('The Bar plot of passengers by Class',fontdict={'fontsize':8})
axe1.bar(class_label,class_value)
st.pyplot(fig2)

bar_text = ''' Base on the above Plots
* There are more Male on Board than Females
* And majority of the passengers on board are in Third Class
'''
st.text(bar_text)