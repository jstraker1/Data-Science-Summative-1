import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

df = pd.read_csv("attendance_anonymised-1.csv")
df.drop(['Planned End Date'] , axis =1 )
df.rename(columns = {'Unit Instance Code' : 'Module code' , 'Calocc Code': 'Year' , 'Long Description' : 'Module Name' , 'Register Event ID' : 'Event ID' , 'Register Event Slot ID' : 'Event Slot ID' , 'Planned Start Date': 'Date' ,  'is Positive' : 'Has Attended' , 'Postive Marks' : 'Attended' , 'Negative Marks' : 'NotAttended' , 'Usage Code':'Attendance Code' } , inplace = True)
pd.to_datetime(df['Date'])
df = df.sort_values(by = 'Date')
filtered_df = df[df['Module code'] == 1266] 
attendance = pd.DataFrame(filtered_df.groupby(['Date'])['Attended'].mean())
x= attendance.index
y = attendance['Attended']


ui = ui.page_fluid(
    ui.h2("Dashboard of student attendance"),
    ui.output_plot("bar_chart"),
)



def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.plot
    def bar_chart():

        plt.bar(x , y)
        plt.title("Bar chart showing attendance to History module over time")
        plt.xlabel('Date')
        plt.ylabel('Proportion of students attended')
        plt.xticks(rotation = 'vertical')
        plt.show
    

        
       

app = App(ui, server)
