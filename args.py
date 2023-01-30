class args:
    model = 'SCINet'
    ### -------  dataset settings --------------
    data = 'data'
    root_path = ''
    data_path = 'data.csv'
    features = 'M' # может быть 'S' или 'M'
    target = 'OT' # наименование столбца в датасете
    freq = 's' # частота для кодирования времени
    checkpoints = 'exp/data_checkpoints/' # расположение контрольных точек
    inverse = False # денормализация выходных данных
    embed = 'timeF'

    ### -------  device settings --------------
    use_gpu = False # использование gpu
    gpu = 0
    use_multi_gpu = False
    devices = '0'

    ### -------  input/output length settings --------------
    seq_len = 96 # look back window, начальная длина SCINet encoder
    label_len = 48 # начальная длина Informer decoder
    pred_len = 48 # длина поледовательности прогнозирования
    concat_len = 0
    single_step = 0
    single_step_output_One = 0
    lastWeight = 1.0

    ### -------  training settings --------------
    cols = ""
    num_workers = 0 # количество работников-загрузчиков данных ??
    itr = 0
    train_epochs = 100 # количество эпох для тренировки
    batch_size = 32
    patience = 5
    lr = 0.0001
    loss = "mae" # оценочная функция
    lradj = 1
    use_amp = False
    save = True # сохранение выходных результатов
    model_name = 'SCINet'
    resume = False
    evaluate = False


    ### -------  model settings --------------
    hidden_size = 1
    INN = 1
    kernel = 5 # 3,5,7
    dilation = 1
    window_size = 12
    dropout = 0.5
    positionalEcoding = False
    groups = 1
    levels = 3
    stacks = 1
    num_decoder_layer = 1
    RIN = False
    decompose = False


    def __init__(self, data, features, seq_len, label_len, pred_len, hidden_size, stacks, levels, lr, batch_size, dropout, model_name):
        self.data = data
        self.features = features
        self.seq_len = seq_len
        self.label_len = label_len
        self.pred_len = pred_len
        self.hidden_size = hidden_size
        self.stacks = stacks
        self.levels = levels
        self.lr = lr
        self.batch_size = batch_size
        self.dropout = dropout
        self.model_name = model_name