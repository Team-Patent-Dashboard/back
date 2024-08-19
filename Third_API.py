from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# CSV 파일을 로드하여 데이터프레임 생성
file_path = '/mnt/data/df_2.csv'  # 실제 파일 경로로 변경 필요
df = pd.read_csv(file_path)


@app.route('/api/article_analysis', methods=['POST'])
def analyze_article():
    # POST 요청에서 ID 추출
    article_id = request.json.get('id')

    # 주어진 ID로 기사를 찾기
    article = df[df['cluster_num'] == article_id]

    if article.empty:
        return jsonify({"error": "Article not found"}), 404

    article_text =
    #full text 대입

    # 예시로 분석된 특허 정보 생성 (실제로는 이 부분에서 NLP나 다른 분석 기법을 사용할 수 있음)
    patent_info = {
        "Patent_Name": "1",
        "summary": "요약",
        "link": "http://kportal.kipris.or.kr/kportal/search/total_search.do"
    }

    # Response 데이터 구성
    response = {
        "original_article_text": article_text,
        "related_patent_info": [patent_info]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
