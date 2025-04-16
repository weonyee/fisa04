import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class DataType4 {
    public static void main(String[] args) {

        // ArrayList: Array를 list 구조로 쓰는 가변 자료형
        ArrayList arr = new ArrayList();
        System.out.println(arr); // []
        arr.add(1);
        arr.add("가나다");
        arr.add(true);
        arr.add(3.14);
        System.out.println(arr); // [1, 가나다, true, 3.14]

        // 정적 타입으로 자료형을 고정해서 사용
        ArrayList<String> arr2 = new ArrayList<String>();
        arr2.add("가나다"); // 값을 추가
        System.out.println(arr2);
        // arr2.add(3); -> 자료형 안맞아서 에러
        arr2.add("마바사");
        arr2.add("아자차");
        System.out.println(arr2);
        // System.out.println(arr2[1]); -> Array의 방식을 값을 부르기 때문에 에러
        System.out.println(arr2.get(0)); // 특정 인덱스 조회
        arr2.set(1, "마마마"); // 수정
        System.out.println(arr2);

        // 실수 -11, 3, 1, 0, -3, 123이 들어있는 arraylist arr3를 만들고 순서대로 정렬
        // generic - <자료형>을 넣어서 해당 집합자료형에서 사용할 자료형을 고정
        // 자바의 기본 자료형들은 '기본'값이 바로 메모리에 들어가는 구조라 ArrayList
        // 가변성을 위해 '메모리 주소'를 기억하도록 설계되어 있음
        // int, float, boolean 등 기본 자료형을 감싸주는 wrapper 클래스 사용
        ArrayList<Integer> arr3 = new ArrayList<>(Arrays.asList(0, 1, -11, -3, 3, 123));
        Integer[] arr4 = {0, 1, -11, -3, 3, 123};
        arr3.sort(Comparator.naturalOrder()); // sort() 메소드는 파괴적: 결과는 리턴하지 않음
        System.out.println(arr3);
        Arrays.sort(arr4, Comparator.reverseOrder());
        System.out.println(Arrays.toString(arr4));


    }
}
