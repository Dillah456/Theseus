

Kode :
	from flask import Flask, jsonify, request, render_template
	
	import json
	import os
	
	app = Flask(__name__)
	FILE = "Inventory.json"
	
	  
	def load_inventory():
	    if not os.path.exists(FILE):
	        return []
	    with open(FILE, "r", encoding="utf-8") as f:
	        return json.load(f)
	
	  
	def save_inventory(data):
	    with open(FILE, "w", encoding="utf-8") as f:
	        json.dump(data, f, indent=2, ensure_ascii=False)
	
	@app.route("/")
	def index():
	    return render_template("index.html")
	

	@app.route("/api/inventory", methods=["GET"])	
	def get_inventory():
	    return jsonify(load_inventory())
	
	  
	@app.route("/api/inventory", methods=["POST"])
	def save_all_inventory():
	    data = request.get_json()
	    save_inventory(data)
	    return jsonify({"status": "saved"})
	
	@app.route("/api/inventory/add", methods=["POST"])
	def add_item():
	    inventory = load_inventory()
	    item = request.get_json()
	    inventory.append(item)
	
	    save_inventory(inventory)
	
	    return jsonify({"status": "added"})
	
	
	@app.route("/api/inventory/update", methods=["POST"])
	def update_qty():
	    payload = request.get_json()
	    inventory = load_inventory()
	
	    for item in inventory:	
	        if item["Id"] == payload["Id"]:
	            item["Quantity"] = payload["Quantity"]
	
	    save_inventory(inventory)
	    return jsonify({"status": "updated"})
	
	@app.route("/api/inventory/delete", methods=["POST"])
	def delete_item():
	    payload = request.get_json()
	    inventory = load_inventory()
	    inventory = [i for i in inventory if i["Id"] != payload["Id"]]
	
	    save_inventory(inventory)
	
	    return jsonify({"status": "deleted"})
	  
	
	if __name__ == "__main__":
	    app.run(debug=True)