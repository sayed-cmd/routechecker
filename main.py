from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# একটি গ্লোবাল ডাটাবেজ ধারণকারী তালিকা
database = []

@app.route('/')
def index():
    return render_template('index.html')  # প্রধান HTML ফাইল লোড করবে

@app.route('/upload-excel', methods=['POST'])
def upload_excel():
    global database

    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part in the request"})

    file = request.files['file']

    if file.filename == '':
        return jsonify({"success": False, "message": "No file selected"})

    try:
        # পাণ্ডাস দিয়ে এক্সেল ফাইলটি লোড করা
        df = pd.read_excel(file)

        # নিশ্চিত করুন কলাম হেডারগুলো সঠিক
        if list(df.columns) != ["TRACKING_ID", "DELIVERY_ADDRESS", "Route"]:
            return jsonify({"success": False, "message": "Invalid file format"})

        # ডাটাবেজ রিসেট করে নতুন ডেটা সংযুক্ত করা
        database = df.to_dict(orient='records')

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/reset-database', methods=['POST'])
def reset_database():
    global database
    database = []  # ডাটাবেজ ফাঁকা করা
    return jsonify({"success": True})

@app.route('/get-data', methods=['GET'])
def get_data():
    global database

    tracking_id = request.args.get('id')
    if not tracking_id:
        return jsonify({"success": False})

    # ডাটাবেজ থেকে তথ্য অনুসন্ধান করা
    for record in database:
        if record['TRACKING_ID'] == tracking_id:
            return jsonify({
                "success": True,
                "tracking_id": record['TRACKING_ID'],
                "address": record['DELIVERY_ADDRESS'],
                "route": record['Route']
            })

    return jsonify({"success": False})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)

