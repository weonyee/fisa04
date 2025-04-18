package paymentEx;
//1. **신용카드 결제**와 **네이버페이 결제** 객체를 생성합니다.
//        2. 각 결제 수단으로 **결제**를 처리하고, **환불 기능**을 테스트합니다.
//        3. **정적 메서드**를 사용해 **전체 결제 건수**를 출력합니다.
public class Main {
    public static void main(String[] args) {
        // 신용카드와 NaverPay 결제 객체 생성
        Payment creditCard = new CreditCardPayment(50000);
        Payment naverPay = new NaverPayPayment(30000);

        // 결제 처리 (정적 메서드 사용)
        PaymentProcessor.process(creditCard);
        System.out.println();

        PaymentProcessor.process(naverPay);
        System.out.println();

        // 환불 기능 테스트 (다운캐스팅 사용)
        // instanceof 연산자는 객체가 null 인 경우 false 를 반환합니다.
        // instanceof 연산자를 사용하여 타입을 확인한 후, 안전하게 다운캐스팅할 수 있습니다.
        if (creditCard instanceof Refundable) {
            ((Refundable) creditCard).refund();
        }

        if (naverPay instanceof Refundable) {
            ((Refundable) naverPay).refund();
        }

        System.out.println("-----------");
        int total = Payment.getTotalPayments();
        System.out.println("총 결제 건수: " + total);
    }
}
