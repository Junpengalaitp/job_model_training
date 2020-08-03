# Project Title

job-model-training

## Author

* **Junpeng He** - *Initial work* - [alaitp](https://junpengalaitp.github.io/alaitp-frontend/)

## Main Feature
* Job description annotation and training custom job model

## How the model were trained
  I want to keep the model size small but I also want the general entities from en-core-web-lg, so this is how I trained
  the model:
  1. Started with an en-core-web-sm model.
  2. During annotation, I combined my own custom entity annotation and those general entities from en-core-web-lg.
  3. Run annotation test, check there weren't any mislabeled entities or overlapping entities.
  4. Update the en-core-web-sm with the combined entity annotations.

## Related Module
* alaitp-job-keywords

## Built With

* [Python 3.7](https://www.python.org/) - The programming language used
* [SpaCy](https://spacy.io/) - The NLP library used
* [Jupyter Notebook](https://jupyter.org/) - The editor used for annotation


