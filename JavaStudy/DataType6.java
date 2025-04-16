import java.util.*;

public class DataType6 {
    public static void main(String[] args) {
        // Set - 중복을 허용하지 않는 자료형
        // Set이 본체, Hash 구현방식
        Set<String> set = new HashSet<String>();

        System.out.println(set); // [] 텅 비어있을 때
        set.add("허정원");
        set.add("허정원");
        set.add("허정원");
        set.add("허정땡");
        set.add("허정팔");
        System.out.println(set); // [허정원, 허정땡, 허정팔] 중복 불가

        Set<String> set2 = new TreeSet<>(set); // 형변환
        System.out.println(set2);
        set2.add("정팔엄마");

        System.out.println(set2);

        System.out.println(set2.size());
        System.out.println(set2.contains("정팔")); // 완전일치만 사용

        // Array나 다른 참조자료형에서 중복되는 값을 걸러낼 때 사용합니다.
        String[] animals = {"양", "염소", "염소", "염소", "염소", "양", "알파카", "알파카",
                "흑염소", "흑염소", "염소(흑)", "양(아기)", "산양"};
        // Set으로 형변환하셔서 중복값을 걸러내 주세요.
//        Set<String> animals2 = new HashSet<>(List.of(animals)); // Array를 List로 형변환 한 다음에
        Set<String> animals2 = new HashSet<>(Arrays.asList(animals)); // Array를 List로 형변환 한 다음에
        // Array는 고정된 방 크기와 자료형 배열
        // 가변 자료형(ArrayList, Map, Set)으로 변경하기 위해서
        // 중간에 잠시 가변 자료형인 List를 거쳐서 최종 자료형으로 형변환하게 됩니다. = List.of() / Arrays.asList()의 역할
        // int -> Integer로 감싸준 것처럼 나란히 붙은 고정된 방은 떨어뜨려서 List의 참조객체들로 변환
        animals2.remove("양");
        System.out.println(animals2);
    }
}