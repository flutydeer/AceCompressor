import argparse
import base64
import json
import zstandard

class Encrypter:
    def __init__(self) -> None:
        pass

    def comp_project(self, src, target):
        project_data = {}
        with open(src, 'rb') as src_file:
            raw_content = src_file.read()
            cctx = zstandard.ZstdCompressor()
            compressed = cctx.compress(raw_content)
            project_data['content'] = base64.b64encode(compressed).decode()
            project_data['salt'] = ""
        project_data.update({"debugInfo": {"os": "windows", "platform": "pc", "version": "10"}, "version": 1000})
        with open(target, 'w') as target_file:
            json.dump(project_data, target_file, separators=(',', ':'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='acep compress')
    parser.add_argument('src', type=str, help='source file path')
    parser.add_argument('target', type=str, help='target file path')
    args = parser.parse_args()
    encrypter = Encrypter()
    encrypter.comp_project(args.src, args.target)