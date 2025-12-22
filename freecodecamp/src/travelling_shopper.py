#Currency conversion rates dictionary
conversion_rates = {
    "USD": 1.00,
    "EUR": 1.10,
    "GBP": 1.25,
    "JPY": 0.0070,
    "CAD": 0.75
}

def convert_currency(item, prices_list):
    converted_amount = 0;
    converted_price = 0;

    amount = float(item[0])

    currency = item[1]
    #print(f"{amount} {currency}")
    converted_prices = []


    if currency in conversion_rates:
        conversion_rate = conversion_rates[currency]
        converted_amount = amount * conversion_rate
        #print(f"Amount: {amount}, conversion rate: {conversion_rate}, converted_amount: {converted_amount}")
    else:
        converted_amount = 0


    for price in prices_list:
        currency = price[1]

        if currency in conversion_rates:
            conversion_rate = conversion_rates[currency]
            converted_price = float(price[0]) * conversion_rate
            #print(f"{converted_price} {currency}")
            converted_prices.append(converted_price)
            #print(f"{converted_prices}")
        else:
            converted_price = 0
            converted_prices.append(converted_price)



    #print(f"{converted_amount} {converted_prices}")
    return converted_amount, converted_prices



def buy_items(funds, items):
    converted_amount, converted_prices = convert_currency(funds, items)
    #print(converted_amount, converted_prices)
    sum_converted_prices = sum(converted_prices)
    #print(f"The total sum of all items is: {sum_converted_prices}")

    if sum_converted_prices <= converted_amount:
        print("Buy them all!")
        return "Buy them all!"
    else:
        #print("You don't have enough funds to buy all of them!")
        partial_sum = 0
        items_in_cart_counter = 0

        for element in converted_prices:
            if partial_sum < converted_amount:
                if partial_sum + element <= converted_amount:
                    partial_sum += element
                    items_in_cart_counter += 1

                else:
                    break
        # print(f"You can afford buying up to {partial_sum} USD, which correpond to {items_in_cart_counter} items.")
        print(f"Buy the first {items_in_cart_counter} items.")
        return f"Buy the first {items_in_cart_counter} items."



buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) # "Buy the first 2 items."
#convert_currency(["150.00", "USD"])
#convert_currency(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]])
buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) # "Buy them all!"
#convert_currency(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]])
buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]) #"Buy the first 5 items."
#convert_currency(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]])
buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) #"Buy the first 3 items.".