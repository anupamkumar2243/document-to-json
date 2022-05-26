# IMAGE TO JSON CONVERTOR

## Introduction

This project is based on the convertion of financial document like invoice into json(javascript object notation) format.

## Techniques for the process

We use ocr(optical character recognization) and ner(named entity recognization)

OCR(optical character recognization):- OCR is recognizing text in images, such as scanned documents and photos

NER(named entity recognization):- NER is an method which is used for recognizing entities that are present in the text document

## Installation Process in linux

for installing the library just open the command and write the following command pip install -r required.txt. Before installing the pytesseract, first install the following command 1. sudo apt install tesseract-ocr 2. sudo apt install libtesseract-dev after that install pytessaract via pip command.
for installing the spacy,follow the link provided https://spacy.io/usage


## Division of the project

This project divided into four catogaries

### 1. Data Preparation 
In this part, we have done the data preparation using the preparation.ipynb in which the image which is converted into the data with the help of pytesseract and after than we have converted into the csv format (all_invoice.csv) and after that we have done created one column which we have named as tag and after that we have done mannual labeling(for labeling we use BIO tagging format) and after that we converted into tab delimated text format(all_invoice.*txt)

BIO(Beginning Inside outsid):- The BIO / IOB format (short for inside, outside, beginning) is a common tagging format for tagging tokens in a chunking task in computational linguistics (ex. named-entity recognition). The B- prefix before a tag indicates that the tag is the beginning of a chunk, and an I- prefix before a tag indicates that the tag is inside a chunk. The B- tag is used only when a tag is followed by a tag of the same type without O tokens between them. An O tag indicates that a token belongs to no entity / chunk.

### 2. Data preprocessing

In this part 
