from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def puppies():
    return "<h1 style='color: red'>Puppies are cute!</h1>"

@app.route('/<animal>/<color>/<int:num>')
def display_animal(animal, color, num):

    print(f"Animal: {animal}")
    print(f"Color: {color}")
    print("Type of the num var: ", type(num))


    return render_template('index.html', animal=animal, color=color, num=num)

if __name__=="__main__": 
    app.run(debug=True)
