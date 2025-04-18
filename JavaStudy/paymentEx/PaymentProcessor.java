package paymentEx;

public class PaymentProcessor {
    public static void process(Payment payment) {
        payment.processPayment();
        payment.displayAmount();
    }
}
