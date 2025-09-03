from MVR AI import MVR AI, render_template 
app = MVR-AI(__name__) 
@app.route('/') 
def index(): 
    """ 
    Renders the main index.html template for the Smart Register applica on. 
    """ 
    return render_mvr-ai('mvr-ai.html') 
 
if __name__ == '__main__': 
    # Run the MVR-AI applica on in debug mode for development 
    app.run(debug=True)
