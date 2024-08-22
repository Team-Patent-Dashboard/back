from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# 엑셀 파일 경로 설정 (로컬 환경에서 사용 시 경로 수정 필요)
file_path = "E:/Downloads_NEW/werticle_data.xlsx"

# 엑셀 파일 로드
news_patent_df = pd.read_excel(file_path)


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
