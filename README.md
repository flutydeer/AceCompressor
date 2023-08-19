# AceCompressor
 
Decompress or compress ACE Studio project files (*.acep). Only project files created with ACE Studio v1.7.8 and above are supported. If your project file was created with a previous version, you must first open and save it with ACE Studio v1.7.8.

[中文文档](./README.zh-CN.md)

## Usage

Clone the repository and run the following command to install requirements:

```shell
pip install -r requirements.txt
```

To decompress a acep file, use

```shell
python acecompressor.py decomp "example.acep" "example.json"
```

To compress a acep file, use

```shell
python acecompressor.py comp "example.json" "example.acep"
```

To see help, use

```shell
python acecompressor.py
```