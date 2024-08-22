from flask import Flask, request, jsonify
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# 엑셀 파일 경로 설정 (로컬 환경에서 사용 시 경로 수정 필요)
file_path = "E:/Downloads_NEW/werticle_data.xlsx"

# 엑셀 파일 로드
news_patent_df = pd.read_excel(file_path)

'''
꼭 잘 되길 바랄게요
'''

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
