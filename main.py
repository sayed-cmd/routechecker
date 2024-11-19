from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
import io

app = Flask(__name__)

# একটি গ্লোবাল ডাটাবেজ ধারণকারী তালিকা
database = []

# গুগল শিটের লিংক
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1176WIxKQSyxeexL9uOSdD2fSi19AhVSul1MtnSKWLfI/export?format=csv&gid=0"

@app.route('/')
def index():
    return render_template('index.html')  # প্রধান HTML ফাইল লোড করবে

@app.route('/get-data-from-google-sheet', methods=['POST'])
def get_data_from_google_sheet():
    global database

    try:
        # গুগল শিট থেকে CSV ডেটা সংগ্রহ করা
        response = requests.get(GOOGLE_SHEET_URL)
        response.raise_for_status()

        # টেক্সট ডেটা ফাইলের মতো প্রক্রিয়া করা
        csv_text = response.content.decode('utf-8')  # সঠিক UTF-8 এনকোডিং নিশ্চিত

        # ডেটা পাণ্ডাস দিয়ে প্রক্রিয়া করা
        df = pd.read_csv(io.StringIO(csv_text))

        # নিশ্চিত করুন কলাম হেডারগুলো সঠিক
        if list(df.columns) != ["TRACKING_ID", "DELIVERY_ADDRESS", "Route"]:
            return jsonify({"success": False, "message": "Invalid Google Sheet format"})

        # ডাটাবেজ রিসেট করে নতুন ডেটা সংযুক্ত করা
        database = df.to_dict(orient='records')

        return jsonify({"success": True, "message": f"{len(database)} rows loaded successfully!"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Failed to load data: {str(e)}"})



@app.route('/reset-database', methods=['POST'])
def reset_database():
    global database
    database = []  # ডাটাবেজ ফাঁকা করা
    return jsonify({"success": True, "message": "Database reset successfully!"})

@app.route('/get-data', methods=['GET'])
def get_data():
    global database

    print("Current database:", database)  # সার্ভারে থাকা ডেটা প্রিন্ট করে দেখুন

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


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
