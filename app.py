"""Flask web and JSON interfaces for the tax calculator."""

import os

from flask import Flask, jsonify, render_template, request

from tax import calculate_tax


app = Flask(__name__)


def _calculation_values(income, status):
    tax = calculate_tax(income, status)
    amount = float(income)
    effective_rate = tax / amount if amount else 0.0
    return amount, tax, effective_rate


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/calculate")
def calculate():
    income = request.form.get("income", "")
    status = request.form.get("status", "")
    try:
        amount, tax, effective_rate = _calculation_values(income, status)
    except ValueError as error:
        return str(error), 400
    return render_template(
        "result.html", income=amount, status=status, tax=tax,
        effective_rate=effective_rate,
    )


@app.get("/api/calculate")
def api_calculate():
    income = request.args.get("income", "")
    status = request.args.get("status", "")
    try:
        amount, tax, effective_rate = _calculation_values(income, status)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    return jsonify({
        "income": amount,
        "status": status,
        "tax": tax,
        "effective_rate": effective_rate,
    })


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
