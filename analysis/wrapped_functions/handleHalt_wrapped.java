public class HaltHandler {
    
    public static int handleHalt(int processID) {
        if(processID == 0) {
            Machine.halt();
        } else {
            //System.err.println( "non-root process trying to call halt" );
            return -1;
        }
        Lib.assertNotReached( "Machine.halt() did not halt machine!" );
        return 0;
    }
    
}