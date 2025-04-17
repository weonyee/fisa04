package computer;

public class DeskTop extends Computer {
    @Override
    void powerOn(){
        System.out.println("본체에 딸린 버튼을 누릅니다.");
    }

    @Override
    void powerOff(int offTime) {
        System.out.println(offTime + "에 종료됩니다.");
    }
}
