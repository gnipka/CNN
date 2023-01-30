import pandas as pd
from dbModel import dbModel
from args import args
from SCINet.experiments.exp_ETTh import Exp_ETTh

class model():

    def __init__(self, name):
        self.name = name
        self.dbm = dbModel()
        self.coefficients = self.dbm.load_coefficient(name)

    def get_param(self):
        return self.coefficients['LR'], self.coefficients['Stack'], self.coefficients['SeqLen'], self.coefficients['BatchSize'], self.coefficients['Level'], self.coefficients['Dropout']

    def predict(self, fromDateTime, toDateTime):
        data = pd.read_csv('data_1.csv', parse_dates=['time'], sep=";", encoding='cp1251', low_memory=False)

        features_considered = ['Defects.Roll10Sqm.DefMap1',
                               'OPC_V_voronka_K02', 'OPC_V_shnek_K02',
                               'OPC_KN_T_ist_Z1_K02', 'OPC_KN_T_ist_Z2_K02', 'OPC_KN_T_ist_Z3_K02']

        features = data[features_considered]
        features.index = data['time']
        features = features.interpolate()

        features = features[(features.index > fromDateTime) & (features.index < toDateTime)]
        features = features.rename(columns={'Defects.Roll10Sqm.DefMap1': 'OT'})
        features.index.names = ['date']
        features.to_csv('data.csv', ',', encoding='utf-8')

        self.args = args('data', self.coefficients['Features'], int(self.coefficients['SeqLen']), int(self.coefficients['LabelLen']), int(self.coefficients['PredLen']), int(self.coefficients['HiddenSize']), int(self.coefficients['Stack']), int(self.coefficients['Level']), float(self.coefficients['LR']), int(self.coefficients['BatchSize']), float(self.coefficients['Dropout']), self.name)
        self.args.detail_freq = self.args.freq
        self.args.freq = self.args.freq[-1:]

        Exp = Exp_ETTh
        exp = Exp(self.args)

        setting = '{}_{}_ft{}_sl{}_ll{}_pl{}_lr{}_bs{}_hid{}_s{}_l{}_dp{}_inv{}_itr0'.format(self.args.model, self.args.data,
                                                                                             self.args.features,
                                                                                             self.args.seq_len,
                                                                                             self.args.label_len,
                                                                                             self.args.pred_len, self.args.lr,
                                                                                             self.args.batch_size,
                                                                                             self.args.hidden_size,
                                                                                             self.args.stacks, self.args.levels,
                                                                                             self.args.dropout, self.args.inverse)

        self.pred, self.true, self.true_scale, self.pred_scale = exp.predict(setting);

        return self.pred, self.true, self.true_scale, self.pred_scale, features.index

