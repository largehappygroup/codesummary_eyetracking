public class MyClass {
    private void setTopAttributes( Attributes from ) {
        for ( int i = 0; i < from.getLength(); i++ ) {
            topMenu.setAttribute( from.getLocalName( i ), from.getValue( i ) );
            topMenu.setAttribute( from.getQName( i ), from.getValue( i ) );
        }
    }
}