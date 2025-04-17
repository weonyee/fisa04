package book;

public class Book {

    // 클래스 변수 - 클래스 모두가 공유하는 특정한 값
    // 인스턴스를 만들지 않아도 클래스로 접근 가능한 값
    static int totalNo;

    String name;
    String author;
    int no;
    String comment;

    // 생성자
    // 아무 생성자도 만들지 않으면 컴파일러가 기본 생성자를 넣어줌.
    Book() {
        this("이름없음", "미정", "읽는중"); // default parameter
    }

    Book(String name, String author) {
        this.name = name;
        this.author = author;
        this.comment = "읽는중";
        this.no = ++totalNo;
    }

    Book(String name, String author, String comment) {
        this.name = name;
        this.author = author;
        this.comment = comment;
        this.no = ++totalNo;
    }

    void introduce() {
        System.out.println(this.name);
        System.out.println(this.author);
        System.out.println(this.no); // this 를 생략해도 컴파일러가 넣어줌
        System.out.println(this.comment);
    }

    void finish(String comment){
        System.out.println("다 읽었습니다 !!");
        this.comment = comment;
        System.out.println(this.comment);

    }

    // 책 이름 변경
    void setBookName(String bookName) {
        this.name = bookName;
    }

    static void getTotalReview() {
        System.out.println(totalNo + "권의 책을 읽었습니다.");
    }
}
