import datetime

def today_string():
    return datetime.datetime.today().strftime('%Y-%m-%d')

def post_page(index):
    return f"posts/{today_string()}-{index}.png"
