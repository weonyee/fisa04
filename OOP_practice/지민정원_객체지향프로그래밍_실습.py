{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/weonyee/fisa04/blob/main/%EC%A7%80%EB%AF%BC%EC%A0%95%EC%9B%90_%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%8B%A4%EC%8A%B5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 0. 일반회원, 프렌즈, 퍼플만 구현(3시 50분까지)"
      ],
      "metadata": {
        "id": "u9Z61EDBBwZ0"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "<img src=\"https://mblogthumb-phinf.pstatic.net/MjAyMDAzMjhfMTc2/MDAxNTg1Mzc3MTY1NTU1.ziX2BsC1YDb_sX561-ZSJl907fhbSudWXjf2qulcw5og.hl2xTYHPDL1nuxClt5h-2XZuz5zTDfFvrFdrLY549wsg.PNG.sexysbkang/%EB%A7%88%EC%BC%93%EC%BB%AC%EB%A6%AC_%EB%93%B1%EA%B8%89.png?type=w800\">\n"
      ],
      "metadata": {
        "id": "t8gHdlAmYzJr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 4명이 1조로 실습\n",
        "\n",
        "1. 일련번호, 상품명, 수량, 가격을 속성으로 가지는 Product 클래스를 구현해보세요. (일련번호는 자동 입력됨)\n",
        "```\n",
        "새우깡 = Product('새우깡', 3, 1500)\n",
        "```\n",
        "가장 기본적인 기능이나 속성은 무엇인지 생각해보세요\n",
        "\n",
        "2. 마켓컬리의 회원등급 목록을 참조하셔서 class Plain, Friends, Purple 클래스를 구현해보세요.\n",
        "    - Plain 클래스에는 buy(상품명, 수량)이라는 인스턴스 메소드가 있으며,\n",
        "    - 이 메소드는 자료형이 Product(isinstance 활용)인 상품은 구매할 수 있고,\n",
        "    - 자료형이 Product가 아닌 상품은 '바코드를 읽을 수 없습니다.'라는 에러메시지를 리턴합니다.\n",
        "\n",
        "3. Product와 회원 클래스를 이용하여 만들 수 있는 또다른 메소드를 하나 고안해 보세요.\n",
        "\n",
        "- 혜택금액은 무시하셔도 됩니다\n"
      ],
      "metadata": {
        "id": "U4TcuJLwB0BU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "```\n",
        "4명이 1장의 노트북파일을 작성해 구글드라이브 안에 저장해주세요\n",
        "\n",
        "코드리뷰 시간을 갖겠습니다. (각팀 발표 10분)\n",
        "\n",
        "일반회원 - 적립률만\n",
        "프렌즈 - 할인쿠폰도\n",
        "퍼플 - 더블 후기 적립금까지\n",
        "\n",
        "```"
      ],
      "metadata": {
        "id": "oxw-pt4Fmdo_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### product"
      ],
      "metadata": {
        "id": "39eS5K5N_7BU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Product:\n",
        "    id_counter = 1\n",
        "    product_count = 0\n",
        "\n",
        "    def __init__(self, pname, __hcount, __price):\n",
        "        self.id = Product.id_counter # 일련번호\n",
        "        self.pname = pname # 상품이름\n",
        "        self.__hcount = __hcount # 상품 재고\n",
        "        self.__price = __price # 상품 가격\n",
        "        Product.id_counter += 1 # 일련번호\n",
        "        Product.product_count += 1 # 상품 종류의 개수\n",
        "\n",
        "    def __str__(self): # 재고 파악\n",
        "        return f\"일련번호: {self.id}, 상품명: {self.pname}, 수량: {self.__hcount}, 가격: {self.__price}\"\n",
        "\n",
        "    # getter\n",
        "    def get_price(self):\n",
        "        return self.__price\n",
        "\n",
        "    def get_hcount(self):\n",
        "        return self.__hcount\n",
        "\n",
        "    def decrease_hcount(self): # 재고 감소\n",
        "        self.__hcount -= 1\n",
        "\n",
        "#상품 입력\n",
        "새우깡 = Product('새우깡', 3, 1500)\n",
        "초코파이 = Product('초코파이', 2, 2000)\n",
        "고래밥 = Product('고래밥', 1, 1000)\n",
        "찰떡파이 = Product('찰떡파이', 5, 6000)\n",
        "\n",
        "prod_dct = {\n",
        "    '새우깡': 새우깡,\n",
        "    '초코파이': 초코파이,\n",
        "    '고래밥': 고래밥,\n",
        "    '찰떡파이': 찰떡파이\n",
        "}\n",
        "\n",
        "print('Product의 총 개수는 ',Product.product_count,\"개 입니다.\")\n",
        "print(새우깡)\n",
        "print(초코파이)\n",
        "print(고래밥)\n",
        "print(찰떡파이)\n"
      ],
      "metadata": {
        "id": "epu9Z2fD06aY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e855ba75-69c9-4252-da8e-e47eb93c29f6"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Product의 총 개수는  4 개 입니다.\n",
            "일련번호: 1, 상품명: 새우깡, 수량: 3, 가격: 1500\n",
            "일련번호: 2, 상품명: 초코파이, 수량: 2, 가격: 2000\n",
            "일련번호: 3, 상품명: 고래밥, 수량: 1, 가격: 1000\n",
            "일련번호: 4, 상품명: 찰떡파이, 수량: 5, 가격: 6000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### plain"
      ],
      "metadata": {
        "id": "ZHctbXB10ZUj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Plain():\n",
        "    # class var\n",
        "    member_num = 0 # 회원 수\n",
        "\n",
        "    # instance var\n",
        "    def __init__(self, __name, __balance, __total = 0, __point = 0.005):\n",
        "        self.__name = __name # 회원 이름\n",
        "        self.__balance = __balance # 잔고\n",
        "        self.__point = __point # 적립률 default 0.005\n",
        "        self.__total = __total # 구매 총액\n",
        "        Plain.member_num += 1 # 회원 수 +1\n",
        "\n",
        "    def get_name(self): # 이름 확인\n",
        "        return self.__name\n",
        "\n",
        "    def get_balance(self): # 잔고 확인\n",
        "        return self.__balance\n",
        "\n",
        "    def get_point(self): # 적립률 확인\n",
        "        return self.__point\n",
        "\n",
        "    def get_total(self): # 구매 총액 확인\n",
        "        return self.__total\n",
        "\n",
        "    def give_point(self, prod):\n",
        "        save_point = round((prod.get_price() * self.__point))\n",
        "        self.__balance += save_point\n",
        "        print(f'|⩊･)ﾉ⁾⁾ [ {save_point} ] 원이 적립되었습니다.(포인트는 현금처럼 사용이 가능합니다.)')\n",
        "        print(f'=> 잔고 : [ {self.__balance} ] 원') # 총 잔고\n",
        "        print('------')\n",
        "\n",
        "    # instance method\n",
        "    def buy(self, prod):\n",
        "        if isinstance(prod, Product):\n",
        "            if self.__balance >= prod.get_price(): # 잔고랑 상품 가격 비교\n",
        "                prod.decrease_hcount()\n",
        "                self.__balance -= prod.get_price()\n",
        "                print('------')\n",
        "                print(f'{prod.pname} 상품을 구매했습니다.')\n",
        "\n",
        "                # 총 구매액\n",
        "                self.__total += prod.get_price()\n",
        "                print(f'총 구매액은 [ {self.__total} ] 원 입니다.')\n",
        "                print(\"\")\n",
        "\n",
        "                self.give_point( prod)\n",
        "\n",
        "            else:\n",
        "                print(f'잔고가 부족하여 {prod.pname}을(를) 구매할 수 없습니다.')\n",
        "\n",
        "        else: return '바코드를 읽을 수 없습니다.' # product에 없는 상품"
      ],
      "metadata": {
        "id": "xE7-7-q9R-aT"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 잘 작동하는지 보기 위함\n",
        "# Plain 회원 생성\n",
        "\n",
        "aaa = Plain('aaa', 50000)\n",
        "aaa.buy('감자')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "KZ5cU7_U8j-t",
        "outputId": "f5a7dda0-e323-497c-8259-54d78a6f956d"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'바코드를 읽을 수 없습니다.'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### friends"
      ],
      "metadata": {
        "id": "E9Et7pp30aeS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Friends(Plain):\n",
        "    def __init__(self,  __name, __balance, _coupon=3, _coupon_value=6000, __point=0.01, __total=0):\n",
        "        # 부모 클래스 Plain의 생성자 호출\n",
        "        super().__init__( __name, __balance,__point, __total)\n",
        "      # Friends 클래스에서만 사용하는 쿠폰과 쿠폰 가치를 초기화\n",
        "        self._coupon = _coupon\n",
        "        self._coupon_value = _coupon_value\n",
        "\n",
        "\n",
        "    def get_coupon(self):\n",
        "        return self._coupon\n",
        "\n",
        "    def use_coupon(self):\n",
        "        if self._coupon > 0:\n",
        "            self._coupon -= 1\n",
        "            print(f\"쿠폰을 사용했습니다! 남은 쿠폰: {self._coupon}개\")\n",
        "            return self._coupon_value\n",
        "        else:\n",
        "            print(\"쿠폰이 없습니다!\")\n",
        "            return 0\n",
        "\n",
        "    def buy_with_coupon(self, prod):\n",
        "        if prod.get_price() >= 6000:  # 상품 가격이 6000원 이상일 때만 쿠폰 사용\n",
        "            if self._coupon > 0:\n",
        "                discount = self.use_coupon()\n",
        "                discounted_price = max(0, prod.get_price() - discount)\n",
        "                if self._Plain__balance >= discounted_price:\n",
        "                    prod.decrease_hcount()\n",
        "\n",
        "                    self._Plain__balance -= discounted_price\n",
        "                    self._Plain__total += discounted_price\n",
        "                    print(f\"{prod}를 쿠폰을 사용하여 구매했습니다. 할인된 가격: {discounted_price}원\")\n",
        "                    print(f\"잔고: {self._Plain__balance}원\")\n",
        "                else:\n",
        "                    print(\"잔고가 부족합니다!\")\n",
        "            else:\n",
        "                print(\"쿠폰이 없습니다!\")\n",
        "                print(\"일반 구매 진행합니다.\")\n",
        "                super().buy(prod)\n",
        "        else:\n",
        "            print(f\"가격이 {prod.get_price()}원으로, 6000원 미만이라 쿠폰을 사용할 수 없습니다.\")\n",
        "            print(\"일반 구매 진행합니다.\")\n",
        "            super().buy(prod)"
      ],
      "metadata": {
        "id": "XSWqa0BOK1bq"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 잘 작동하는지 보기 위함\n",
        "# Friends 회원 생성\n",
        "friend = Friends(\"Alice\",100000)\n",
        "\n",
        "# 쿠폰 사용 여부를 확인하며 상품 구매\n",
        "\n",
        "friend.buy_with_coupon(찰떡파이)  # 쿠폰이 없어서 일반 구매"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4CGwf3UleYXx",
        "outputId": "592dea2b-287f-4d8c-ec29-305c9a25a8df"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "쿠폰을 사용했습니다! 남은 쿠폰: 2개\n",
            "일련번호: 4, 상품명: 찰떡파이, 수량: 4, 가격: 6000를 쿠폰을 사용하여 구매했습니다. 할인된 가격: 0원\n",
            "잔고: 100000원\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### purple"
      ],
      "metadata": {
        "id": "LwFzv9_r0b6h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Purple(Friends):\n",
        "    def __init__(self, __name, __balance, _coupon=4, _coupon_value=10000, __point=0.07, __total=0):\n",
        "        super().__init__( __name, __balance, __point, __total)\n",
        "      #  클래스에서만 사용하는 쿠폰과 쿠폰 가치를 초기화\n",
        "        self._coupon = _coupon\n",
        "        self._coupon_value = _coupon_value\n",
        "    def benefit(self, prod):\n",
        "        review = input('리뷰를 작성하셨나요?: ')\n",
        "        if review == 'O':\n",
        "            print('[ 더블 후기 적립금 ]이 제공되었습니다.')\n",
        "            print('후기를 작성하시면 적립금이 두 배가 됩니다.')\n",
        "            super().give_point(prod)\n",
        "\n",
        "        else: print('다음에는 꼬옥 리뷰를 작성해주세요.')"
      ],
      "metadata": {
        "id": "IZLXg-2e0cyG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 회원 생성"
      ],
      "metadata": {
        "id": "4HYUuCLaaMyP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def create_member(__name, __balance, _prev):\n",
        "    if _prev < 150000:\n",
        "        obj = Plain(n, bal)\n",
        "        p = input(\"어떤 것을 구매하시나요?: \")\n",
        "        if p in prod_dct:\n",
        "            selected_product = prod_dct[p]\n",
        "            print(obj.buy(selected_product))\n",
        "\n",
        "    elif prev < 1000000:\n",
        "        obj = Friends(n, bal)\n",
        "        p = input(\"어떤 것을 구매하시나요?: \")\n",
        "        if p in prod_dct:\n",
        "            selected_product = prod_dct[p]\n",
        "            print(obj.buy_with_coupon(selected_product))\n",
        "\n",
        "    else:\n",
        "        obj = Purple(n, bal)\n",
        "        p = input(\"어떤 것을 구매하시나요?: \")\n",
        "        if p in prod_dct:\n",
        "            selected_product = prod_dct[p]\n",
        "            print(obj.buy_with_coupon(selected_product))\n",
        "            print(obj.benefit(selected_product))"
      ],
      "metadata": {
        "id": "stowcWkjY9df"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 실행"
      ],
      "metadata": {
        "id": "lskr6EGZ0dHS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### plain"
      ],
      "metadata": {
        "id": "Z0wPOs3loUJJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('------')\n",
        "print('시작')\n",
        "print('------')\n",
        "n, bal, prev = input('이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): ').split()\n",
        "bal = int(bal[:-1])\n",
        "prev = int(prev[:-1])\n",
        "create_member(n, bal, prev)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "AftURvVGoWWI",
        "outputId": "8fd1e1b1-9454-4a85-c89e-899d3dfbaeeb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "------\n",
            "시작\n",
            "------\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-18daac79a742>\u001b[0m in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'시작'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'------'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mn\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbal\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mprev\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0mbal\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbal\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mprev\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprev\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### friends"
      ],
      "metadata": {
        "id": "9otfeaNPktNy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('------')\n",
        "print('시작')\n",
        "print('------')\n",
        "n, bal, prev = input('이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): ').split()\n",
        "bal = int(bal[:-1])\n",
        "prev = int(prev[:-1])\n",
        "create_member(n, bal, prev)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OYtrXUYWkxQA",
        "outputId": "81b548d4-4338-44c9-cebd-8d0b127a9b08"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "------\n",
            "시작\n",
            "------\n",
            "이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): 허정원 10000원 800000원\n",
            "어떤 것을 구매하시나요?: 찰떡파이\n",
            "쿠폰을 사용했습니다! 남은 쿠폰: 2개\n",
            "일련번호: 4, 상품명: 찰떡파이, 수량: 1, 가격: 6000를 쿠폰을 사용하여 구매했습니다. 할인된 가격: 0원\n",
            "잔고: 10000원\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('------')\n",
        "print('시작')\n",
        "print('------')\n",
        "n, bal, prev = input('이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): ').split()\n",
        "bal = int(bal[:-1])\n",
        "prev = int(prev[:-1])\n",
        "create_member(n, bal, prev)"
      ],
      "metadata": {
        "id": "hBbWhB0Roela"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### purple"
      ],
      "metadata": {
        "id": "eZ1kZ9eVkrOY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print('------')\n",
        "print('시작')\n",
        "print('------')\n",
        "n, bal, prev = input('이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): ').split()\n",
        "bal = int(bal[:-1])\n",
        "prev = int(prev[:-1])\n",
        "create_member(n, bal, prev)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tFyTO-CW_5Nj",
        "outputId": "8c6f61ea-0970-4af4-e362-8f0829a32641"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "------\n",
            "시작\n",
            "------\n",
            "이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): 허정원 100000원 19900000원\n",
            "어떤 것을 구매하시나요?: 찰떡파이\n",
            "쿠폰을 사용했습니다! 남은 쿠폰: 3개\n",
            "일련번호: 4, 상품명: 찰떡파이, 수량: 2, 가격: 6000를 쿠폰을 사용하여 구매했습니다. 할인된 가격: 0원\n",
            "잔고: 100000원\n",
            "None\n",
            "리뷰를 작성하셨나요?: O\n",
            "[ 더블 후기 적립금 ]이 제공되었습니다.\n",
            "후기를 작성하시면 적립금이 두 배가 됩니다.\n",
            "|⩊･)ﾉ⁾⁾ [ 0 ] 원이 적립되었습니다.(포인트는 현금처럼 사용이 가능합니다.)\n",
            "=> 잔고 : [ 100000 ] 원\n",
            "------\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('------')\n",
        "print('시작')\n",
        "print('------')\n",
        "n, bal, prev = input('이름과 잔고, 전월 실적을 입력해주세요.(이름/___원/___원): ').split()\n",
        "bal = int(bal[:-1])\n",
        "prev = int(prev[:-1])\n",
        "create_member(n, bal, prev)"
      ],
      "metadata": {
        "id": "QfMKpCEgrCdW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "oEqn4DGZrC8t"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
