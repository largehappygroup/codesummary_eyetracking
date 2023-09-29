public class MyClass {
    public void makeUniqueParagraphForGlobalWithLength(String global, int length) {
        String paragraph = "";
        String word;

        for (int x = 0; x < length; x++) {
            word = makeUniqueStringForGlobalWithLength(global, (int) (Math.random() * 8) + 2);
            paragraph += word + " ";
        }
        utils.setGlobal(global, paragraph);
    }
}