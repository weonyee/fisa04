public class DataType2 {
    public static void main(String[] args) {
        String h = "안녕하세요 문자열입니다.\n2번째 줄\n3번째 줄";
        // 파이썬에선 '' "" """""" 구분하지는 않았으나
        // 자바에서는
        // char -> ''
        // string -> ""
        System.out.println(h);

        String i = """
                
                안녕하세요 문자열입니다.
                2번째 줄
                3번째 줄
                """;
        System.out.println(i);
        // 멀티라인으로 문자열을 저장할 때는 """ 다음 줄부터 내용을 작성
        // 끝날 때는 개행 상관없음

        String a = "가나다";
        String b = "가나다";
        System.out.println(a==b);

        // 동일한 값이라도 서로 다른 메모리 주소를 가지게 됨
        String c = new String("가나다");
        System.out.println(a==c);

        System.out.println("========");

        // 값과 자료형이 일치하는지 보려면 equals()
        System.out.println(a.equals(b));
        System.out.println(a.equals(c));

        String message = "hello world!";
        System.out.println(message.replace("hello", "hi"));

        // %f float, %s string, %d decimal(십진법), %o octa(팔진법) %h hex(십육진법)
        System.out.println(String.format("어제 %d시간 %.2f분 유투브를 봤어요.", 13, 13.677));
    }
}
