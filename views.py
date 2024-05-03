from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views=Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/crusade")
def Crusade():
    return render_template("crusade.html")

@views.route("/battle-reports")
def BattleReports():
    return render_template("battle-reports.html")

@views.route("/armies")
def Armies():
    return render_template("Armies.html")

@views.route("/players")
def get_json():
    return jsonify({'name': 'Kyksa', 'Army': 'Tyranids', 'Faction': 'Invaders', 'Score': 0})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home ():
    return redirect(url_for("views.home"))