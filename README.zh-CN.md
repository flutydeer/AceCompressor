# AceCompressor

解压或压缩 ACE Studio 工程文件（*.acep）。 仅支持由 ACE Studio v1.7.8 及以上版本创建的工程文件。如果你的工程文件是由之前的版本创建的，必须先用 ACE Studio v1.7.8 打开并保存。

## 用法

克隆本仓库并运行以下命令来安装环境：

```shell
pip install -r requirements.txt
```

解压 acep 文件：

```shell
python acecompressor.py decomp "example.acep" "example.json"
```

压缩 acep 文件：

```shell
python acecompressor.py comp "example.json" "example.acep"
```

查看帮助：

```shell
python acecompressor.py
```