public class MyClass {

    protected void doOutput(int lvl, Object message, Throwable t) {
        System.out.print("[");
        System.out.print(_taskName);
        System.out.print(" - ");
        System.out.print(LEVEL[lvl]);
        System.out.print("]");
        System.out.println(message);

        if (t != null) {
            t.printStackTrace();
        }
    }

}