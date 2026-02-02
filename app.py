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
            font-family: 'Poppins', sans-serif;
            background:#f5f5f5;
            margin:0;
            padding:0;
        }

        header{
            background:black;
            color:white;
            padding:20px;
            text-align:center;
        }

        .container{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
            gap:20px;
            padding:20px;
        }

        .card{
            background:white;
            padding:15px;
            border-radius:10px;
            text-align:center;
        }

        .price{
            font-weight:600;
            font-size:18px;
        }
    </style>
</head>
<body>

<header>
    <h1>Kunal Clothing</h1>
    <p>Official Store</p>
</header>

<div class="container">
    {% for p in products %}
    <div class="card">
        <h3>{{ p.name }}</h3>
        <p class="price">₹ {{ p.price }}</p>
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
