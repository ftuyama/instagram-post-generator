import datetime

def today_string():
    return datetime.datetime.today().strftime('%Y-%m-%d')

def post_page(index):
    return f"posts/{today_string()}-{index}.png"

def post_image(final=False):
    if final:
        return f"posts/{today_string()}-final.png"
    else:
        return f"posts/{today_string()}.png"
