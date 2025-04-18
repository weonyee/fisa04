package paymentEx;
//### **인터페이스 - `Refundable`**
//
//        - **환불 기능**을 제공해야 하는 결제 수단을 구분합니다.
//        1. **메서드**:
//        - `refund()` – 결제를 환불합니다.
public interface Refundable {
    void refund();
}
