from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

file_path = 'file 경로'
df = pd.read_csv(file_path)


@app.route('/api/all_news', methods=['GET'])
def get_all_news():
    # DataFrame을 JSON 형태로 변환
    news_data = [
        {
            "id": int(row['cluster_num']),
            "title": row['top_title'],
            "description": row['description'],
            "link": row['link']
        }
        for _, row in df.iterrows()
    ]

    return jsonify(news_data)


if __name__ == '__main__':
    app.run(debug=True)
