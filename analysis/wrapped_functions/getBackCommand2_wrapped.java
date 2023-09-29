public class ExampleClass {

    private Command backCommand2;

    public Command getBackCommand2() {
        if ( backCommand2 == null ) {//GEN-END:|92-getter|0|92-preInit
            // write pre-init user code here
            backCommand2 = new Command( "Back", Command.BACK, 0 );//GEN-LINE:| 92-getter | 1 | 92-postInit
            // write post-init user code here
        }//GEN-BEGIN:| 92-getter | 2 |
        return backCommand2;
    }

}