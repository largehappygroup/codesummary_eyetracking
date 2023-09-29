public class MyClass {
    protected void tellAgain( final QName message ) throws RemoteException{
        final AbstractCoordParticipantProxy proxy =
            this.getParticipantProxy();

        if ( State.MESSAGE_CANCEL.equals( message )){
            proxy.cancelOperation( null );

        } else if ( State.MESSAGE_COMPENSATE.equals( message )){
            proxy.compensateOperation( null );

        } else if ( State.MESSAGE_CLOSE.equals( message )){
            proxy.closeOperation( null );

        } else if ( State.MESSAGE_EXITED.equals( message )){
            proxy.exitedOperation( null );

        } else if ( State.MESSAGE_FAULTED.equals( message )){
            proxy.faultedOperation( null );

        } else if ( State.MESSAGE_GETSTATUS.equals( message )){
            proxy.getStatusOperation( null );

        } else{
            throw new IllegalArgumentException( "Sorry, cannot tell a participant " + message );
        }
    }
}