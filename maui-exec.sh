java -Xmx1024m -jar maui2.jar train -l training/ -m output_model -v drp.rdf -f skos

java -Xmx1024m -jar maui2.jar run input.txt -m output_model -v drp.rdf -f skos