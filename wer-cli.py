import argparse

import datetime
from evaluate import load
import sys


def calculate_wer(reference_file, prediction_file):
    
    with open(reference_file) as f:
        reference = f.read()

    with open(prediction_file) as f:
        prediction = f.read()
    
    _wer = load("wer")
    wer_score = _wer.compute(predictions=[prediction], references=[reference])
    wer_score = wer_score * 100
    return wer_score

def main():

    args = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    args.add_argument("-r", "--reference", help="Reference file",  required=True)
    args.add_argument("-p", "--prediction", help="Predition file",  required=True)
    
    d = args.parse_args().__dict__

    wer_score = calculate_wer(d["reference"], d["prediction"])
    print(f"WER metric: {wer_score}%");

if __name__ == "__main__":
    main()    
