import svgwrite

svg_document = svgwrite.Drawing(filename= "test.svg", size = ("800px", "600px"))

svg_document.save()
