from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/main_news', methods=['GET'])
def get_main_news():
    news_data = [
        {
            "id": 0,
            "imageUrl": "https://image.zdnet.co.kr/2024/08/13/aa86b3dbd68e57f31cf81aaed686db53.jpg",
            "title": "현대차 직원은 출입증도 달라…전자잉크 LCD 사원증 특허   ",
            "keyword": "핵심 키워드1",
            "source": "https://zdnet.co.kr/view/?no=20240813130506"
        },
        {
            "id": 1,
            "imageUrl": "https://img8.yna.co.kr/etc/inner/KR/2024/08/12/AKR20240812087600003_01_i_P4.jpg",
            "title": "반도건설, 특허출원 지하 구조물 시공법 현장 첫 적용",
            "keyword": "핵심 키워드2",
            "source": "https://www.yna.co.kr/view/AKR20240812087600003?input=1195m"
        },
        {
            "id": 3,
            "imageUrl": "https://dimg.donga.com/wps/NEWS/IMAGE/2024/08/13/126504667.2.png",
            "title": "시나몬랩, 새 제형의 ‘스낵형 건강기능식품’ 특허 취득",
            "keyword": "핵심 키워드3",
            "source": "https://www.donga.com/news/Economy/article/all/20240813/126504724/1"
        },
        {
            "id": 7,
            "imageUrl": "https://image.dnews.co.kr/photo/photo/2024/08/12/202408121357332990872-2-527765.jpg",
            "title": "궁중비책, 신규 키즈라인 런칭.. 특허출원성분 로얄테라티가드 함유",
            "keyword": "핵심 키워드4",
            "source": "https://www.dnews.co.kr/uhtml/view.jsp?idxno=202408121357332990872"
        },
        {
            "id": 11,
            "imageUrl": "https://cdn.eroun.net/news/photo/202408/45859_88097_298.png",
            "title": "오쎄, 천연 성분 LDSF-6 complex 성분 특허 출원 \"스포츠세제 독자성분\" ",
            "keyword": "핵심 키워드5",
            "source": "https://www.eroun.net/news/articleView.html?idxno=45859"
        }
    ]

    return jsonify(news_data)


if __name__ == '__main__':
    app.run(debug=True)
