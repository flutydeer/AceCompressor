import argparse
import json
import base64
import zstandard


class Decrypter:
    def __init__(self):
        pass

    def decomp_project(self, src:str, target:str):
        with open(src) as src_file:
            project_data = json.load(src_file)
            raw_content = base64.b64decode(project_data['content'])
            dctx = zstandard.ZstdDecompressor()
            decompressed = dctx.decompress(raw_content)
        with open(target, 'wb') as target_file:
            target_file.write(decompressed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='acep decompress')
    parser.add_argument('src', type=str, help='source file path')
    parser.add_argument('target', type=str, help='target file path')
    args = parser.parse_args()
    decrypter = Decrypter()
    decrypter.decomp_project(args.src, args.target)