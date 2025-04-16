import java.math.BigDecimal;
import java.util.Arrays;

public class DataType3 {
    public static void main(String[] args) {

        // 배열
        // 각 방에는 똑같은 자료형이 들어감
        // 자료형[] 변수명 = {값1, 값2, 값3};

        // 선언 & 대입
        System.out.println("선언 & 대입");
        int[] arr1 = {1, 2, 3};
        System.out.println(arr1); // 메모리 주소 출력됨 [I@b4c966a
        System.out.println(Arrays.toString(arr1)); // [1, 2, 3]

        int[] arr2 = {4, (int) 2.15, 2};
        System.out.println(Arrays.toString(arr2));
        arr2[2] = 15;
        System.out.println(Arrays.toString(arr2));

        // 선언 -> 대입
        System.out.println("선언 -> 대입");
        int[] arr3 = new int[3];
        System.out.println(Arrays.toString(arr3)); // default값 0으로 채워짐 [0, 0, 0]
        arr3[2] = 32;
        System.out.println(Arrays.toString(arr3));

        float[] arr4 = new float[3]; // default: 0
        arr4[1] = 2; // 정수를 실수 배열에 넣을 때는 자동 형변환됨
        System.out.println(Arrays.toString(arr4));

        boolean[] arr5 = new boolean[3]; // default: false
        System.out.println(Arrays.toString(arr5)); // [false, false, false]
        // string - default: null

        // 고정 소수점 - big decimal
        System.out.println("고정 소수점");
        BigDecimal[] arr6 = new BigDecimal[3];
        System.out.println(Arrays.toString(arr6)); // default: null
        arr6[0] = BigDecimal.valueOf(3.114);
        arr6[1] = new BigDecimal(3.12);
        arr6[2] = new BigDecimal("3.13");
        System.out.println(Arrays.toString(arr6));

    }
}
