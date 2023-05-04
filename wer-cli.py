import os
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

def main()    

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-r", "--reference", help="Reference file")
    parser.add_argument("-p", "--prediction", help="Predition file")


    wer = calculate_wer(args.reference, args.prediction)
    print(f"WER metric: {wer_score}%");

if __name__ == "__main__":
    main()    
