#this script does NLP tasks for testing created word embeddings using python nlp SpaCy lib. For training POS and NER tagger and using them to evaluate embeddings.

#On the site https://spacy.io/usage/training there is a tool to generate a base_config.cfg file, that you can download
#then that config needs to be filled in with all the other defaults. This generates the config.cfg
#python -m spacy init fill-config base_config.cfg config.cfg

#For training a model, you need a .spacy format file. To generate it, you use the covert method https://spacy.io/api/cli#convert with options
#i converted all 3 (train, dev, test) .conllu files this way from https://github.com/UniversalDependencies/UD_Latvian-LVTB
#python -m spacy convert lv_lvtb-ud-test.conllu .\ --converter conllu

#Train the custom model to use in the spaCy nlp pipeline for tagging later.
#python -m spacy train config.cfg --output ./ --paths.train ./lv_lvtb-ud-train.spacy --paths.dev ./lv_lvtb-ud-dev.spacy
