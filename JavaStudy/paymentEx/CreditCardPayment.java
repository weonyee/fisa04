package paymentEx;
//- `Payment`를 **상속**합니다.
//- `Refundable` 인터페이스를 **구현**하여 **환불 기능**을 제공합니다.
//        - 결제 금액을 출력하고 결제를 처리합니다.
public class CreditCardPayment extends Payment implements Refundable{
    public CreditCardPayment(double amount) {
        super(amount);
    }

    @Override
    public void processPayment() {
        System.out.println("신용카드로 "  + getAmount() + " 원을 결제합니다.");
//        displayAmount();
    }

    @Override
    public void refund() {
        System.out.println("신용카드 결제를 환불합니다.");
//        displayAmount();
    }
}
