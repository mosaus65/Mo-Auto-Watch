import json
import time
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super_secret_key_change_me"

ADMIN_PASSWORD = "admin123"

def load_profile():
    with open("links.json", "r") as file:
        return json.load(file)

def save_profile(data):
    with open("links.json", "w") as file:
        json.dump(data, file, indent=4)

@app.route("/")
def home():
    profile_data = load_profile()
    return render_template("index.html", profile=profile_data)

@app.route("/click/<int:link_id>")
def click_track(link_id):
    profile = load_profile()
    target_url = None
    
    for category in profile.get("categories", []):
        for link in category.get("links", []):
            if link.get("id") == link_id:
                link["clicks"] = link.get("clicks", 0) + 1
                target_url = link.get("url")
                break
        if target_url:
            break
            
    if target_url:
        save_profile(profile)
        return redirect(target_url)
    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("admin"))
        else:
            error = "Invalid password!"
    return f'''
        <div style="max-width:320px;margin:100px auto;font-family:sans-serif;background:#0f172a;color:#fff;padding:2rem;border-radius:12px;text-align:center;">
            <h2>Admin Login</h2>
            {"<p style='color:#ef4444;'>"+error+"</p>" if error else ""}
            <form method="POST">
                <input type="password" name="password" placeholder="Enter Admin Password" required style="width:100%;padding:0.75rem;margin-bottom:1rem;border-radius:8px;border:1px solid #334155;background:#1e293b;color:#fff;box-sizing:border-box;">
                <button type="submit" style="width:100%;padding:0.75rem;border-radius:8px;background:#25D366;border:none;font-weight:bold;cursor:pointer;">Login</button>
            </form>
        </div>
    '''

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("home"))

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
        
    profile = load_profile()
    
    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "update_profile":
            profile["name"] = request.form.get("name")
            profile["handle"] = request.form.get("handle")
            profile["bio"] = request.form.get("bio")
            profile["avatar"] = request.form.get("avatar")
            save_profile(profile)
            
        elif action == "add_link":
            new_title = request.form.get("title")
            new_url = request.form.get("url")
            new_class = request.form.get("class", "email")
            cat_index = int(request.form.get("category_index", 0))
            
            icon_map = {
                "tiktok": "fab fa-tiktok",
                "facebook": "fab fa-facebook-f",
                "whatsapp": "fab fa-whatsapp",
                "youtube": "fab fa-youtube",
                "email": "fas fa-envelope"
            }
            
            new_link = {
                "id": int(time.time()),
                "title": new_title,
                "url": new_url,
                "class": new_class,
                "icon": icon_map.get(new_class, "fas fa-link"),
                "clicks": 0
            }
            
            profile["categories"][cat_index]["links"].append(new_link)
            save_profile(profile)

        return redirect(url_for("admin"))

    return render_template("admin.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)