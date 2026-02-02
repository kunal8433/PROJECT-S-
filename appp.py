from flask import Flask, render_template_string, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "kunalclothing"

# Make sure Flask knows correct static folder
app.static_folder = os.path.join(os.path.dirname(__file__), "static")

products = [
    {"id": 1, "name": "Men T-Shirt", "price": 799, "image": "tshirt.jpg"},
    {"id": 2, "name": "Women Hoodie", "price": 1299, "image": "hoodie.jpg"},
    {"id": 3, "name": "Denim Jacket", "price": 1999, "image": "jacket.jpg"},
    {"id": 4, "name": "Oversized Shirt", "price": 999, "image": "shirt.jpg"}
]

home_html = """
<!DOCTYPE html>
<html>
<head>
<title>Kunal Clothing</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
body{font-family:Poppins;background:#f6f7fb;margin:0}
header{background:#0f172a;color:white;padding:20px}
.brand{display:flex;align-items:center;gap:12px}
.brand img{width:50px;height:50px;border-radius:50%}

a{color:white;text-decoration:none;font-weight:600}

.container{
padding:25px;
display:grid;
grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
gap:20px;
}

.card{
background:white;
border-radius:14px;
padding:15px;
text-align:center;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.card img{
width:100%;
height:200px;
object-fit:cover;
border-radius:10px;
}

.price{color:#2563eb;font-weight:600}

button{
background:#0f172a;
color:white;
border:none;
padding:8px 14px;
border-radius:8px;
cursor:pointer;
}

button:hover{background:#2563eb}

.topbar{
display:flex;
justify-content:space-between;
align-items:center;
}
</style>
</head>
<body>

<header>
<div class="topbar">
<div class="brand">
<img src="{{ url_for('static', filename='kunal.jpg') }}">
<h2>Kunal Clothing</h2>
</div>
<a href="{{ url_for('cart') }}">🛒 Cart</a>
</div>
</header>

<div class="container">
{% for p in products %}
<div class="card">
<img src="{{ url_for('static', filename=p.image) }}">
<h3>{{p.name}}</h3>
<p class="price">₹ {{p.price}}</p>

<form action="{{ url_for('add_to_cart', pid=p.id) }}" method="post">
<button>Add to Cart</button>
</form>
</div>
{% endfor %}
</div>

</body>
</html>
"""

cart_html = """
<!DOCTYPE html>
<html>
<head>
<title>Cart</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

<style>
body{font-family:Poppins;background:#f6f7fb;margin:0;padding:20px}
.box{background:white;padding:20px;border-radius:12px;max-width:600px;margin:auto}
.item{display:flex;justify-content:space-between;margin-bottom:10px}
a{text-decoration:none;color:#2563eb}
button{background:#0f172a;color:white;border:none;padding:8px 14px;border-radius:8px}
</style>
</head>
<body>

<div class="box">
<h2>Your Cart</h2>

{% if cart %}
{% for i in cart %}
<div class="item">
<span>{{i.name}}</span>
<span>₹ {{i.price}}</span>
</div>
{% endfor %}

<hr>
<p><b>Total : ₹ {{total}}</b></p>

<form action="{{ url_for('order') }}" method="post">
<button>Place Final Order</button>
</form>

<br>
<a href="{{ url_for('home') }}">← Back to shop</a>

{% else %}
<p>Your cart is empty</p>
<a href="{{ url_for('home') }}">Go shopping</a>
{% endif %}

</div>

</body>
</html>
"""

order_html = """
<!DOCTYPE html>
<html>
<head>
<title>Order</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap" rel="stylesheet">

<style>
body{font-family:Poppins;background:#f6f7fb;margin:0}
.box{
background:white;
padding:40px;
border-radius:14px;
max-width:500px;
margin:80px auto;
text-align:center;
}
a{text-decoration:none;color:#2563eb}
</style>
</head>
<body>

<div class="box">
<h2>🎉 Order Placed Successfully!</h2>
<p>Thank you for shopping with</p>
<h3>Kunal Clothing</h3>
<br>
<a href="{{ url_for('home') }}">Back to Home</a>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(home_html, products=products)


@app.route("/add/<int:pid>", methods=["POST"])
def add_to_cart(pid):
    if "cart" not in session:
        session["cart"] = []

    for p in products:
        if p["id"] == pid:
            session["cart"].append(p)

    session.modified = True
    return redirect(url_for("home"))


@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(i["price"] for i in cart_items)
    return render_template_string(cart_html, cart=cart_items, total=total)


@app.route("/order", methods=["POST"])
def order():
    session["cart"] = []
    return render_template_string(order_html)


if __name__ == "__main__":
    app.run(debug=True)
