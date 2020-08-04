# Project Title

job-model-training

## Author

* **Junpeng He** - *Initial work* - [alaitp](https://junpengalaitp.github.io/alaitp-frontend/)

## Main Feature
* Job description annotation and training custom job model

## How I trained the model
  I want to keep the model size small, but I also want the general entities from en-core-web-lg, so this is how I 
  trained the model:
  1. Started with an en-core-web-sm model as custom model.
  2. Get those general entity indices from en-core-web-lg model(automated).
  3. Get those custom entity indices from the custom model(automated).
  4. Add the custom entity indices that were not recognized or mislabeled by the custom model(manual).
  5. During training, I combined my own custom entity annotation and those general entities from en-core-web-lg.
  6. Run annotation test, check there weren't any mislabeled entities or overlapping entities.
  7. Update the custom model with the combined entity annotations.

## Related Module
* alaitp-job-keywords

## Built With

* [Python 3.7](https://www.python.org/) - The programming language used
* [SpaCy](https://spacy.io/) - The NLP library used
* [Jupyter Notebook](https://jupyter.org/) - The editor used for annotation


