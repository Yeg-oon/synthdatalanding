from flask import Flask, render_template, request, send_file, jsonify
import io
from data_generator import SyntheticDataGenerator

app = Flask(__name__)
generator = SyntheticDataGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_data():
    try:
        data = request.get_json()
        
        # Parse columns
        columns = {}
        for column in data['columns']:
            columns[column['name']] = column['type']
        
        row_count = int(data['rowCount'])
        noise_level = float(data['noiseLevel'])
        
        # Generate CSV
        csv_content = generator.generate_csv(columns, row_count, noise_level)
        
        # Create file in memory
        output = io.BytesIO()
        output.write(csv_content.encode('utf-8'))
        output.seek(0)
        
        return send_file(
            output,
            as_attachment=True,
            download_name='synthetic_data.csv',
            mimetype='text/csv'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
