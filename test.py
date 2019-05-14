#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import unicodecsv
import datetime
import pymysql.cursors
#import sys
#import ipdb; ipdb.set_trace()

def listerErreurs(msg):
	fichier = open("erreurs.txt", "a")
	msg = str(datetime.datetime.now()) + " : " + msg + "\n"
	fichier.write(msg)
	fichier.close()


def parserCSV():
	csv = open("file.csv", "r")
	lines = [l.strip() for l in csv]
	try:
		genererSQL(lines)
	except:
		message = "Erreur lors de la génération du SQL"
		listerErreurs(message)
	csv.close()


def genererSQL(lines):
	file = open("file.sql", "w")
	file.write("INSERT INTO `produit` (`pr_refour`, `pr_desi`, `pr_pack`, `pr_prac`, `pr_prix`, `pr_codebarre`) VALUES \n")
	i = 0
	while i < len(lines):
		if "0" <= lines[i][0] <= "9":
			line = lines[i].split(",")
			file.write("('" + str(int(float(line[0]))) + "', '" + line[2] + " " + str(int(float(line[3]))) + " ML', '" + line[4] + "', '" + line[5] + "', '" + line[6] + "', '" + str(int(float(line[7]))) + "')")
			if i != (len(lines) - 1):
				file.write(",\n")
		i = i + 1
	file.close()


def importerDonnees():
	connexion = pymysql.connect(host='localhost', user='ap', password='ap', db='produit')
	try:
		with connexion.cursor() as cursor:
			file = open("file.sql", "r")
			sql = file.read()
			file.close()
			cursor.execute(sql)
			connexion.commit()
	finally:
		connexion.close()

	#bdd = conn.cursor()
	#sql = open("file.sql", "r")
	#bdd.execute(sql)


def xls2csv(xls_filename, csv_filename):

    wb = xlrd.open_workbook(xls_filename)
    sh = wb.sheet_by_index(0)

    fh = open(csv_filename,"wb")
    csv_out = unicodecsv.writer(fh, encoding='utf-8')

    for row_number in range (sh.nrows):
        csv_out.writerow(sh.row_values(row_number))

    fh.close()


try:
	xls2csv("Rattrapage AP.XLS", "file.csv")
except:
	message = "Erreur lors de la conversion XLS vers CSV"
	listerErreurs(message)

try:
	parserCSV()
except:
	message = "Erreur lors du parsing du CSV"
	listerErreurs(message)

try:
	importerDonnees()
except:
	message = "Erreur lors de l'insertion dans la base de données"
	listerErreurs(message)
