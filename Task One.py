
mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'UK'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 107.25
}

template = "{name} is made in {made}. The price is {price} which is almost equal to {converted_price:.2f} BDT."

for item in mobile_data['data']:
    price_in_usd_float = float(item['price'].replace(' USD', ''))
    item['converted_price'] = price_in_usd_float * mobile_data['exchange_rate']
    formatted_info = template.format(**item)
    print(formatted_info)