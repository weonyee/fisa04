package paymentEx;
//- `Payment`를 **상속**합니다.
//- `Refundable` 인터페이스를 **구현**합니다.
//- 결제 금액을 출력하고 결제를 처리합니다.
public class NaverPayPayment extends Payment implements Refundable {

    public NaverPayPayment(double amount) {
        super(amount);
    }

    @Override
    public void processPayment() {
        System.out.println("네이버페이로 " + getAmount() + " 원을 결제합니다.");
    }

    @Override
    public void refund() {
        System.out.println("네이버페이 결제를 환불합니다.");
    }

}
