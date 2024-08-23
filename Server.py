from flask import Flask, request, jsonify
import pandas as pd
import requests  # If needed for web scraping
from bs4 import BeautifulSoup  # If needed for parsing HTML content

app = Flask(__name__)

# Load Excel file for the data
file_path = "E:/Downloads_NEW/werticle_data.xlsx"
news_patent_df = pd.read_excel(file_path)

from flask import Flask, jsonify

app = Flask(__name__)

### 첫번째 API
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
    app.run(debug=True, port=5000)  # 포트 설정


### 두번째 api
@app.route('/api/all_news', methods=['GET'])
def get_all_news():
    # 전체 뉴스 데이터를 추출
    all_news_data = news_patent_df.drop_duplicates(subset='news_index')

    # 데이터 형식 변환 (JSON 형식으로 변환)
    news_list = []
    for _, row in all_news_data.iterrows():
        news_list.append({
            "id": int(row['news_index']),
            "title": row['news_title'],
            "description": row['news_description'],
            "keyword": row['news_keyword'],
            "source": row['news_link']
        })

    # JSON 응답
    return jsonify(news_list)


if __name__ == '__main__':
    app.run(debug=True)


### 세번째 api
@app.route('/api/article_analysis', methods=['POST'])
def analyze_article():
    news_id = request.json.get('id')

    # 뉴스 ID에 해당하는 뉴스 기사 정보 가져오기
    article_data = news_patent_df[news_patent_df['news_index'] == news_id]

    if article_data.empty:
        return jsonify({"error": "Article not found"}), 404

    # 기사 URL 가져오기
    article_url = article_data.iloc[0]['news_link']

    # HTTP GET 요청을 통해 HTML 콘텐츠 가져오기
    try:
        response = requests.get(article_url)
        response.raise_for_status()
        html_content = response.text
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to retrieve article: {str(e)}"}), 500

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html_content, 'html.parser')

    # 특정 태그를 기반으로 기사 본문 추출 (예시는 <p> 태그)
    paragraphs = soup.find_all('p')
    article_text = "\n".join([p.get_text() for p in paragraphs])

    # 기사 정보 구성
    article_info = {
        "title": article_data.iloc[0]['news_title'],
        "keyword": article_data.iloc[0]['news_keyword'],
        "full_text": article_text,
    }

    # 관련 특허 정보 추출 (특허 3개씩 제공)
    patents = []
    for i in range(min(3, len(article_data))):  # 3개의 특허를 선택
        patent_info = {
            "patent_title": article_data.iloc[i]['patent_title'],
            "patent_description": article_data.iloc[i]['recommended_patent_summary'],
            "patent_link": article_data.iloc[i]['patent_link'],
        }
        patents.append(patent_info)

    # 응답 데이터 구성
    response = {
        "article": article_info,
        "related_patents": patents
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)






