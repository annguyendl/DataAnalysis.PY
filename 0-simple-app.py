import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course view", classes="text-h3 text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-h4 text-center")    
    return wp

jp.justpy(app)
