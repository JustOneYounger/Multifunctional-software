import folium
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout

from Multifunctionalsoftware.soft import *


class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self, url):
        self.setUrl(url)


class initconfig(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 初始化网页组件
        self.mywebdict = self.web_dictory()
        web_layout = QVBoxLayout()
        web_layout.setContentsMargins(0, 0, 0, 0)
        self.init_web = WebEngineView()
        web_layout.addWidget(self.init_web)
        self.frame_web_show_0.setLayout(web_layout)
        self.init_web.load(QUrl("https://www.baidu.com/"))

        self.comboBox_quick_web.currentIndexChanged.connect(self.web_combobox_changed)
        self.tabWidget_webs.currentChanged.connect(self.changespinx_index)
        self.spinBox_web_index.valueChanged.connect(self.changetab_index)

        # 初始化地图组件
        self.textBrowser_map.setText("地图加载较为缓慢，请耐心等候\n"
                                     "地图默认使用常规高德地图\n"
                                     "默认经纬度为北京\n"
                                     "可点击经纬度查询进行经纬度获取\n"
                                     "比例参数范围为0-18")
        self.mymapdict = self.map_dictory()
        Map = folium.Map([float(self.lineEdit_latitude.text()), float(self.lineEdit_longitude.text())],
                         tiles=self.mymapdict[self.comboBox_map_types.currentText()],
                         attr=self.comboBox_map_types.currentText(),
                         zoom_start=self.spinBox_map_proportion.value(),
                         )
        Map.add_child(folium.LatLngPopup())  # 显示鼠标点击点经纬度
        Map_html = Map.get_root().render()  # Map转化为html
        map_layout = QVBoxLayout()
        map_layout.setContentsMargins(0, 0, 0, 0)
        self.qwebengine_map = QWebEngineView()
        map_layout.addWidget(self.qwebengine_map)
        self.frame_map.setLayout(map_layout)
        self.qwebengine_map.setHtml(Map_html)

    def map_dictory(self):
        map_dict = {
            "高德-常规图": "https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7",
            "高德-中英文对照": "https://webrd02.is.autonavi.com/appmaptile?lang=zh_en&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
            "高德-纯英文对照": "https://webrd02.is.autonavi.com/appmaptile?lang=en&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
            "高德-卫星影像图": "https://webst02.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}",
            "高德-街道路网图": "https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=8&ltype=11",
            "中国行政区划边界": "http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/administrative_division_boundaryandlabel/MapServer/tile/{z}/{y}/{x}",
            "水系专题": "http://thematic.geoq.cn/arcgis/rest/services/ThematicMaps/WorldHydroMap/MapServer/tile/{z}/{y}/{x}",
            "街道网图": "http://thematic.geoq.cn/arcgis/rest/services/StreetThematicMaps/Gray_OnlySymbol/MapServer/tile/{z}/{y}/{x}",
            "腾讯地图": "https://rt0.map.gtimg.com/tile?z={z}&x={x}&y={-y}",
        }
        return map_dict

    def web_dictory(self):
        web_dict = {
            "百度": "https://www.baidu.com/",
            "百度翻译": "https://fanyi.baidu.com/mtpe-individual/multimodal#/",
            "必应": "https://cn.bing.com/",
            "知乎": "https://www.zhihu.com/",
            "小红书": "https://www.xiaohongshu.com/explore",
            "CSDN": "https://www.csdn.net/"
        }
        return web_dict

    def web_combobox_changed(self):
        self.lineEdit_web_url_input.setText(self.mywebdict[self.comboBox_quick_web.currentText()])

    def changespinx_index(self):
        self.spinBox_web_index.setValue(self.tabWidget_webs.currentIndex())

    def changetab_index(self):
        self.tabWidget_webs.setCurrentIndex(self.spinBox_web_index.value())
