public class FlowControl3 {
    public static void main(String[] args){

        // ++, -- 증감연산자
        System.out.println("-- 증감 연산자 --");
        int a = 1;
        int b = 2;
        System.out.println(a++); // 후위식
        System.out.println(++a); // 전위식

        // 논리연산자 && || !
        // 앞의 조건이 만족되면 뒤는 보지도 않고 넘어감
        System.out.println("-- 논리 연산자 --");
        int c = 5;
        System.out.println((a>b) && (b<c)); // true
        System.out.println((a>b) || (b<c)); // true
        System.out.println(!(b<c)); // false

        // 비트연산자
        // 모든 조건을 확인함
        System.out.println("-- 비트 연산자 --");
        System.out.println((a>b) & (b<c)); // true
        System.out.println((a>b) | (b<c)); // true
        System.out.println(~b); // -3


    }
}
