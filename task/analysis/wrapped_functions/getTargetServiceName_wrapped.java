public class Parser {
    protected String getTargetServiceName( AddressingHeaders headers ) throws Exception {
        To toURI = headers.getTo();

        if ( toURI == null ) {
            return null;
        }
        String to = toURI.getPath();

        if ( to == null ) {
            return null;
        }
        // set the target service
        return ( to.substring( to.lastIndexOf( '/' ) + 1 ));
    }
}