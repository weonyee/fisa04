package book;

public class BookReview {
    public static void main(String[] args) {
//        Book book1 = new Book();
//        book1.introduce();
//        book1.finish("어 이 책 안읽어봤나 ...");
//        System.out.println("---------");
//
//        // 책 이름, 작가명 입력받고 싶음
//        Book book2 = new Book("더블", "정해연", "재밌습니다.");
//        book2.introduce();
//        book2.finish("재밌다!!");
//
//        System.out.println("---------");
//        book2.setBookName("두 번째 거짓말");
//        book2.introduce();
//
//        System.out.println("---------");
//        Book.getTotalReview();

        ComicBook comic1 = new ComicBook("짱구", "짱짱구 작가", 5);
        comic1.introduce();
        System.out.println(comic1.star);

        System.out.println("----------");

        ComicBook comic2 = new ComicBook("짱짱짱구", "신형만 작가");
        comic2.getBookStar(); // 자식 클래스의 인스턴스는 사용 가능
        System.out.println(comic2.star);
    }
}
