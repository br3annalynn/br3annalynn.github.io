app = Flask(__name__)
app.secret_key = "shhhhthisisasecret"
app.config.from_object(config)

@app.route("/")
def index():    
    return render_template('index.html')

# @app.route("/", methods=['POST'])
# def login():
#     submitted_name = request.form.get('name')
#     print submitted_name
#     submitted_password = request.form.get('password')
#     print submitted_password

#     user_id = model2.login(submitted_name, submitted_password)
#     if user_id:   
#         session['session_user_id'] = user_id
#         folder = model2.get_folder(user_id) 
#         session['session_folder'] = folder
#         print "Successfully loged in"
#         return redirect(url_for("display_inventory"))
#     else:
#         flash("Username or password incorect.")
#         return redirect(url_for("process_login"))
