import svgwrite
import svgutils

svg_document = svgwrite.Drawing(filename= "test.svg", size = ("800px", "600px"))

svg_document.add(svg_document.rect(
  insert = (0,0),
  size = ("200px", "100px"),
  stroke_width = "1",
  stroke = "black",
  fill = "rgb(255,255,0)"))

svg_document.save()

first_svg = svgutils.transform.fromfile('spiders/spider.svg')
second_svg = svgutils.transform.fromfile('bulls/bull-silhouette.svg')

first_svg.append(second_svg)

first_svg.save('merged.svg')
