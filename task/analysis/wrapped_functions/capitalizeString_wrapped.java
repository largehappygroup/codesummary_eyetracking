public class StringManipulation {
    public String capitalizeString( String s ) {
        String result = "";
        for( int i = 0; i < s.length(); i++ ) {
            if ( i == 0 || s.substring( i - 1, i ).equals( " " ))
                result += s.substring( i, i + 1 ).toUpperCase();
            else
                result += s.substring( i, i + 1 );          
        }  
        return result;
    }
}