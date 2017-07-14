#coding:utf8
# mailliao@163.com
# 2017.7.7
# 参考 Python Geospatial Development 3rd Edition
import mapnik
#在xml里设置标签文字的样式
mapfile = 'tm/osm.xml'
MIN_LAT = 4#-35
MAX_LAT = 55#+35
MIN_LONG = 73#-12
MAX_LONG = 135#+50
MAP_WIDTH = 700
MAP_HEIGHT = 800

#定义polygone的样式
polygonStyle = mapnik.Style()
#定义2个rule，angola用a颜色，其余用b颜色，即两个rule
#rule1
rule = mapnik.Rule()
rule.filter = mapnik.Filter("[NAME] = 'China'")
symbol = mapnik.PolygonSymbolizer()
symbol.fill = mapnik.Color("green")
rule.symbols.append(symbol)
polygonStyle.rules.append(rule)
#rule2
rule = mapnik.Rule()
rule.filter = mapnik.Filter("[NAME] != 'China'")
symbol = mapnik.PolygonSymbolizer()
symbol.fill = mapnik.Color("gray")
rule.symbols.append(symbol)
polygonStyle.rules.append(rule)

#line的样式及rule
rule = mapnik.Rule()
symbol = mapnik.LineSymbolizer()
symbol.fill = mapnik.Color("#000000")
symbol.opacity = 0.1
rule.symbols.append(symbol)
polygonStyle.rules.append(rule)
# symbol.name = "NAME"报错，说是bug，至今无较好解决方案
'''
#label的样式
labelStyle = mapnik.Style()
rule = mapnik.Rule()
symbol = mapnik.TextSymbolizer()
symbol.name = "NAME"
symbol.font_name = "DejaVu Sans Book"
symbol.size = 12
rule.symbols.append(symbol)
labelStyle.rules.append(rule)
'''
#shp数据源
datasource = mapnik.Shapefile(file="tm/" + "TM_WORLD_BORDERS-0.3.shp")
polygonLayer = mapnik.Layer("Polygons")
polygonLayer.datasource = datasource
polygonLayer.styles.append("PolygonStyle")
labelLayer = mapnik.Layer("Labels")
labelLayer.datasource = datasource
labelLayer.styles.append("labelstyle")
print("here?2")
map1 = mapnik.Map(MAP_WIDTH, MAP_HEIGHT, "+proj=longlat +datum=WGS84  +no_defs")
mapnik.load_map(map1, mapfile)
map1.background = mapnik.Color("#8080a0")
map1.append_style("PolygonStyle", polygonStyle)
#map1.append_style("LabelStyle", labelstyle)
map1.layers.append(polygonLayer)
map1.layers.append(labelLayer)
map1.zoom_to_box(mapnik.Box2d(MIN_LONG, MIN_LAT, MAX_LONG, MAX_LAT))
#map1.zoom_all()
mapnik.render_to_file(map1, "mapa.png")

