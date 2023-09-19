import argparse
import os
import pandas as pd
import numpy as np
import torch
from torch.utils.tensorboard import SummaryWriter
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from SCINet.experiments.exp_ETTh import Exp_ETTh
from args import args

def force_cudnn_initialization():
    s = 32
    dev = torch.device('cuda')
    torch.nn.functional.conv2d(torch.zeros(s, s, s, s, device=dev), torch.zeros(s, s, s, s, device=dev))

def init_model(args, nameModel):
  torch.manual_seed(4321)  # reproducible
  torch.cuda.manual_seed_all(4321)
  torch.backends.cudnn.benchmark = False
  torch.backends.cudnn.deterministic = True  # Can change it to False --> default: False
  torch.backends.cudnn.enabled = True

  Exp = Exp_ETTh

  mae_ = []
  maes_ = []
  mse_ = []
  mses_ = []
  lossArray = []

  force_cudnn_initialization()
  if args.evaluate:
      setting = '{}_{}_ft{}_sl{}_ll{}_pl{}_lr{}_bs{}_hid{}_s{}_l{}_dp{}_inv{}_itr0'.format(args.model, args.data, args.features, args.seq_len, args.label_len, args.pred_len, args.lr, args.batch_size, args.hidden_size, args.stacks, args.levels, args.dropout, args.inverse)
      exp = Exp(args)  # set experiments
      print('>>>>>>>testing : {}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'.format(setting))
      mae, maes, mse, mses = exp.test(setting, evaluate=True)
      print('Final mean normed mse:{:.4f},mae:{:.4f},denormed mse:{:.4f},mae:{:.4f}'.format(mse, mae, mses, maes))
  else:
      if args.itr:
          for ii in range(args.itr):
              # setting record of experiments
              setting = '{}_{}_ft{}_sl{}_ll{}_pl{}_lr{}_bs{}_hid{}_s{}_l{}_dp{}_inv{}_itr{}'.format(args.model, args.data, args.features, args.seq_len, args.label_len, args.pred_len, args.lr, args.batch_size, args.hidden_size, args.stacks, args.levels, args.dropout, args.inverse, ii)

              exp = Exp(args)  # set experiments
              print('>>>>>>>start training : {}>>>>>>>>>>>>>>>>>>>>>>>>>>'.format(setting))
              modelBin, loss = exp.train(setting, nameModel)
              lossArray.append(loss)
              print('>>>>>>>testing : {}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'.format(setting))
              mae, maes, mse, mses = exp.test(setting)
              mae_.append(mae)
              mse_.append(mse)
              maes_.append(maes)
              mses_.append(mses)

              torch.cuda.empty_cache()
          print('Final mean normed mse:{:.4f}, std mse:{:.4f}, mae:{:.4f}, std mae:{:.4f}'.format(np.mean(mse_), np.std(mse_), np.mean(mae_), np.std(mae_)))
          print('Final mean denormed mse:{:.4f}, std mse:{:.4f}, mae:{:.4f}, std mae:{:.4f}'.format(np.mean(mses_), np.std(mses_), np.mean(maes_), np.std(maes_)))
          print('Final min normed mse:{:.4f}, mae:{:.4f}'.format(min(mse_), min(mae_)))
          print('Final min denormed mse:{:.4f}, mae:{:.4f}'.format(min(mses_), min(maes_)))
      else:
          setting = '{}_{}_ft{}_sl{}_ll{}_pl{}_lr{}_bs{}_hid{}_s{}_l{}_dp{}_inv{}_itr0'.format(args.model, args.data, args.features, args.seq_len, args.label_len, args.pred_len, args.lr, args.batch_size, args.hidden_size, args.stacks, args.levels, args.dropout, args.inverse)
          exp = Exp(args)  # set experiments
          print('>>>>>>>start training : {}>>>>>>>>>>>>>>>>>>>>>>>>>>'.format(setting))
          modelBin, loss = exp.train(setting, nameModel)
          lossArray.append(loss)

          print('>>>>>>>testing : {}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'.format(setting))
          mae, maes, mse, mses = exp.test(setting)
          print('Final mean normed mse:{:.4f},mae:{:.4f},denormed mse:{:.4f},mae:{:.4f}'.format(mse, mae, mses, maes))
  return lossArray

