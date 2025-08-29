from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        
        req_data = request.get_json()

        if not req_data or 'data' not in req_data:
            return jsonify({
                "is_success": False,
                "user_id": "dinesh_bhandari_01012005", 
                "error": "Missing 'data' key in request body."
            }), 400

        data = req_data['data']
        
        user_id = "dinesh_bhandari_01012005"
        email = "dinesh.bhandari2022@vitstudent.ac.in"
        roll_number = "22BML0062"

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alpha_chars_for_concat = []

        for item in data:
            if isinstance(item, str):
                if item.isalpha():
                    alphabets.append(item.upper())
                    alpha_chars_for_concat.extend(list(item))
                elif item.isnumeric():
                    num = int(item)
                    total_sum += num
                    if num % 2 == 0:
                        even_numbers.append(item)
                    else:
                        odd_numbers.append(item)
                else:
                    special_characters.append(item)
        
        alpha_chars_for_concat.reverse()
        concat_string = "".join(
            [char.upper() if i % 2 == 0 else char.lower() 
             for i, char in enumerate(alpha_chars_for_concat)]
        )

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "user_id": "YOUR_FULL_NAME_DDMMYYYY",
            "error": f"An error occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)