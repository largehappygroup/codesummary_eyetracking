Please note that since I am an AI language model, I cannot directly create or parse files. However, I can provide you a java class format corresponding to the given function. Here is the class format you can use:

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

Make sure to add the required imports or modify the code if needed.