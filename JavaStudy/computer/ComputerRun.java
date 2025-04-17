package computer;

public class ComputerRun {
    public static void main(String[] args) {
        NoteBook noteBook = new NoteBook();
        noteBook.run();

        System.out.println("-------------");
        DeskTop deskTop = new DeskTop();
        deskTop.run();
    }

}
