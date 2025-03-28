# pdf-to-csv-webscraper
_Last READ.ME update: 2025-03-28_

## Summary

This repository contains two scripts: one is meant to scrap a website, look for specific PDFs and download them. The other reads one of them, parses its sheet, nicely formating it and replace some specific abbreviations to their respective name.

## web-scraper.py

Execution:
1. Gets webpage via requests, creates soup
2. Looks for <a> tags with 'href' attribute ending in 'pdf' and containing 'Anexo'
3. Downloads PDFs on the tags
4. Adds them to a .zip named 'Teste_pdfs.zip' and unlinks the pdfs

## data-extraction-tools.py

Execution:
1. Extracts a specific PDF file inside a specific .zip file (result of previous script)
2. Uses tabula to read the sheet in it and convert to a pandas dataframe
3. Uses pandas to replace specific column abbreviations to their full name
4. Concats into a single dataframe
5. Transforms into .csv
6. Unlinks PDF
7. Adds .csv to 'Teste_LuccaMilfont.zip'