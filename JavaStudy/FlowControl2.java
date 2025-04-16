import java.util.Scanner;

public class FlowControl2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("정수를 입력하세요.");
        int num = sc.nextInt();

        // if문
        System.out.println("-- IF 문 --");
        if (num % 2 == 0) {
            System.out.println("짝수입니다.");
        } else {
            System.out.println("홀수입니다.");
        }

        // switch문
        System.out.println("-- switch 문 --");
        int mod = num % 2;
        switch (mod) {
            case 0:
                System.out.println("짝수입니다.");
                break;
            case 1:
                System.out.println("홀수입니다.");
                break;
        }

        // 간단 버젼
        switch (num % 2) {
            case 0 -> System.out.println("짝수입니다.");
            case 1 -> System.out.println("홀수입니다.");
        }

        // 삼항연산자
        System.out.println("-- 삼항연산자 --");
        String check = (num % 2 == 0) ? "짝수입니다." : "홀수입니다.";
        System.out.println(check);
    }
}
