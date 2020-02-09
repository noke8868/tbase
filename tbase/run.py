# -*- coding:utf-8 -*-
"""
1. 提供多进程并环境
2. 根据输入选择：算法，Policy-Net, Value-Net, 优化算法. 然后生成Agent
3. 训练保存模型performance, 参数
"""
import hydra
from tbase.common.logger import logger


@hydra.main(config_path="config.yaml")
def main(args):
    logger.info("running")
    logger.info("TODO")
    print(args.pretty())


if __name__ == '__main__':
    main()
