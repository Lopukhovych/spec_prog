from spyre import server

import pandas as pd
from os import listdir

class StockExample(server.App):
    title = "Laba2 Mama ama criminal"

    inputs = [{     "input_type":'dropdown',
                    "label": 'Parametr',
                    "options" : [ {"label": "VCI", "value":"VCI"},
                                  {"label": "TCI", "value":"TCI"},
                                  {"label": "VHI", "value":"VHI"}],
                    "variable_name": 'column',
                    "action_id": "update_data" },

                { "input_type": 'dropdown',
                   "label": 'Province',
                   "options": [{"label": "Vinnickaya", "value": "1"},
                               {"label": "Volinskaya", "value": "2"},
                               {"label": "Dnepropetrovskaya", "value": "3"},
                               {"label": "Doneckaya", "value": "4"},
                               {"label": "Jitomirskaya", "value": "5"},
                               {"label": "Zakarpatskaya", "value": "6"},
                               {"label": "Zaporojskaya", "value": "7"},
                               {"label": "Ivano-Frankovskaya", "value": "8"},
                               {"label": "Kievskaya", "value": "9"},
                               {"label": "Kirovogradskaya", "value": "10"},
                               {"label": "Luganskaya", "value": "11"},
                               {"label": "Lvovskaya", "value": "12"},
                               {"label": "Nikolaevskaya", "value": "13"},
                               {"label": "Odeskaya", "value": "14"},
                               {"label": "Poltavskaya", "value": "15"},
                               {"label": "Rovenskaya", "value": "16"},
                               {"label": "Summskaya", "value": "17"},
                               {"label": "Ternopol'skaya", "value": "18"},
                               {"label": "Khar'kovskaya", "value": "19"},
                               {"label": "Khersonskaya", "value": "20"},
                               {"label": "Hmel'nickaya", "value": "21"},
                               {"label": "Cherkasskaya", "value": "22"},
                               {"label": "Chernivec'ka", "value": "23"},
                               {"label": "Chernigovskaya", "value": "24"},
                               {"label": "Krim", "value": "25"},
                               {"label": "Kiev", "value": "26"},
                               {"label": "Sevastopol'", "value": "27"},],
                   "variable_name": 'province',
                   "action_id": "update_data"},

                {    "input_type": 'text',
                   "label": 'Year',
                   "value": '1996',
                   "variable_name": 'year',
                   "action_id": "update_data" },

                {    "input_type": 'text',
                   "label": 'Week \n From',
                   "value": '13',
                   "variable_name": 'week_start',
                   "action_id": "update_data" },
                 {    "input_type": 'text',
                   "label": 'To',
                   "value": '20',
                   "variable_name": 'week_end',
                   "action_id": "update_data" }

              ]  # action_ids can point to controls
    
    # changing the input state now activates this control so we no longer need a button
    controls = [{   "control_type" : "hidden",  
                    "label" : "get value about VCI,TCI,VHI",
                    "control_id" : "update_data"}]

    tabs = ["Plot", "Table"]  # add tabs

    outputs = [{    "output_type" : "plot",
                    "output_id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot",  # must specify which tab each output should live in
                    "on_page_load" : True },
                {   "output_type" : "table",
                    "output_id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def getData(self, params):
        column = params['column']
        province = params['province']
        try:
            year = int(params['year'])
        except ValueError:
            year = 2008
        try:
            week_start = int(params['week_start'])
        except ValueError:
            week_start = 5
        try:
            week_end = int(params['week_end'])
        except ValueError:
            week_end = 20

        if week_start < 1 or week_start > week_end or week_start > 52:
            week_start = 1
        if week_end > 52 or week_end < 1:
            week_end = 52
        if year > 2015 and week_end > 5 or year < 1982:
            year = 2008

        df = pd.read_csv('VHI/'+filter(lambda x: x.startswith('VHI_' + province + '_'), listdir("VHI/."))[0])
        df = df[df['year'] == int(year)]
        df = df[df['week'] >= int(week_start)]
        df = df[df['week'] <= int(week_end)]
        df = df[['week', column]]

        return df

    def getPlot(self, params):
        df = self.getData(params)
        plt_obj = df.set_index('week').plot()
        plt_obj.set_ylabel(list(df[:0])[1])
        plt_obj.set_title('week')
        fig = plt_obj.get_figure()
        return fig

app = StockExample()
# app.launch(port=9093)