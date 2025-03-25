class CafeOrder:
    DISCOUNT_THRESHOLD = 10000
    DISCOUNT_RATE = 0.1

    def __init__(self, drinks, prices):
        self.drinks = drinks
        self.prices = prices
        self.amounts = [0] * len(drinks)
        self.total_price = 0

    def apply_discount(self, price: int) -> float:
        """
        Apply discount rate when the total amount exceeds a certain threshold
        :param price: price before discount
        :return: price after discount
        """
        if price >= self.DISCOUNT_THRESHOLD:
            return price * (1 - self.DISCOUNT_RATE)
        return price

    def process_order(self, idx: int):
        """
        Process the order and accumulate the total price
        :param idx: index of the ordered drink
        """
        print(f"{self.drinks[idx]} ordered. Price: {self.prices[idx]} won")
        self.total_price += self.prices[idx]
        self.amounts[idx] += 1

    def display_menu(self) -> str:
        """
        Generate a dynamic menu string
        :return: formatted menu string
        """
        return "".join(
            [f"{k + 1}) {self.drinks[k]} {self.prices[k]} won  "
             for k in range(len(self.drinks))]
        ) + f"{len(self.drinks) + 1}) Exit : "

    def print_summary(self):
        """Print order summary and final price"""
        print("\nProduct\tPrice\tAmount\tSubtotal")
        for i in range(len(self.drinks)):
            if self.amounts[i] > 0:
                print(f"{self.drinks[i]}\t{self.prices[i]}\t{self.amounts[i]}\t"
                      f"{self.prices[i] * self.amounts[i]}")

        discounted_price = self.apply_discount(self.total_price)
        discount = self.total_price - discounted_price

        print(f"\nTotal price before discount: {self.total_price} won")
        if discount > 0:
            print(f"Discount amount: {discount:.0f} won")
            print(f"Total price after discount: {discounted_price:.0f} won")
        else:
            print("No discount applied")
            print(f"Total price: {self.total_price} won")

    def run(self):
        """Execute the order system"""
        while True:
            try:
                menu = int(input(self.display_menu()))
                if 1 <= menu <= len(self.drinks):
                    self.process_order(menu - 1)
                elif menu == len(self.drinks) + 1:
                    print("Order finished~")
                    break
                else:
                    print(f"Menu {menu} is invalid. Please choose from the above menu.")
            except ValueError:
                print("Please enter a valid number. Try again.")

        self.print_summary()


if __name__ == "__main__":
    # menu_drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
    # menu_prices = [2000, 3000, 4900]
    menu_drinks = ["Ice Americano", "Cafe Latte"]
    menu_prices = [2000, 3000]
    cafe = CafeOrder(menu_drinks, menu_prices)
    cafe.run()



'''
클래스
__init__: 초기화 메소드
__new__: 생성자

클래스변수: 모든 인스턴스가 같은 값을 공유
인스턴스 변수: 각 객체마다 값이 다름

self==this: 메소드 실행 인스턴스를 의미

인스턴스 메소드: self를 매개변수로
클래스 메소드: cls를 매개변수로

클래스 메소드, 정적 메소드는 클래스이름.메소드() 요렇게 사용
- 객체 생성없이 사용 가능.

파이썬 클래스 이름-파스칼 표기법?

파이썬은 원래 메인 함수가 없음. 함수, 클래스 아닌 곳부터 그냥 시작. 
다른 언어는 메인함수가 프로그램 엔트리포인트. 

매개변수 타입, 리턴 타입은 가독성을 위해 적는 거임
def fun(parm: int)->float: 이렇게 해놓고 문자열 리턴해도 에러 안남요



'''