from __future__ import unicode_literals, print_function

import os
import random
from pathlib import Path

import plac
import spacy
from spacy.util import minibatch, compounding

from constants.constants import LABELS
from model_training_v2.training_01.train_data_01 import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "job_model")


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model=None, new_model_name="job_model", output_dir=path, n_iter=800):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    random.seed(0)
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    # ner.add_label(LABEL) # add new entity label to entity recognizer
    for label in LABELS:
        ner.add_label(label)
    # Adding extraneous labels shouldn't mess anything up
    ner.add_label("VEGETABLE")
    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()
    move_names = list(ner.move_names)
    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        sizes = compounding(1.0, 4.0, 1.001)
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = minibatch(TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
            print("Losses", losses)

    # test the trained model
    test_text = "Job description Position Title: Back End Developer Reports to: CEO Organization: Politech Position Location: Remote About Politech Politech creates digital products and technology solutions for nonprofits, campaigns, and foundations. Our primary focus has been to assist progressive organizations, particularly those influencing the policy and political landscape, that advocate on behalf of underserved communities. Our software platforms have been a vital part of keeping such organizations successful and efficient. Who We Are We are deeply committed to public service and progressive social change. We are 100% minority owned and operated with a diverse team, inclusive of gender, ethnicity, and race. Position Summary This role will focus on dev ops and back end/API development, but the ideal candidate will have a full stack skillset. Our stack is Postgres/Ruby/Rails/React. Right now we have a mix of HTML+jQuery and React but we are in the process of moving toward split app architecture. As part of that process we are building out a REST API and revamping our deployment environment. The latter would be the main focus of this position, but it would also involve pitching in on the React side of things when required. We are seeking someone with excellent communication skills who will work as a team player and a self-starter. The ideal candidate should have mid-level experience, but they won’t be placed in some hierarchical structure. This position will work directly with the other developers, and will report directly to the CEO. The individual should be highly motivated to make a difference and to have an impact on moving progressive issues forward. Our employees’ opinions matter to us for the success of the company, and we want you to bring creative solutions to make our work better for our clients. Interest and understanding of politics and campaigns is a plus but not required. Our employees are from all over the country, and bring varying levels of experience to the company. First and foremost, we value honesty from all employees within our firm. We strongly encourage a work environment centered on open communication and conscientiousness. Working remotely gives our employees the ability to better maintain a work-life balance, but we expect that productivity and job performance will not be sacrificed. We are a fully remote team so you will need to be flexible to work with staff in different time zones when necessary. Responsibilities Improve and maintain deployment environment and tools Design and build efficient, reusable, and reliable Ruby code Integration of data storage solutions Postgresql and Redis Expand and improve test coverage Identify bottlenecks and bugs then devise solutions to these problems Help maintain code quality, organization, and automation Integrations with external APIs Skills Experience setting up and maintaining deployment environments using Linux and Nginx Knowledge of best practices and IT operations in an always-up, always-available service Experience with automation/configuration management using either Puppet, Chef, or an equivalent Ability to use a wide variety of open source technologies and cloud services Strong experience with SQL and PostgreSQL Advanced understanding of object-oriented programming Experience with Ruby on Rails, along with common libraries such as Sidekiq Intermediate understanding of the syntax of Ruby and its nuances Intermediate understanding of Javascript and Jquery Familiarity with front end frameworks such as Vue, React or Angular Familiarity with concepts of MVC, ORM, and RESTful design patterns A knack for writing clean, readable Ruby code Ability to integrate multiple data sources and databases into one system Understanding of fundamental design principles behind a scalable application Able to create database schemas that represent and support business processes Able to implement automated testing platforms and unit tests Proficient understanding of code versioning tools such as Git Familiarity with development aiding tools such as Bower, Bundler, Rake, etc. Familiarity with continuous integration Compensation: Salary commensurate with knowledge, experience, and qualifications. Politech is an Equal Opportunity Employer that greatly values diversity at our company. We do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status, veteran status, or disability status. How to apply Apply with your GitHub account (or similar), resume, and cover letter. Introduce yourself to us as a colleague. Show us your future here! We value great writers, so be yourself, be creative. Stock cover letters won’t do. Tell us why you want this job. Let us know why you want to work at Politech and not somewhere else. You should be able to show samples of your previous work upon request."
    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta["name"] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        # Check the classes have loaded back consistently
        assert nlp2.get_pipe("ner").move_names == move_names
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)


if __name__ == "__main__":
    plac.call(main)
