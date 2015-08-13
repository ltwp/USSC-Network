class Case(object):
  """Represents one Supreme Court Case."""

  def __init__(self,year=1000,id_num=0,citations=[]):
    self.year = year
    self.id_num = id_num
    self.citations = citations

  def __str__(self):
    print 'Case no. %s from %s. It cites the following:' % (self.id_num, self.year)
    print self.citations
    return ''

cases = dict()

fin = open('ussc_cites_small.txt')
for line in fin:
  line = line.strip();
  line = line.split(',')
  # CITED, CITING
  cited = line[0].split()
  citing = line[1].split()
  # 0th is year, 3th is id_num

  if citing[3] not in cases:
    # we're gonna make an object  for the citing case and put it in our dictionary
    case = Case(citing[0],citing[3],[cited[3]])
    cases[citing[3]] = case
  else:
    case = cases[citing[3]]
    case.citations.append(cited[3])

#################################################################

import networkx as nx
G = nx.DiGraph()

for c in cases:
  #print cases[c].id_num

  #G.add_node(cases[c].id_num)
  # Uses case numbers as nodes. Maybe we should use case objects?
  G.add_node(cases[c])

  #print cases[c].citations
  for k in cases[c].citations:
    if k in cases:
      G.add_edge(cases[c],cases[k])
    else:
      #print 'oops! Tried to draw an edge to a case that does not exist yet.'

#G.nodes()
#G.edges()

#G.degree(cases['202'])

#################################################################

import matplotlib.pyplot as plt
