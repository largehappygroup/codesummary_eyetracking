public class ExitFunction {
    public void exit( EventObject event ) {
        for ( ExitListener listener : exitListeners ) {
            if ( !listener.canExit( event )) {
                return;
            }
        }
        try {
            for ( ExitListener listener : exitListeners ) {
                try {
                    listener.willExit( event );
                } catch ( Exception e ) { 
                    logger.log( Level.WARNING, "ExitListener.willExit() failed", e );
                }
            }
            shutdown();
        } catch ( Exception e ) { 
            logger.log( Level.WARNING, "unexpected error in Application.shutdown()", e );
        }
        finally {
            end();
        }
    } 
}