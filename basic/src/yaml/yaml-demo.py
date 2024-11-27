"""
python - yaml 文件操作

可选的库：
1. PyYaml
2. Ruamel.yaml
3. AnyConfig

第二个库更好地实现了 yaml 规范，允许修改 yaml 文件内容
第三个库可以把 JSON、YAML、TOML 等配置文件的内容加载为 dict
"""
import anyconfig
from ruamel.yaml import YAML

# 读取 yaml 文件内容
with open('./demo.yaml') as f:
    yaml = YAML()
    print(yaml.load(f))

config = anyconfig.load('./demo.yaml')
print(config)
print(f"username: {config['user']['name']}")
