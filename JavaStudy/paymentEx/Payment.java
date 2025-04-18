package paymentEx;
//- 모든 결제 수단이 가져야 할 **공통 속성**과 **기능**을 정의합니다.
//        1. **필드**:
//        - `amount` (double): 결제 금액 (**접근 제어자** 사용)
//2. **메서드**:
//        - **추상 메서드** `processPayment()` – 결제를 처리합니다.
//        - **일반 메서드** `displayAmount()` – 결제 금액을 출력합니다.
//3. **정적 필드**와 **정적 메서드**를 사용해 **전체 결제 건수**를 관리합니다.

public abstract class Payment {
    // 인스턴스 변수
    private double amount;

    // 정적 필드 - 결제 건수
    private static int totalPayments = 0;

    // 생성자
    public Payment(double amount) {
        this.amount = amount;
        totalPayments ++;
    }

    // 추상메서드
    public abstract void processPayment();

    // 일반메서드
    public void displayAmount() {
        System.out.println("결제 금액: "+amount + "원");
    }

    // 정적 메서드
    public static int getTotalPayments() {
        return totalPayments;
    }

    public double getAmount() {
        return amount;
    }

}
