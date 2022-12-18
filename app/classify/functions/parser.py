from selectolax.parser import HTMLParser
from app.schemas import *
import re


class Parser:
  def __init__(self, classifier = Classifier):
    html_regex = "<(\"[^\"]*\"|'[^']*'|[^'\">])*>"
    self.html_regex = re.compile(html_regex)
    self.classifier = classifier
    self.explicitly_excluded_regex = re.compile("|".join(self.classifier.explicitly_excluded_strings))
  
  def parse_single(self, text):
    tree = HTMLParser(text)
    tree = tree.text(separator=' ', strip=True)
    tree = re.sub(self.explicitly_excluded_regex,' ',tree).strip()
    tree = re.sub('  ', ' ', tree).strip()
    tree = re.sub('\|', '｜', tree).strip()
    return tree

  def parse(self, texts):
    lined_targets = []
    for text in texts:
      if re.search(self.html_regex, text):
        entry = self.parse_single(text)
      else:
        entry = re.sub("\n", "", text)
      lined_targets.append(entry)
    return lined_targets
