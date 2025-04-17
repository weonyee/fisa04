package book;

public class ComicBook extends Book{

    int star;

    ComicBook(String name, String author){
        super(name, author);
    }

    ComicBook(String name, String author, int star){
//        this.name = name;
//        this.author = author;
        super(name, author); // 부모 클래스 생성자에게 넘겨줌
        this.star = star;
    }

    // 부모 클래스의 특정 메소드를 자식 클래스에서 변경해서 사용
    @Override // 부모한테 이 메서드가 있는지 확인
    void introduce() {
        System.out.println("별점: "+this.star);
        super.introduce();
    }

    void getBookStar() {
        System.out.println(this.star);

    }
}
