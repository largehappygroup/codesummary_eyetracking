public class MyClass {
    
    public String getMessage() {
        StringBuffer sb = new StringBuffer();

        if ( messages != null ) {
            for ( int i = 0; i < messages.size(); i++ ) {
                Object o = messages.elementAt( i );

                if ( o != null ) {
                    sb.append( o.toString() );
                    sb.append( "|n" );
                }
            }
        }
        
        return sb.toString();
    }
} 