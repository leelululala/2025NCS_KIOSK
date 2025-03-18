
drinks=["ice americano","cafe latte","Watermelon juice"]
prices=[2000,3000,4900]
total_price=0

amounts=[0]*len(drinks)



def order_process(idx: int):
    """
    Functions that address the beverage order display function,
    the total cumulative amount ajjeogu
    :param idx: list's index number
    """
    global total_price
    print(f"{drinks[idx]} ordered. Price: {prices[idx]} won")
    total_price += prices[idx]
    amounts[idx] += 1



menu_lists="".join(f"{k+1}) {drinks[k]} {prices[k]}won  " for k in range(len(drinks)))
menu_lists+=f"{len(drinks)+1}) Exit: "

help(order_process)
while True:

    menu = int(input(menu_lists))
    if 1<=menu<=len(drinks):
        order_process(menu-1)
    elif menu==len(drinks)+1:
        print("finish order~")
        break
    else:
        print(f"{menu} menu is not exist. pleas choose from above menu.")


print("Product  Price  Amount  Total")
for i in range(len(drinks)):
    if amounts[i]>0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")

print(f"total price: {total_price}")
