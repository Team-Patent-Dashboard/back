from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/main_news', methods=['GET'])
def get_main_news():
    news_data = [
        {
            "id": 0,
            "imageUrl": "https://image.zdnet.co.kr/2024/08/13/aa86b3dbd68e57f31cf81aaed686db53.jpg",
            "title": "현대차 직원은 출입증도 달라…전자잉크 LCD 사원증 특허   ",
            "keyword": "전자종이 비콘, 디스플레이 적용, 디스플레이 잉크",
            "source": "https://zdnet.co.kr/view/?no=20240813130506"
        },
        {
            "id": 12,
            "imageUrl": "https://cgeimage.commutil.kr/phpwas/restmb_allidxmake.php?pp=002&amp;idx=3&amp;simg=202408131143570751348439a487410625221173.jpg",
            "title": "애즈원, ‘LED디스플레이 장애 자동복구’ 관련 기술 미국 특허 취득해 K-Display 선두주자로 자리매김!",
            "keyword": "디스플레이 전문, 디스플레이 장애, 애즈원 한국",
            "source": "http://www.globalepic.co.kr/view.php?ud=20240813114350228448439a4874_29"
        },
        {
            "id": 28,
            "imageUrl": "https%3A%2F%2Fi3n.news1.kr%2Fsystem%2Fphotos%2F2024%2F4%2F7%2F6582621%2Fhigh.jpg",
            "title": "LG엔솔-금호석화, 전고체 배터리 소재 공동 개발…中 특허 획득",
            "keyword": "석유화학 공동, 금호 석유화학, 개발 전해질",
            "source": "https://www.news1.kr/industry/general-industry/5500016"
        },
        {
            "id": 38,
            "imageUrl": "https://newsimg.sedaily.com/2024/08/05/2DCWCQYO9T_1.jpg",
            "title": "네오아이즈, 행동 유형 검사 k-DISC 특허, 저작권 지식재산권 등록 출원 완료",
            "keyword": "재산권 확보, 직무 환경, 지식 재산권",
            "source": "https://www.sedaily.com/NewsView/2DCWCQYO9T"
        }
    ]

    return jsonify(news_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # 포트를 5001로 설정
