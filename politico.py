from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
parties = []


@app.route("/parties", methods=["POST"])
def create_political_party():
    data = request.get_json() or {}
    party = {}
    # Ensure that all fields required to create a political party are availed.
    fields = ["id", "name", "hqAddress", "logoUrl"]
    for field in fields:
        if field not in data:
            error_message = {
                "status": 400,
                "message": f"Please include {field} in data when creating political party.",
            }
            return make_response(jsonify(error_message), 400)
        else:
            party[field] = data[field]
    # Ensure that the party id is unique and has not been used before.
    if party["id"] in [party["id"] for party in parties]:
        error_message = {
            "status": 400,
            "message": f"id needs to be unique. A party of id {party['id']} has been created before.",
        }
        return make_response(jsonify(error_message), 400)
    # Append to the list of parties.
    parties.append(party)
    response = {"status": 201, "data": [{"id": party["id"], "name": party["name"]}]}
    return make_response(jsonify(response), 201)


@app.route("/parties", methods=["GET"])
def get_all_political_parties():
    response = {"status": 200, "data": parties}
    return make_response(jsonify(response), 200)


if __name__ == "__main__":
    app.run(debug=True)
