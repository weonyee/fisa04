import java.util.HashMap;
import java.util.Map;

public class DataType5 {
    public static void main(String[] args) {
        // HashMap - 파이썬의 딕셔너리와 유사한 자료구조  k로 v를 불러옵니다.
        // Map이 본체, Hash라는 구현방식(알고리즘)을 사용
        // 하나의 키에 하나의 밸류가 매칭됩니다. 키를 통해서 바로 값을 찾기 때문에 속도가 빠르다
        // 검색, 삽입, 삭제가 빈번한 자료들. 대규모 데이터 처리에 적합하다.
        HashMap<String, String> map = new HashMap<String, String>();
        map.put("name", "신짱구");
        map.put("age", "5");
        map.put("name", "신짱아");
        System.out.println(map); // {name=신짱구}

        System.out.println(map.get("name"));
        System.out.println(map.get("name2")); // 없는 key 호출시 null을 출력
        System.out.println(map.getOrDefault("name2", "찾는 값이 없습니다.")); // 없는 key 호출시 null을 출력

        // key만 필요할 때
        System.out.println(map.keySet());
        // value만 필요할 때
        System.out.println(map.values());
        // k-v 쌍이 모두 필요할 때
        System.out.println(map.entrySet());

        // 특정 key가 있는지 확인할 때 - 완전일치
        System.out.println(map.containsKey("name")); // t / f 로 리턴
        System.out.println(map.containsKey("name2"));

        // 특정 value가 있는지 - 완전일치
        System.out.println(map.containsValue("신짱구"));
        System.out.println(map.containsValue("신짱아"));
        System.out.println(map.containsValue("신")); // 일부일치는 불가

        System.out.println(map.size()); // 전체 원소의 개수

        // name key가 있는 값을 삭제
        System.out.println("--------------------------------");
        map.remove("name");
        System.out.println(map);
        map.remove("name2");
        System.out.println(map);

        // 전부다 삭제하되 map이라는 HashMap은 남겨놓고
        map.clear();
        System.out.println(map);

        // 비어있는지 t/f
        System.out.println(map.isEmpty());
    }
}