class model():

    def __init__(self, name, id):
        self.name = name
        self.id = id
        # self.coefficients = self.dbm.loadCoefficient(name)

    # получение параметров модели
    # def getParam(self):
    #     return self.coefficients['LR'], self.coefficients['Stack'], self.coefficients['SeqLen'], self.coefficients['BatchSize'], self.coefficients['Level'], self.coefficients['Dropout']

    # прогнозирование
    # def predict(self, fromDateTime, toDateTime, coefficients, nameModel):
    #
    #     data = pd.read_csv('data_1.csv', parse_dates=['time'], sep=";", encoding='cp1251', low_memory=False)
    #
    #     features_considered = ['Defects.Roll10Sqm.DefMap1',
    #                            'OPC_V_voronka_K02', 'OPC_V_shnek_K02',
    #                            'OPC_KN_T_ist_Z1_K02', 'OPC_KN_T_ist_Z2_K02', 'OPC_KN_T_ist_Z3_K02']
    #
    #     features = data[features_considered]
    #     features.index = data['time']
    #     features = features.interpolate()
    #
    #     features = features[(features.index > fromDateTime) & (features.index < toDateTime)]
    #     features = features.rename(columns={'Defects.Roll10Sqm.DefMap1': 'OT'})
    #     features.index.names = ['date']
    #     features.to_csv('data.csv', ',', encoding='utf-8')
    #
    #     self.args = args('data', int(coefficients['HiddenSize']), int(coefficients['BatchSize']), int(coefficients['Epochs']), self.name)
    #     self.args.detail_freq = self.args.freq
    #     self.args.freq = self.args.freq[-1:]
    #
    #     Exp = Exp_ETTh
    #     exp = Exp(self.args)
    #
    #     self.pred, self.true, self.true_scale, self.pred_scale = exp.predict(nameModel)
    #
    #     return self.pred, self.true, self.true_scale, self.pred_scale, features.index

    def predict(self, frame, coefficients, nameModel):

        frame = frame.interpolate()
        frame.to_csv('data.csv', ',', encoding='utf-8')

        self.args = args('data', int(coefficients['HiddenSize']), int(coefficients['BatchSize']), int(coefficients['Epochs']), self.name, 'data.csv')
        self.args.detail_freq = self.args.freq
        self.args.freq = self.args.freq[-1:]

        Exp = Exp_ETTh
        exp = Exp(self.args)

        self.pred, self.true, self.true_scale, self.pred_scale = exp.predict(nameModel)
        os.remove('data.csv')
        return self.pred, self.true, self.true_scale, self.pred_scale, frame.index

    # def education(self, coefficients, fromDateTime, toDateTime, frame):
    #
    #     frame = frame.interpolate()
    #     frame.to_csv('sample_data/data.csv', ',', encoding='utf-8')
    #     # data = pd.read_csv('data_1.csv', parse_dates=['time'], sep=";", encoding='cp1251', low_memory=False)
    #     # features_considered = ['Defects.Roll10Sqm.DefMap1',
    #     #                        'OPC_V_voronka_K02', 'OPC_V_shnek_K02',
    #     #                        'OPC_KN_T_ist_Z1_K02', 'OPC_KN_T_ist_Z2_K02', 'OPC_KN_T_ist_Z3_K02']
    #     #
    #     # features = data[features_considered]
    #     # features.index = data['time']
    #     # features = features.interpolate()
    #     # features = features[(features.index > fromDateTime) & (features.index < toDateTime)]
    #     # features = features.rename(columns={'Defects.Roll10Sqm.DefMap1': 'OT'})
    #     # features.index.names = ['date']
    #     # features.to_csv('sample_data/data.csv', ',', encoding='utf-8')
    #
    #     arg = args('data', int(coefficients['HiddenSize']), int(coefficients['BatchSize']), int(coefficients['Epochs']), self.name)
    #     arg.detail_freq = arg.freq
    #     arg.freq = arg.freq[-1:]
    #
    #     init_model(arg, self.name)
    #
    #     true = np.load('exp/ett_results/' + self.name + "/true_scales.npy")
    #     pred = np.load('exp/ett_results/' + self.name + "/pred_scales.npy")
    #     return true, pred, features.index

    def education(self, coefficients, frame):

        frame = frame.interpolate()
        frame.to_csv('sample_data/data.csv', ',', encoding='utf-8')

        arg = args('data', int(coefficients['HiddenSize']), int(coefficients['BatchSize']), int(coefficients['Epochs']), self.name, 'sample_data/data.csv')
        arg.detail_freq = arg.freq
        arg.freq = arg.freq[-1:]

        # init_model(arg, self.name)
        loss = init_model(arg, self.name)

        true = np.load('exp/ett_results/' + self.name + "/true_scales.npy")
        pred = np.load('exp/ett_results/' + self.name + "/pred_scales.npy")
        return true, pred, frame.index, loss


