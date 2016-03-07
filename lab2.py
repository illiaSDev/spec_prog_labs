from spyre import server
import pandas as pd
import  urllib.request
import  urllib.error
import json
from matplotlib import pyplot as plt
import numpy as np

class VHIplot(server.App):
    title = "VHI info"

    inputs = [{     "input_type":'dropdown',
                    "label": 'column', 
                    "options" : [ {"label": "VCI", "value":"VCI"},
                                  {"label": "TCI", "value":"TCI"},
                                  {"label": "VHI", "value":"VHI"}],
                    "variable_name": 'column', 
                    "action_id": "update_data" },
              {     "input_type":'text',
                    "label": 'Year since', 
                    "value":2010,
                    "variable_name": "since", 
                    "action_id": "update_data" },
              {     "input_type":'text',
                    "label": 'Year till', 
                    "value":2016,
                    "variable_name": "till", 
                    "action_id": "update_data" },
              {     "input_type":'text',
                    "label": 'Week from', 
                    "value":1,
                    "variable_name": "week_since", 
                    "action_id": "update_data" },
              {     "input_type":'text',
                    "label": 'Week to', 
                    "value":52,
                    "variable_name": "week_till", 
                    "action_id": "update_data" },
              {     "input_type":'dropdown',
                    "label": 'Region', 
                    "variable_name": "reg", 
                    "options" : [ {"label":"Cherkasy Oblast", "value":"1"},
								  {"label":"Chernihiv Oblast", "value":"2"},
								  {"label":"Chernivtsi Oblast", "value":"3"},
								  {"label":"Crimea", "value":"4"},
								  {"label":"Dnipropetrovsk Oblast", "value":"5"},
								  {"label":"Donetsk Oblast", "value":"6"},
								  {"label":"Ivano-Frankivsk Oblast", "value":"7"},
								  {"label":"Kharkiv Oblast", "value":"8"},
								  {"label":"Kherson Oblast", "value":"9"},
								  {"label":"Khmelnytskyi Oblast", "value":"10"},
								  {"label":"Kiev Oblast", "value":"11"},
								  {"label":"Kiev City", "value":"12"},
								  {"label":"Kirovohrad Oblast", "value":"13"},
								  {"label":"Luhansk Oblast", "value":"14"},
								  {"label":"Lviv Oblast", "value":"15"},
								  {"label":"Mykolaiv Oblast", "value":"16"},
								  {"label":"Odessa Oblast", "value":"17"},
								  {"label":"Poltava Oblast", "value":"18"},
								  {"label":"Rivne Oblast", "value":"19"},
								  {"label":"Sevastopol`", "value":"20"},
								  {"label":"Sumy Oblast", "value":"21"},
								  {"label":"Ternopil Oblast", "value":"22"},
								  {"label":"Transkarpathia Oblast", "value":"23"},
								  {"label":"Vinnytsia Oblast", "value":"24"},
								  {"label":"Volyn Oblast", "value":"25"},
								  {"label":"Zaporizhia Oblast", "value":"26"},
								  {"label":"Zhytomyr Oblast", "value":"27"}],
                    "action_id": "update_data"}]
    controls = [{   "control_type" : "button",  
                    "label" : "Get info",
                    "control_id" : "update_data"}]

    tabs = ["Plot", "Table"]  # add tabs

    outputs = [{    "output_type" : "plot",
                    "output_id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot",
                    "on_page_load" : True },
               {    "output_type" : "table",
                    "output_id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]
    def getPlot(self,params):
        path="vhi_id_"+str(params['reg'])+".csv"
        df = pd.read_csv(path, index_col=False, header=1)
        x=df[(df['year']>=int(params['since']))]
        x=x[(x['year']<=int(params['till']))]
        x=x[(x['week']>=int(params['week_since']))]
        x=x[(x['week']<=int(params['week_till']))]
        z=x[params['column']]
        y=x.index
        y=y-y[0]
        plt.plot(y,z)
        return plt.gcf()

    def getData(self, params):
        path="vhi_id_"+str(params['reg'])+".csv"
        df = pd.read_csv(path, index_col=False, header=1)
        x=df[(df['year']>=int(params['since']))]
        x=x[(x['year']<=int(params['till']))]
        x=x.rename(columns={'%Area_VHI_LESS_15':'VHI<15'})
        x=x.rename(columns={'%Area_VHI_LESS_35':'VHI<35'})
        return x

app = VHIplot()
app.launch(port=8080)