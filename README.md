# IMAGE TO JSON CONVERTOR

## INTRODUCTION

In this project the user will upload the document image and then it convert into json(javascript object notation)

## 1.DATA COLLECTION

We used personal invoices data around 60 images.

## 2.PROCESS OF THE PROJECT

This has divided into different part which has been shown below

## data preparation

In this process we have done preparation, where we have convert the all the image into the text format in the form of .csv format and then we will annotate all the text which was generated by the ocr(optical character recognization). For labelling we use BIO(beginning inside outside) method.

## data preprocessing
In this process, firstly we have converted all the .csv which we have annoted by BIO labelling and then we have converted into the tab delimated txt format
and then we have converted txt data into the dataframe for furthur preprocessing and then converted all the preprocessing data into the test and train pickle format.

## data training
In this process, we have converted the pickle formated data into spacy format and then train the model. For converting into the spacy format from pickle we have created the preprocess file which convert into the spacy format. 

## prediction
In this process, we furthur preprocess the data and then combine the all the chunks into the one and the convert into dictinary format and after the using the help of json library it convert the dictionary format into the json format

## Web Application using flask
