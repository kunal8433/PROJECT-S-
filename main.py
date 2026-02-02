from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"name": "Men T-Shirt", "price": 799},
    {"name": "Women Hoodie", "price": 1299},
    {"name": "Denim Jacket", "price": 1999},
    {"name": "Oversized Shirt", "price": 999}
]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Kunal Clothing</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

    <style>
        body{
            font-family:'Poppins', sans-serif;
            margin:0;
            background:#f6f7fb;
        }

        header{
            background:linear-gradient(90deg,#000000,#1f2933);
            color:white;
            padding:25px;
            text-align:center;
        }

        .brand{
            display:flex;
            align-items:center;
            justify-content:center;
            gap:15px;
            margin-top:10px;
        }

        .brand img{
            width:60px;
            height:60px;
            border-radius:50%;
            object-fit:cover;
            border:2px solid white;
        }

        .container{
            padding:30px;
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
            gap:20px;
        }

        .card{
            background:white;
            padding:18px;
            border-radius:14px;
            text-align:center;
            box-shadow:0 10px 20px rgba(0,0,0,0.08);
        }

        .card h3{
            color:#111827;
        }

        .price{
            color:#2563eb;
            font-weight:600;
            font-size:18px;
        }

        .buy{
            margin-top:10px;
            padding:8px 14px;
            border:none;
            border-radius:8px;
            background:#111827;
            color:white;
            cursor:pointer;
        }

        .buy:hover{
            background:#2563eb;
        }

    </style>
</head>
<body>

<header>
    <div class="brand">
        <img src="/static/kunal.jpg">
        <h1>Kunal Clothing</h1>
    </div>
    <p>Official Personal Brand Store</p>
</header>

<div class="container">
    {% for p in products %}
    <div class="card">
        <h3>{{ p.name }}</h3>
        <p class="price">₹ {{ p.price }}</p>
        <button class="buy">Buy Now</button>
    </div>
    {% endfor %}
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, products=products)

if __name__ == "__main__":
    app.run(debug=True)
