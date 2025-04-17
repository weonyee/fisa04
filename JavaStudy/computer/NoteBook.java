package computer;

public class NoteBook extends Computer {
    @Override
    void powerOn() {
        System.out.println("전원을 켜세요.");
    }

    @Override
    void powerOff(int offTime) {
        System.out.println(offTime + "에 종료됩니다.");
    }

    // final 태그 때문에 작동하지 않음
//    @Override
//    void run() {
//        super.run();
//        System.out.println("절전모드 실행.....");
//    }
}
