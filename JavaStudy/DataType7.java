import java.util.*;

public class DataType7 {
    public static void main(String[] args) {
        // enum - 같은 값을 강제해서 받을 때 : M/F 남 남성 MAN man m
        // enum은 문자열로 작성하지만 개념적으로는 상수(고정된 값)처럼 사용
        // 대문자로 작성
        ArrayList<Language> languageList = new ArrayList<>();
//        languageList.add("JAVA");
        languageList.add(Language.JAVA);
//        languageList.add("go");

        // 개발자가 제한한 옵션이 아닌 옵션은 들어갈 수 없게 강제할 때 사용합니다.
        System.out.println(languageList);
    }
}

enum Language { // enum이라는 키워드로 데이터의 묶음이면서 자료형이 되는 값들을 작성
    JAVA, PYTHON, JS, CSS, HTML
}