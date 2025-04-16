public class DataType1 {
    public static void main(String[] args) {
        // num
        int a = 3;
        int b;
        b = 1;
        int c = 2;
        float d = 3.14F;
        System.out.println(d);
        long e;
        e = 15L;
        System.out.println(e);

        // char
        char f = '가';
        System.out.println(f);
        // char f = "가"; -> 에러
        // char f = """가"""; -> 에러

        // boolean -> true / false
        boolean g = true;
        System.out.println(g);

        // 연산
        System.out.println(a+d); // int + float
//        System.out.println(b+g); // int + boolean
    }

}
