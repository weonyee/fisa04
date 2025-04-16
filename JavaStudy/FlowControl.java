import java.util.Scanner;

public class FlowControl {
    public static void main(String[] args) {
        // 파이썬의 input처럼 표준 입력 값을 받는 scanner라는 객체
        Scanner sc = new Scanner(System.in);
        System.out.println("정수를 입력하세요.");
        int age = sc.nextInt();

        // if문
//        if ( age >= 18) {
//            System.out.println("어른입니다.");
//        } else if (age >= 15) {
//            System.out.println("곧 어른입니다.");
//        } else {
//            System.out.println("baby ~");
//        }

        // switch문
        // 정수, enum, string을 가지고 분기를 만들 때 주로 사용됨
//        switch (age) {
//            case 18:
//                System.out.println("생일이 지났으면 어른입니다!! ㅡㅡ");
//                break;
//            default:
//                if (age >= 19) {
//                    System.out.println("완전히 어른입니다.");
//                } else {
//                    System.out.println("아직 아이입니다.");
//                }
//        }
        // 삼항연산자: 18살보다 어리면 어른이 아닙니다, 18보다 크거나 같으면 어른입니다. 콘솔에 출력
        String result = (age < 18)? "어른이 아닙니다." : "어른입니다.";
        System.out.println(result);

        // get/post 요청을 받아서 구분할 때
        // 사용자 권한에 따라 특정 주소에 접근할 수 있게 할 때
        // 에러코드를 미리 Enum으로 만들어놓고 에러코드를 돌려줄 때

    }
}