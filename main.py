import sys
import webbrowser
import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView,
    QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from io import BytesIO


class NewsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("News Crawler App")
        self.setGeometry(100, 100, 900, 600)

        self.layout = QVBoxLayout(self)

        self.label = QLabel("네이버 뉴스 인기기사 크롤러")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.button = QPushButton("인기 기사 가져오기")
        self.button.clicked.connect(self.fetch_news)
        self.layout.addWidget(self.button)

        # 테이블: 썸네일 | 제목 | 이동 버튼
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["썸네일", "제목", "사이트 이동"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.layout.addWidget(self.table)

    def fetch_news(self):
        url = "https://news.naver.com/section/105"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        # 기사 리스트 가져오기 (예시: 헤드라인 뉴스 기준)
        news_items = soup.select(".sa_list .sa_item")[:6]

        self.table.setRowCount(len(news_items))

        for i, news_item in enumerate(news_items):
            img = news_item.select_one("img")
            title = news_item.select_one(".sa_text_strong").get_text(strip=True)
            print("111")
            # img_tag = a_tag.select_one("img")
            # title = img_tag.get("alt") if img_tag else "제목 없음"
            # img_url = img_tag.get("src") if img_tag else None

            # if img_url:
            #     try:
            #         img_data = requests.get(img_url).content
            #         pixmap = QPixmap()
            #         pixmap.loadFromData(img_data)
            #         thumbnail_label = QLabel()
            #         thumbnail_label.setPixmap(pixmap.scaled(100, 60, Qt.KeepAspectRatio))
            #     except:
            #         thumbnail_label = QLabel("이미지 오류")
            # else:
            #     thumbnail_label = QLabel("없음")
            #
            # # 제목
            # title_item = QTableWidgetItem(title)
            #
            # # 사이트 이동 버튼
            # go_btn = QPushButton("이동")
            # go_btn.clicked.connect(lambda _, url=link: webbrowser.open(url))
            #
            # # 테이블에 삽입
            # self.table.setCellWidget(i, 0, thumbnail_label)
            # self.table.setItem(i, 1, title_item)
            # self.table.setCellWidget(i, 2, go_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NewsApp()
    window.show()

    sys.exit(app.exec())
