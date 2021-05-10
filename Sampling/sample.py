import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random

File_Object = pd.read_csv("Population.csv")
Population = File_Object["Population (2020)"].tolist()

Population_Data = st.mean(Population)

print(Population_Data)


def show_fig(mean_data):
    df = mean_data
    fig = ff.create_distplot([df], ['Population'], show_hist=False)
    fig.show()


def RandomDataPickerMean(counter):
    Random_Data = []

    for i in range(0, counter):
        random_number = random.randint(0, len(Population))
        value = Population[random_number]
        Random_Data.append(value)

    Mean = st.mean(Random_Data)

    return Mean


def setup():
    mean_list = []

    for i in range(0, 100):
        set_of_means = RandomDataPickerMean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)


setup()
