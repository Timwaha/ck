#!/usr/bin/python

import csv
import os

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET


with open('metrics.csv', 'w') as csvfile:

	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	fieldnames = ['Version', 'ANA', 'CIS', 'DAM', 'DCC', 'MFA', 'MOA', 'NOM', 'NOPM', 'DSC', 'NOH', 'Reusability', 'Effectiveness', 'Extendibility', 'Functionality', 'Understandability', 'TLOC']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	folder_path = "/Users/mac/Desktop/M3QMOOD/xmls/"
	print "Parsing..."

	for xml in sorted(os.listdir(folder_path)):

		if "xml" in xml :

			filename = folder_path + xml
			# print filename

			tree = ET.ElementTree(file=filename)
			root = tree.getroot()

			version = root.get('scope')
			print version

			# ANA
			ana = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="ANA"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				ana = value.get('value')

			# CIS
			cis = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="CIS"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="type"]')
				cis = value.get('avg')

			# DAM
			dam = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="DAM"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="type"]')
				dam = value.get('avg')

		    # DCC
			dcc = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="DCC"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="type"]')
				dcc = value.get('avg')

		    # MFA
			mfa = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="MFA"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="packageFragment"]')
				mfa = value.get('avg')

			# MOA
			moa = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="MOA"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="packageFragment"]')
				moa = value.get('total')

			# NOM
			nom = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="NOM"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="type"]')
				nom = value.get('avg')

			# NOPM
			nopm = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="NOPM"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Values[@per="packageFragment"]')
				nopm = value.get('total')

			# DSC
			dsc = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="DSC"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				dsc = value.get('value')

			# NOH
			noh = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="NOH"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				noh = value.get('value')

			# Reusability
			reu = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="REU"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				reu = value.get('value')

			# Flexibility
			fle = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="FLE"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				fle = value.get('value')

			# Effectiveness
			eff = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="EFE"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				eff = value.get('value')

			# Extendibility
			ext = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="EXT"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				ext = value.get('value')

			# Functionality
			fun = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="FUN"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				fun = value.get('value')

			# Understandability
			und = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="ENT"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				und = value.get('value')

			# TLOC
			tloc = ''
			for metric in root.findall('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Metric[@id="TLOC"]'):
				value = metric.find('{http://metrics.sourceforge.net/2003/Metrics-First-Flat}Value')
				tloc = value.get('value')

			writer.writerow({'Version':version, 'ANA':ana, 'CIS':cis, 'DAM':dam, 'DCC':dcc, 'MFA':mfa, 'MOA':moa, 'NOM':nom, 'NOPM':nopm, 'DSC':dsc, 'NOH':noh, 'Reusability':reu, 'Effectiveness':eff, 'Extendibility':ext, 'Functionality':fun, 'Understandability':und, 'TLOC':tloc})

	print "Done!"
