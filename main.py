
import os
import argparse
from utils.quick_start import quick_start
os.environ['NUMEXPR_MAX_THREADS'] = '48'
#设置环境变量 NUMEXPR_MAX_THREADS 的值为 '48'。具体来说，它是告诉NumExpr库在进行计算时最多可以使用48个线程。


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='FourierKAN_GCF', help='name of models')
    parser.add_argument('--dataset', '-d', type=str, default='games', help='name of datasets')
    #默认的dataset名称是games
    
    config_dict = {
        'gpu_id': 0,
    }

    args, _ = parser.parse_known_args()

    quick_start(model=args.model, dataset=args.dataset, config_dict=config_dict, save_model=True)


