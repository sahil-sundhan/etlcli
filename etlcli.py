import argparse
import papermill
import json
import sys

def load_config():
    try:
        with open('./etlcli/config.json') as f:
            CONFIG = json.load(f)
            return CONFIG
    except FileNotFoundError:
        sys.stdout.write("Config file not found")


class cliApp():
    def __init__(self):
        self._config = load_config()
        self._parser = argparse.ArgumentParser(description='Simple command based bundle execution utility')
        self._parser.add_argument('--bundle', '-b', type=str, help='bundle name')
        self._parser.add_argument('--node', '-n', type=str, help='node name')

    def _executeNode(self, book, log):
        try:
            papermill.execute_notebook(book, log)
        except Exception as e:
            sys.stdout.write(f"Failure!\n{e}\n")

    def _parseInput(self):
        args = self._parser.parse_args()
        if args.bundle:
            bundle = str(args.bundle)
            if bundle in self._config:
                if args.node:
                    node = args.node
                    if node in self._config[bundle]:
                        book = self._config[bundle][node]['main']
                        log = self._config[bundle][node]['log']
                        self._executeNode(book, log)
                    else:
                        sys.stdout.write(f"Node {node} not found")
            else:
                 print() # edit here
        else:
            sys.stdout.write(f"Bundle {args.bundle} not found")

    def run(self):
        self._parseInput()

if __name__ == '__main__':
    print(load_config())
