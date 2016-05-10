# coding=utf-8
__author__ = 'javon'

import sys

rdfTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF
	xmlns="http://vocab.cdmk-caribbean.net/cdmk#"
	xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
	xmlns:owl="http://www.w3.org/2002/07/owl#"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:dct="http://purl.org/dc/terms/"
	xmlns:skos="http://www.w3.org/2004/02/skos/core#"
	xmlns:skosxl="http://www.w3.org/2008/05/skos-xl#"
	xmlns:ann="http://art.uniroma2.it/ontologies/annotation#">
	"""


topLevelConcept = """
<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#ConceptScheme"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/DRM_Ontology">
	<rdf:type rdf:resource="http://www.w3.org/2008/05/skos-xl#Label"/>
	<skosxl:literalForm xml:lang="en">Disaster Recovery Management</skosxl:literalForm>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk">
	<skosxl:prefLabel rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/DRM_Ontology"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879">
	<rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
	<skos:inScheme rdf:resource="http://vocab.cdmk-caribbean.net/cdmk"/>
	<skos:topConceptOf rdf:resource="http://vocab.cdmk-caribbean.net/cdmk"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/xl_en_f27a3993">
	<rdf:type rdf:resource="http://www.w3.org/2008/05/skos-xl#Label"/>
	<skosxl:literalForm xml:lang="en">CDMK</skosxl:literalForm>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879">
	<skosxl:prefLabel rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/xl_en_f27a3993"/>
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/xl_en_f27a3993">
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879">
	<dct:created rdf:datatype="xsd:http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T21:08:54Z</dct:created>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/xl_en_f27a3993">
	<dct:created rdf:datatype="xsd:http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T21:08:54Z</dct:created>
	<dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T21:08:54Z</dct:modified>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879">
	<dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T21:09:33Z</dct:modified>
</rdf:Description>

"""

topLevelConceptFuseki = """
<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk">
    <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#ConceptScheme"/>
	<skos:prefLabel xml:lang="en">Disaster Recovery Management</skos:prefLabel>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879">
	<rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
	<skos:inScheme rdf:resource="http://vocab.cdmk-caribbean.net/cdmk"/>
	<skos:topConceptOf rdf:resource="http://vocab.cdmk-caribbean.net/cdmk"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879">
	<skos:prefLabel xml:lang="en">CDMK</skos:prefLabel>
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
	<dct:created rdf:datatype="xsd:http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T21:08:54Z</dct:created>
    <dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T21:09:33Z</dct:modified>
</rdf:Description>
"""

elementDescription = """
<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
	<skos:inScheme rdf:resource="http://vocab.cdmk-caribbean.net/cdmk"/>
	<skos:broader rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#xl_en_b7d2aa081%(count)d">
	<rdf:type rdf:resource="http://www.w3.org/2008/05/skos-xl#Label"/>
	<skosxl:literalForm xml:lang="en">%(term)s</skosxl:literalForm>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<skosxl:prefLabel rdf:resource="http://vocab.cdmk-caribbean.net/cdmk#xl_en_b7d2aa081%(count)d"/>
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#xl_en_b7d2aa081%(count)d">
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<dct:created rdf:datatype="xsd:http://www.w3.org/2001/XMLSchema#dateTime">2016-03-31T04:32:05Z</dct:created>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#xl_en_b7d2aa081%(count)d">
	<dct:created rdf:datatype="xsd:http://www.w3.org/2001/XMLSchema#dateTime">2016-03-31T04:32:05Z</dct:created>
	<dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-31T04:32:05Z</dct:modified>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-31T04:32:05Z</dct:modified>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<skos:definition rdf:resource="http://vocab.cdmk-caribbean.net/cdmk#def_63e3c550%(count)d"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#def_63e3c550%(count)d">
	<rdf:value xml:lang="en">%(description)s</rdf:value>
	<dct:created rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-30T22:22:53Z</dct:created>
</rdf:Description>
"""

elementDescriptionFuskei = """
<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
	<skos:inScheme rdf:resource="http://vocab.cdmk-caribbean.net/cdmk"/>
	<skos:broader rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/c_e34f6879"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_893a08ac1%(count)d">
	<skos:prefLabel xml:lang="en">%(term)s</skos:prefLabel>
	<dct:created rdf:datatype="xsd:http://www.w3.org/2001/XMLSchema#dateTime">2016-03-31T04:32:05Z</dct:created>
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
	<dct:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2016-03-31T04:32:05Z</dct:modified>
	<skos:definition xml:lang="en">%(description)s</skos:definition>
</rdf:Description>

"""

broader = """
<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_%(count)d">
	<rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
	<skos:inScheme rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/CDMK"/>
	<skos:broader rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/Disaster_Recovery"/>
</rdf:Description>

<rdf:Description rdf:about="http://vocab.cdmk-caribbean.net/cdmk#c_%(count)d">
	<skosxl:prefLabel rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/%(validterm)s"/>
	<hasStatus xmlns="http://art.uniroma2.it/ontologies/vocbench#">Proposed</hasStatus>
</rdf:Description>
"""

hastop = """<skos:hasTopConcept rdf:resource="http://vocab.cdmk-caribbean.net/cdmk/%(term)s"/>"""
endTag = """</rdf:RDF>"""

def read_phrase(fo,delimiter):
    char = fo.read(1)

    if char == ",":
        return ""

    if char =="\r":
        fo.read(1)
        char = fo.read(1)
    if char == "\"":
        char = fo.read(1)
        delimiter = "\""
    phrase = ""
    while char != delimiter:
        phrase += char
        char = fo.read(1)
    if "Post-disaster" in phrase:
        print "here"
    return phrase

def build_fuseki():
    filename = sys.argv[1]
    name = filename.split('.')[0]
    fp = open(filename, "r")
    of = open(name + "_fuseki.rdf", "w")
    of.write(rdfTemplate)
    of.write(topLevelConceptFuseki)
    count = 0
    term = read_phrase(fp, ",")
    description = read_phrase(fp, "\n")
    while term != "":
        print term
        data = {"term": term, "description": description, "count": count}
        count += 1
        of.write(elementDescriptionFuskei % data)
        term = read_phrase(fp, ",")
        if term != "":
            description = read_phrase(fp, "\n")

    of.write(endTag)
    of.close()
    fp.close()

literal_form = "<skosxl:literalForm xml:lang=\"en\">"
pref_form = "<skosxl:prefLabel"
pref_label = """<skos:prefLabel xml:lang="en">%(term)s</skos:prefLabel>"""

def translate_vocbench_to_fuseki():
    filename = sys.argv[1]
    name = filename.split('.')[0]
    fp = open(filename, "r")
    of = open(name + "_fuseki.rdf", "w")
    file_data = fp.read()
    fp.close()
    start_index = 0
    length = len(file_data)
    data ={}
    while literal_form in file_data:
        start_index = file_data.find(literal_form, start_index)
        if start_index == -1:
            break
        deletion_start = start_index
        start_index = file_data.find(">",start_index)+1
        end_index = file_data.find("<",start_index)
        term = file_data[start_index:end_index]
        data['term'] = term
        deletion_end = file_data.find(">",end_index)+1
        file_data = file_data[0:deletion_start] + file_data[deletion_end:length]
        start_index = file_data.find(pref_form,end_index)
        end_index = file_data.find(">",start_index) + 1
        file_data = file_data[0:start_index] + (pref_label % data) + file_data[end_index:length]
    of.write(file_data)
    of.close()
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: converter.py <filename>"
    else:
        translate_vocbench_to_fuseki()
