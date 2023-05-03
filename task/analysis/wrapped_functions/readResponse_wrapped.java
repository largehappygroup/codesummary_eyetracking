public class ResponseReader {
   
    private String readResponse( InputStream stream ) {
        BufferedReader input = new BufferedReader( new InputStreamReader( stream ));
        StringBuffer sb = new StringBuffer();
        String line;
        try {
            line = input.readLine();
        } catch ( IOException e ) {
            line = null;
        }
        while ( line != null ) {
            if ( !line.trim().equals( "" ) ) {
                if ( sb.length() > 0 ) sb.append( "|n" );
                sb.append( line );
            }
            try {
                line = input.readLine();
            } catch ( IOException e ) {
                line = null;
            }
        }
        return sb.toString();
    }
    
}