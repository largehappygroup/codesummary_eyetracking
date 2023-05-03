public class RegexMatcher {

    public String toString() {
        StringBuffer sb = new StringBuffer();

        sb.append( "java.util.regex.Matcher" );
        sb.append( "[pattern=" + pattern() );
        sb.append( " region=" );
        sb.append( regionStart() + "," + regionEnd() );
        sb.append( " lastmatch=" );

        if (( first >= 0 ) && ( group() != null )) {
            sb.append( group() );
        }
        sb.append( "]" );
        return sb.toString();
    }

}