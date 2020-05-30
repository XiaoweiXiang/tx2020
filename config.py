import os

# 项目地址
project_path = os.getcwd()

# 数据地址
train_path = os.path.join(project_path, 'data/train')
test_path = os.path.join(project_path, 'data/test')
feature_path = os.path.join(project_path, 'data/feature')

# 分析结果
analysis_path = os.path.join(project_path, 'analysis')

# 模型结果
model_path = os.path.join(project_path, 'model')

# 结果保存地址
submission_path = os.path.join(project_path, 'submission')
